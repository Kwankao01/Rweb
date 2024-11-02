<script>
    import ItemList from '$lib/ItemList.svelte';
    export let data;

    // Transform the landmark data to match the ItemList expected format
    const items = data.summaries.map(hotel=> ({
        slug: hotel.slug,
        name: hotel.title,
        image: hotel.image,
        rating: hotel.rating,
        reviews: hotel.reviews,
        city: hotel.city,
        price: hotel.price,
        cancellation: "Free cancellation available"
    }));

    // Get unique cities from landmarks
    const cities = [...new Set(items.map(item => item.city))];

    // Create props for ItemList
    const props = {
        top: "Discover hotels",
        title: "Select a hotel",
        items: items,
        cities: cities,
        itemRoute: "/hotel",
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

    /* Hotel selection styling */
    .hotel-selection {
        max-width: 1200px;
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

    /* Grid for hotels */
    .hotel-list {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        justify-content: center;
    }

    /* Hotel card styling */
    .hotel-card {
        flex: 1 1 calc(33.33% - 20px); /* Each card takes up 1/3 of the row with some space for margin */
        max-width: 360px;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 15px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        transition: transform 0.2s;
        text-align: center;
    }

    /* Hover effect */
    .hotel-card:hover {
        transform: scale(1.02);
    }

    /* Image styling */
    .hotel-image {
        width: 100%;
        height: 180px;
        border-radius: 8px;
        object-fit: cover;
        margin-bottom: 10px;
    }

    /* Hotel info styling */
    .hotel-info h3 {
        font-size: 1.2rem;
        color: #26796c;
        margin: 0;
    }

    .hotel-info p {
        color: #555;
        margin: 5px 0;
    }
</style>