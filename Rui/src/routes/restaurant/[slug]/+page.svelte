<script>
    import ItemCard from '../../../lib/ItemCard.svelte';
    export let data;

    const handleSelectItem = (item) => {
        // Empty since we're on detail page
    };
</script>

<div class="restaurant-container">
    {#if data.restaurant}
        <div class="restaurant-content">
            <h1>{data.restaurant.title}</h1>
            <img src={data.restaurant.image} alt={data.restaurant.title} class="restaurant-image" />
            <div class="restaurant-details">
                <div>{data.restaurant.content}</div>
                <p class="rating">Rating: {data.restaurant.rating} ({data.restaurant.reviews} reviews)</p>
                <p class="location">Location: {data.restaurant.city}</p>
                <p class="price">Price: ฿{data.restaurant.price.toLocaleString()}</p>
                {#if data.restaurant.cancellation}
                    <p class="cancellation">{data.restaurant.cancellation}</p>
                {/if}
            </div>
        </div>
    {:else}
        <p>Restaurant not found</p>
    {/if}
</div>

<style>
    .restaurant-container {
        max-width: 800px; 
        margin: 0 auto; 
        padding: 20px; 
        background-color: #f9f9f9; 
        border-radius: 8px; 
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); 
    }

    .restaurant-content {
        padding: 20px;
    }

    h1 {
        font-size: 2.5em; 
        color: #26796c; 
        text-align: center; 
        margin-bottom: 20px; 
    }

    .restaurant-image {
        width: 100%; 
        max-height: 500px; 
        object-fit: cover;
        border-radius: 8px; 
        margin-bottom: 20px; 
    }

    .restaurant-details {
        font-size: 1.2em; 
        line-height: 1.6; 
        color: #555; 
        padding: 20px;
        background: white;
        border-radius: 8px;
    }

    .rating {
        font-weight: bold; 
        color: #ff9800;
        margin: 15px 0;
    }

    .location {
        font-style: italic; 
        color: #666;
        margin: 10px 0;
    }

    .price {
        color: #26796c;
        font-weight: bold;
        font-size: 1.3em;
        margin: 15px 0;
    }

    @media (max-width: 768px) {
        .restaurant-container {
            margin: 10px;
        }
        
        h1 {
            font-size: 2em;
        }
        
        .restaurant-image {
            max-height: 400px;
        }
    }
</style>