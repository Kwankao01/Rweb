import { posts } from '../data.js';

export function load({ params }) {
    const hotel = posts.find(post => post.slug === params.slug);
    
    if (!hotel) {
        return {
            status: 404,
            error: new Error('Hotel not found')
        };
    }

    return {
        hotel
    };
}