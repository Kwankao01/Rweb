// src/routes/trip/[id]/+page.server.js
import { error } from '@sveltejs/kit';

export async function load({ params, fetch, locals }) {
    const tripId = params.id;

    try {
        // Get token (adjust based on your auth setup)
        const token = localStorage.getItem('token'); // or however you store your token

        // Fetch trip details
        const response = await fetch(`/api/trips/${tripId}`, {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw error(response.status, 'Failed to load trip data');
        }

        const tripData = await response.json();
        
        // Return structured data with defaults
        return {
            trip: {
                id: tripData.id || null,
                name: tripData.name || '',
                destination: tripData.destination || '',
                start: tripData.start || null,
                end: tripData.end || null,
                duration: tripData.duration || 0,
                countdown: tripData.countdown || 0,
                hotels: tripData.hotels || [],
                group_id: tripData.group_id || null
            }
        };

    } catch (err) {
        console.error("Error loading trip:", err);
        throw error(500, 'Failed to load trip data');
    }
}