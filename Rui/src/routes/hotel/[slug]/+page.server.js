export async function load({ params, fetch }) {
    try {
        const response = await fetch(`/api/hotels/${params.slug}`);
        const hotel = await response.json();

        if (!hotel) {
            return {
                status: 404,
                error: new Error('Hotel not found')
            };
        }

        return {
            hotel
        };
    } catch (error) {
        console.error('Error loading hotel data:', error);
        return {
            status: 500,
            error: new Error('Internal Server Error')
        };
    }
}
