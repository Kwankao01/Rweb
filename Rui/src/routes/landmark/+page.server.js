import { posts } from './data.js';

export function load() {
    try {
        const cities = [...new Set(posts.map(post => post.city))].sort();
        return {
            landmarks: posts,
            cities
        };
    } catch (error) {
        console.error('Error loading landmark data:', error);
        return {
            landmarks: [],
            cities: []
        };
    }
}