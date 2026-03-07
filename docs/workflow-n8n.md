# veilleur — n8n Workflow

## Overview

```
Gmail Trigger → Extract Links → Flatten Links → Loop Over Links ─┐
                                                                   │
              Prepare Output → Write File ← (done) ───────────────┤
                                                                   │
                    Wait → Scrape via Jina → Merge Content ← (loop)┘
```

The workflow triggers on each new email, extracts useful links, scrapes their content via Jina Reader, and saves everything to `data/raw/`.

---

## Importing the workflow

1. In n8n → **⋮** menu (three dots, top right) → **Import from File**
2. Select `n8n/workflow-veilleur.json`
3. **Reconnect the Gmail credential**: click on the "Gmail Trigger" node → select the `Gmail OAuth2 — veilleur` credential
4. Activate the workflow (toggle in the top right)

---

## Node details

### 1. Gmail Trigger

**Role**: Triggers the workflow on each new email received.

- **Event**: Message Received
- **Poll**: every minute (adjustable)
- **Simplify**: disabled (we want the raw HTML to extract links)
- **Credential**: Gmail OAuth2 — veilleur

> **Tip**: To test, send yourself a test email containing a few links to `veilleur.allienne@gmail.com`, then click "Execute workflow" in n8n.

### 2. Extract Links (Code)

**Role**: Parses the email HTML and extracts all `<a href>` links.

Automatic filters — the following are removed:
- Tracking links (`click.`, `doubleclick`, `analytics`)
- Unsubscribe and preference management links
- Social media links (Facebook, Twitter, LinkedIn sharing)
- Image links (`.png`, `.jpg`, `.gif`, `.svg`)
- Marketing links (`mailchimp`, `sendgrid`, `convertkit`, `beehiiv`)
- Very short links (< 20 characters)

**Output**: one object per email with `newsletter_name`, `from`, `received_at`, `links[]`, `link_count`.

### 3. Flatten Links (Code)

**Role**: Transforms the newsletter-grouped link list into individual items for loop scraping.

One email with 8 links → 8 output items, each carrying the metadata from the original newsletter.

### 4. Loop Over Links (Split In Batches)

**Role**: Processes links one by one to avoid overloading Jina Reader.

- **Batch Size**: 1
- **Output 0 (done)**: when all links are scraped → sends to "Prepare Output"
- **Output 1 (loop)**: for each link → sends to "Wait"

### 5. Wait

**Role**: 1.5-second pause between each Jina request to respect the rate limit.

Jina Reader offers ~200 free requests per day. With 4-7 newsletters and ~5-10 links each, that's 20 to 70 requests/day → well within limits.

### 6. Scrape via Jina (HTTP Request)

**Role**: Fetches the content of each link in markdown via Jina Reader.

- **URL**: `https://r.jina.ai/{{ $json.url }}`
- **Method**: GET
- **Header**: `Accept: text/markdown`
- **Timeout**: 15 seconds
- **On Error**: continue (if a link fails, move on to the next one)

Jina Reader returns the page content in clean, ad-free markdown format. It's free and requires no API key.

### 7. Merge Content (Code)

**Role**: Reattaches the scraped content to the original link metadata (URL, title, newsletter, date).

Also marks whether scraping succeeded or not (`scraped: true/false`).

### 8. Prepare Output (Code)

**Role**: Aggregates all results, groups by newsletter, and prepares binary data for file writing.

- **Grouping**: one JSON file per newsletter
- **Naming**: `YYYY-MM-DD-newsletter-01.json`, `YYYY-MM-DD-newsletter-02.json`, etc. (date-prefixed, handles newsletters arriving at different times)

### 9. Write File (Read/Write Files from Disk)

**Role**: Writes each prepared binary file to `/data/veilleur/raw/`.

The Docker volume mounts `/data/veilleur` to `/Users/sn0rks/Code/github.com/allienna/veilleur/data`, so the files are directly accessible in the repo.

---

## Output format

Each `YYYY-MM-DD-newsletter-NN.json`:

```json
{
  "newsletter": "Email subject",
  "from": "sender@example.com",
  "received_at": "2026-03-06T14:30:00.000Z",
  "links": [
    {
      "url": "https://example.com/article",
      "title": "Title extracted from the HTML link",
      "content": "# Article title\n\nFull markdown content scraped by Jina...",
      "scraped": true
    }
  ]
}
```

---

## Testing the workflow

1. Send a test email to `veilleur.allienne@gmail.com` containing links to tech articles
2. In n8n, click **Execute workflow** (or wait for the next poll)
3. Check each node by clicking on it to see the output
4. Verify the created file:
   ```bash
   cat /Users/sn0rks/Code/github.com/allienna/veilleur/data/raw/$(date +%Y-%m-%d)-newsletter-01.json
   ```

---

## Troubleshooting

### Gmail Trigger doesn't fire
- Check that the workflow is **activated** (green toggle in the top right)
- Check that the Gmail credential is connected
- The first poll can take up to 1 minute

### Jina Reader returns empty content
- Some sites block scrapers — this is normal, the link will be marked `scraped: false`
- Sites behind a paywall will only return the beginning of the article

### Filesystem write error
- Check that the Docker volume is properly mounted: `docker exec n8n-veille ls /data/veilleur/raw/`
- The `data/raw/` folder must exist in the repo before n8n can write to it

### Too many extracted links (noise)
- Adjust the filters in the "Extract Links" node: add domains to the `skip` list
- This can be refined after a few days of use by observing what gets through
