import { posts } from './data.js';

export function load() {
    try {
        const cities = [...new Set(posts.map(post => post.city))].sort();
        return {
            restaurants: posts,
            cities
        };
    } catch (error) {
        console.error('Error loading restaurant data:', error);
        return {
            restaurants: [],
            cities: []
        };
    }
}