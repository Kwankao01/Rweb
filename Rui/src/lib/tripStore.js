import { writable, get } from 'svelte/store';
import { browser } from '$app/environment';
import { token } from '$lib/stores/auth.js';

// Store to manage hotels added to trips
export const tripHotels = writable([]);

// Add hotel to a trip
export async function addHotelToTrip(tripId, hotel) {
    try {
        const currentToken = get(token);
        if (!currentToken) {
            throw new Error('No authentication token available');
        }

        const response = await fetch(`/api/trips/${tripId}/hotels`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${currentToken}`,
            },
            body: JSON.stringify(hotel),
            credentials: 'include'
        });

        if (response.ok) {
            const newHotel = await response.json();
            tripHotels.update(hotels => [...hotels, newHotel]);
        } else {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Failed to add hotel to trip');
        }
    } catch (error) {
        console.error('Error adding hotel:', error);
    }
}

// Remove hotel from a trip
export async function removeHotelFromTrip(tripId, hotelId) {
    try {
        const currentToken = get(token);
        if (!currentToken) {
            throw new Error('No authentication token available');
        }

        const response = await fetch(`/api/trips/${tripId}/hotels/${hotelId}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${currentToken}`,
            },
            credentials: 'include'
        });

        if (response.ok) {
            tripHotels.update(hotels => hotels.filter(hotel => hotel.id !== hotelId));
        } else {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Failed to remove hotel from trip');
        }
    } catch (error) {
        console.error('Error removing hotel:', error);
    }
}

// Load hotels for a trip
export async function loadHotelsForTrip(tripId) {
    try {
        const currentToken = get(token);
        if (!currentToken) {
            tripHotels.set([]);
            return;
        }

        const response = await fetch(`/api/trips/${tripId}/hotels`, {
            headers: {
                'Authorization': `Bearer ${currentToken}`
            },
            credentials: 'include'
        });

        if (response.ok) {
            const data = await response.json();
            tripHotels.set(data);
        } else {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Failed to load hotels');
        }
    } catch (error) {
        console.error('Error loading hotels:', error);
        tripHotels.set([]); // Set empty array on error
    }
}
