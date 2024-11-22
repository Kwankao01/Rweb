export async function load({ fetch }) {
    try {
        const restaurantResponse = await fetch('/api/landmarks/');
        const landmarks = await restaurantResponse.json();
        
        const cities = [...new Set(landmarks.map(landmark => landmark.city))].sort();
        
        return {
            landmarks,
            cities
        };
    } catch (error) {
        console.error('Error loading restaurant data:', error);
        return {
            landmarks: [],
            cities: []
        };
    }
}