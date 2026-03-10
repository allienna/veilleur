import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import tailwind from '@astrojs/tailwind';
import { remarkReadingTime } from './remark-reading-time.mjs';

export default defineConfig({
  site: 'https://allienna.github.io',
  base: '/veilleur',
  integrations: [mdx(), tailwind()],
  output: 'static',
  markdown: {
    remarkPlugins: [remarkReadingTime],
  },
});
