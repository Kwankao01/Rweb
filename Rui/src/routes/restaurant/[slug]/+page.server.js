export async function load({ params, fetch }) {
    try {
        const response = await fetch(`/api/restaurants/${params.slug}`);
        const restaurant = await response.json();

        if (!restaurant) {
            return {
                status: 404,
                error: new Error('Restaurant not found')
            };
        }

        return {
            restaurant
        };
    } catch (error) {
        console.error('Error loading restaurant data:', error);
        return {
            status: 500,
            error: new Error('Internal Server Error')
        };
    }
}