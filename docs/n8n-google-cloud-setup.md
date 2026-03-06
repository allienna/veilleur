# veilleur — Setup n8n & Google Cloud OAuth2

## Prerequisites

- Docker installed on Mac
- Dedicated Gmail account: `veilleur.allienne@gmail.com`

---

## 1. Start n8n locally

```bash
cd /Users/sn0rks/Code/github.com/allienna/veilleur/n8n
docker-compose up -d
```

Access: http://localhost:5678

The `docker-compose.yml` mounts the project's `data/` directory to `/data/veilleur` inside the container, allowing n8n to write scraped files directly into the project tree.

---

## 2. Create the Google Cloud project

1. Sign in to https://console.cloud.google.com with `veilleur.allienne@gmail.com`
2. Create a new project named **veilleur**
3. Enable the Gmail API:
   - APIs & Services → Library
   - Search for "Gmail API" → **Enable**

---

## 3. Configure the OAuth consent screen

1. APIs & Services → **OAuth consent screen**
2. User type: **External**
3. App name: `veilleur`
4. Contact email: `veilleur.allienne@gmail.com`
5. Scopes: add `https://www.googleapis.com/auth/gmail.readonly`

### Add the test user

This step is mandatory — without it, Google blocks access with a 403 `access_denied` error ("veilleur has not completed the Google verification process").

1. APIs & Services → OAuth consent screen → **Audience**
2. **Test users** section → **Add users**
3. Add `veilleur.allienne@gmail.com`
4. Save

> **Note**: In "Testing" mode, tokens expire after 7 days. You'll need to reconnect the credential in n8n at that point. To avoid this long-term, you can publish the app (no Google verification needed for personal use).

---

## 4. Create the OAuth credentials

1. APIs & Services → **Credentials** → **Create Credentials** → **OAuth client ID**
2. Application type: **Web application**
3. Name: `n8n`
4. Authorized redirect URI: `http://localhost:5678/rest/oauth2-credential/callback`
   (this URL can be found in n8n when creating the Gmail credential)
5. Click **Create**
6. Copy the **Client ID** and the **Client Secret**

---

## 5. Connect n8n to Gmail

1. In n8n → left sidebar → **Credentials** → **Create new**
2. Search for **Gmail OAuth2 API**
3. Paste the **Client ID** and the **Client Secret**
4. Click **Sign in with Google**
5. Google displays "Google hasn't verified this app" → click **Continue** (this is normal for an app in test mode)
6. Authorize read access to Gmail
7. Result: **Connection successful**

---

## Troubleshooting

### 403 error "Access blocked: veilleur has not completed the Google verification process"

The email used to sign in is not in the test users list. Add the email in OAuth consent screen → Audience → Test users.

### Token expires after 7 days

This is expected behavior in "Testing" mode with External user type. Two options:
- Reconnect the credential in n8n (Credentials → Gmail OAuth2 → Sign in with Google)
- Publish the app in Google Cloud Console (OAuth consent screen → Publishing status → Publish) — no Google verification needed for personal use with fewer than 100 users

### n8n won't start

```bash
cd /Users/sn0rks/Code/github.com/allienna/veilleur/n8n
docker-compose logs -f
```
