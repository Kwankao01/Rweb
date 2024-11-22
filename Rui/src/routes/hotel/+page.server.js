export async function load({ fetch }) {
    try {
        const hotelResponse = await fetch('/api/hotels/');
        const hotels = await hotelResponse.json();
        
        const cities = [...new Set(hotels.map(hotel => hotel.city))].sort();
        
        return {
            hotels,
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
