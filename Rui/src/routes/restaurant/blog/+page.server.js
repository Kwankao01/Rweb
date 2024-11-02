import { posts } from './data.js';

/**
 * @returns {{ summaries: { slug: string; title: string }[] }}
 */
export function load() {
    return {
        summaries: posts.map((post) => ({
            slug: post.slug,
            title: post.title
        }))
    };
}