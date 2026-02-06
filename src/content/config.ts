import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    // Required fields
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),

    // Optional fields
    author: z.string().optional(),
    category: z.enum(['AI Strategy', 'Implementation', 'Industry', 'Career']).optional(),
    tags: z.array(z.string()).optional().default([]),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),

    // SEO overrides (optional)
    seoTitle: z.string().optional(),
    seoDescription: z.string().optional(),

    // Content flags
    featured: z.boolean().optional().default(false),
    draft: z.boolean().optional().default(false),
  }),
});

export const collections = {
  blog: blogCollection,
};
