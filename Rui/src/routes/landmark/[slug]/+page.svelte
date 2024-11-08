<script>
    import ItemCard from '../../../lib/ItemCard.svelte';
    export let data;

    const handleSelectItem = (item) => {
        // Empty since we're on detail page
    };
</script>

<div class="landmark-container">
    {#if data.landmark}
        <div class="landmark-content">
            <h1>{data.landmark.title}</h1>
            <img src={data.landmark.image} alt={data.landmark.title} class="landmark-image" />
            <div class="landmark-details">
                <div>{@html data.landmark.content}</div>
                <p class="rating">Rating: {data.landmark.rating} ({data.landmark.reviews} reviews)</p>
                <p class="location">Location: {data.landmark.location}</p>
                <p class="city">City: {data.landmark.city}</p>
            </div>
        </div>
    {:else}
        <p>Landmark not found</p>
    {/if}
</div>

<style>
    .landmark-container {
        max-width: 800px; 
        margin: 0 auto; 
        padding: 20px; 
        background-color: #f9f9f9; 
        border-radius: 8px; 
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); 
    }

    .landmark-content {
        padding: 20px;
    }

    h1 {
        font-size: 2.5em; 
        color: #26796c; 
        text-align: center; 
        margin-bottom: 20px; 
    }

    .landmark-image {
        width: 100%; 
        max-height: 500px; 
        object-fit: cover;
        border-radius: 8px; 
        margin-bottom: 20px; 
    }

    .landmark-details {
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

    .city {
        color: #666;
        font-style: italic;
        margin: 10px 0;
    }

    @media (max-width: 768px) {
        .landmark-container {
            margin: 10px;
        }
        
        h1 {
            font-size: 2em;
        }
        
        .landmark-image {
            max-height: 400px;
        }
    }
</style>