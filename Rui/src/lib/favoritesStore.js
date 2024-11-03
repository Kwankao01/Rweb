import { writable } from 'svelte/store';

export const favorites = writable([]);

export function addToFavorites(item) {
    if (!item.type) {
        console.warn('Adding item without type:', item);
        return;
    }

    favorites.update(items => {
        const exists = items.some(i => i.slug === item.slug);
        if (!exists) {
            console.log('Adding item with type:', item.type); // เพิ่ม debug log
            return [...items, item];
        }
        return items;
    });
}

export function removeFromFavorites(slug) {
    favorites.update(items => items.filter(item => item.slug !== slug));
}