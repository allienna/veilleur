import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { getCollection } from 'astro:content';

export async function GET(context: APIContext) {
  const [articles, blogPosts] = await Promise.all([
    getCollection('articles'),
    getCollection('blog'),
  ]);

  const items = [
    ...articles.map((article) => ({
      title: article.data.title,
      pubDate: article.data.date,
      link: new URL(`articles/${article.slug}/`, context.site).toString(),
    })),
    ...blogPosts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.date,
      ...(post.data.description ? { description: post.data.description } : {}),
      link: new URL(`blog/${post.slug}/`, context.site).toString(),
    })),
  ].sort((a, b) => b.pubDate.valueOf() - a.pubDate.valueOf());

  return rss({
    title: 'Le Veilleur',
    description: 'Veille technologique quotidienne et articles — Aurélien Allienne.',
    site: context.site,
    items,
  });
}
