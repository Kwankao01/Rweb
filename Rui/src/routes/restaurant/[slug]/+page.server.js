import { posts } from '../data.js';

export function load({ params }) {
    const restaurant = posts.find(post => post.slug === params.slug);
    
    if (!restaurant) {
        return {
            status: 404,
            error: new Error('Restaurant not found')
        };
    }

    return {
        restaurant
    };
}