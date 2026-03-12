import { defineCollection, z } from 'astro:content';

const articles = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    themes: z.array(z.string()).default([]),
    sources: z.number().optional(),
    image: z.string().optional(),
  }),
});

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    description: z.string(),
    themes: z.array(z.string()).default([]),
    image: z.string().optional(),
  }),
});

const fiches = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    url: z.string(),
    authors: z.array(z.string()).optional(),
    keywords: z.array(z.string()).default([]),
    theme: z.string().default('Autre'),
    tone: z.string().optional(),
    used_in: z.array(z.string()).default([]),
  }),
});

export const collections = { articles, blog, fiches };
