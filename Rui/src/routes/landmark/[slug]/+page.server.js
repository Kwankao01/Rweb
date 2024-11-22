export async function load({ params, fetch }) {
    try {
        const response = await fetch(`/api/landmarks/${params.slug}`);
        const landmark = await response.json();

        if (!landmark) {
            return {
                status: 404,
                error: new Error('landmark not found')
            };
        }

        return {
            landmark
        };
    } catch (error) {
        console.error('Error loading restaurant data:', error);
        return {
            status: 500,
            error: new Error('Internal Server Error')
        };
    }
}