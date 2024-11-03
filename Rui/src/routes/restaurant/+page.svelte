<script>
    import ItemList from '$lib/ItemList.svelte';
    export let data;

    // Transform the landmark data to match the ItemList expected format
    const items = data.summaries.map(restaurant => ({
        slug: restaurant.slug,
        name: restaurant.title,
        image: restaurant.image,
        rating: restaurant.rating,
        reviews: restaurant.reviews,
        city: restaurant.city,
        price: 0,
        cancellation: ""
    }));

    // Get unique cities from landmarks
    const cities = [...new Set(items.map(item => item.city))];

    // Create props for ItemList
    const props = {
        top: "Discover Restaurants",
        title: "Select a Restaurant",
        items: items,
        cities: cities,
        itemRoute: "/restaurant",
        selectedCity: ""
    };
</script>

<ItemList {...props} />

<style>
    :global(.item-card) {
        background-color: #ffffff;
    }

    :global(.item-info h3) {
        color: #26796c;

    }
    .search-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }

    .search-input {
        padding: 10px 20px;
        border: 1px solid #ccc;
        border-radius: 30px;
        font-size: 18px;
        width: 800px;
        max-width: 100%;
        transition: width 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .search-button {
        margin-left: -40px;
        background: none;
        border: none;
        cursor: pointer;
        color: #26796c;
        font-size: 18px;
    }

    /* Landmark selection styling */
    .restaurant-selection {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    h2 {
        font-size: 1.8rem;
        color: #26796c;
        margin-bottom: 20px;
        text-align: center;
    }

    .restaurant-list {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .restaurant-card {
        display: flex;
        align-items: center;
        padding: 15px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        transition: transform 0.2s;
    }

    .restaurant-card:hover {
        transform: scale(1.02);
    }

    .restaurant-image {
        width: 120px;
        height: 90px;
        border-radius: 8px;
        object-fit: cover;
        margin-right: 15px;
    }

    .restaurant-info h3 {
        font-size: 1.5rem;
        color: #26796c;
        margin: 0;
    }

    .restaurant-info p {
        color: #555;
        margin: 5px 0;

    }
</style>
