import { posts } from '../data.js';

export function load({ params }) {
    const landmark = posts.find(post => post.slug === params.slug);
    
    if (!landmark) {
        return {
            status: 404,
            error: new Error('landmark not found')
        };
    }

    return {
        landmark
    };
}