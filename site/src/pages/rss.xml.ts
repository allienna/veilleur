import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { getCollection } from 'astro:content';

export async function GET(context: APIContext) {
  const articles = await getCollection('articles');
  const sorted = articles.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());

  return rss({
    title: 'Le Veilleur',
    description: 'Veille technologique quotidienne — articles générés depuis les meilleures newsletters tech.',
    site: context.site,
    items: sorted.map((article) => ({
      title: article.data.title,
      pubDate: article.data.date,
      link: new URL(`articles/${article.slug}/`, context.site).toString(),
    })),
  });
}
