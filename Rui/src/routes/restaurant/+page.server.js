import { posts } from './data.js';

export function load() {
    return {
        summaries: posts.map((post) => ({
            slug: post.slug,
            title: post.title,
            image: post.image,
            content: post.content,
            rating: post.rating,
            reviews: post.reviews,
            location: post.location,
            city: post.city
        })),
    };
}