export async function load({ fetch }) {
    try {
        const restaurantResponse = await fetch('/api/restaurants/');
        const restaurants = await restaurantResponse.json();
        
        const cities = [...new Set(restaurants.map(restaurant => restaurant.city))].sort();
        
        return {
            restaurants,
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