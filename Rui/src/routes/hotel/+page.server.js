import { posts } from './data.js';

export function load() {
    try {
        const cities = [...new Set(posts.map(post => post.city))].sort();
        return {
            hotels: posts,
            cities
        };
    } catch (error) {
        console.error('Error loading hotel data:', error);
        return {
            hotels: [],
            cities: []
        };
    }
}