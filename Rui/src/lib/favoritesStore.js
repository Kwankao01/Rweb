import { writable, get } from 'svelte/store';
import { browser } from '$app/environment';
import { token } from '$lib/stores/auth.js';
 
const storedFavorites = browser ? JSON.parse(localStorage.getItem('favorites') || '[]') : [];
export const favorites = writable(storedFavorites);
export const popupMessage = writable('');
export const showPopup = writable(false);
 
export async function addToFavorites(item) {
    try {
        const currentToken = get(token);
       
        if (!currentToken) {
            throw new Error('No authentication token available');
        }
 
        const response = await fetch('/api/favorites', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${currentToken}`,
            },
            body: JSON.stringify(item),
            credentials: 'include'
        });
       
        if (response.ok) {
            favorites.update(items => {
                const newItems = [...items, item];
                if (browser) {
                    localStorage.setItem('favorites', JSON.stringify(newItems));
                }
                return newItems;
            });
            displayPopup("Added to favorites");
        } else {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Failed to add to favorites');
        }
    } catch (error) {
        console.error('Error adding to favorites:', error);
        displayPopup("Failed to add to favorites");
    }
}
 
export async function removeFromFavorites(slug) {
    try {
        const currentToken = get(token);
       
        if (!currentToken) {
            throw new Error('No authentication token available');
        }
 
        let itemToRemove;
        favorites.update(items => {
            itemToRemove = items.find(item => item.slug === slug);
            return items.filter(item => item.slug !== slug);
        });
 
        if (!itemToRemove) {
            throw new Error('Item not found in favorites');
        }
 
        const response = await fetch(`/api/favorites/${itemToRemove.id}?type=${itemToRemove.type}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${currentToken}`,
            },
            credentials: 'include'
        });
       
        if (response.ok) {
            if (browser) {
                const updatedFavorites = get(favorites);
                localStorage.setItem('favorites', JSON.stringify(updatedFavorites));
            }
            displayPopup("Removed from favorites");
        } else {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Failed to remove from favorites');
        }
    } catch (error) {
        console.error('Error removing from favorites:', error);
        displayPopup("Failed to remove from favorites");
    }
}
 
export async function loadFavorites() {
    try {
        const currentToken = get(token);
       
        if (!currentToken) {
            favorites.set([]);
            return;
        }
 
        const response = await fetch('/api/favorites/', {
            headers: {
                'Authorization': `Bearer ${currentToken}`
            },
            credentials: 'include'
        });
       
        if (response.ok) {
            const data = await response.json();
            console.log('Raw favorites data:', data);
            favorites.set(data);
        } else {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Failed to load favorites');
        }
    } catch (error) {
        console.error('Error loading favorites:', error);
        favorites.set([]); // Set empty array on error
    }
}
 
function displayPopup(message) {
    popupMessage.set(message);
    showPopup.set(true);
    setTimeout(() => showPopup.set(false), 2000);
}