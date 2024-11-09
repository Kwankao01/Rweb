import { writable } from 'svelte/store';

export const favorites = writable([]);
export const popupMessage = writable('');
export const showPopup = writable(false);

export function addToFavorites(item) {
    console.log('Adding to favorites:', item); 
    favorites.update(items => [...items, item]);
    displayPopup("Added to favorites");
}

export function removeFromFavorites(slug) {
    console.log('Removing from favorites:', slug); 
    favorites.update(items => items.filter(item => item.slug !== slug));
    displayPopup("Removed from favorites");
}

function displayPopup(message) {
    popupMessage.set(message);
    showPopup.set(true);
    setTimeout(() => {
        showPopup.set(false);
    }, 2000);
}