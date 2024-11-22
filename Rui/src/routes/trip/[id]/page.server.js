// page.server.js
import { error } from '@sveltejs/kit';

export async function load({ params, fetch }) {
  const tripId = params.id;

  try {
    // Fetch trip details
    const tripResponse = await fetch(`/api/trips/${tripId}`);
    const trip = await tripResponse.json();

    // Fetch associated hotels
    const hotelsResponse = await fetch(`/api/trips/${tripId}/hotels`);
    const hotels = await hotelsResponse.json();

    // Fetch associated restaurants 
    const restaurantsResponse = await fetch(`/api/trips/${tripId}/restaurants`);
    const restaurants = await restaurantsResponse.json();

    // Fetch associated landmarks
    const landmarksResponse = await fetch(`/api/trips/${tripId}/landmarks`);  
    const landmarks = await landmarksResponse.json();

    return {
      trip,
      hotels,
      restaurants,
      landmarks
    };
  } catch (err) {
    throw error(500, 'Error fetching trip data');
  }
}