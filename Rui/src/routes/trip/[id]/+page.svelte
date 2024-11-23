<script>
    import { onMount } from 'svelte';
    export let data;

    // Destructure with default values
    $: ({ trip = {
        name: '',
        destination: '',
        duration: 0,
        countdown: 0,
        hotels: []
    } } = data);

    // Ensure hotels is always an array
    $: hotels = Array.isArray(trip?.hotels) ? trip.hotels : [];

    let loading = true;
    let error = null;

    onMount(() => {
        loading = false;
    });

    function handleItemAdded(event) {
        const { item } = event.detail;
        hotels = [...hotels, item];
    }

    
</script>

{#if loading}
    <div class="loading">Loading...</div>
{:else if error}
    <div class="error">{error}</div>
{:else}
    <div class="trip-details">
        <h1>{trip.name || 'Untitled Trip'}</h1>
        <p>Destination: {trip.destination || 'Not specified'}</p>
        <p>Duration: {trip.duration || 0} days</p>
        <p>Countdown: {trip.countdown || 0} days until trip</p>

        <h2>Hotels</h2>
        {#if hotels.length > 0}
            <div class="hotels-grid">
                {#each hotels as hotel}
                    <div class="hotel-card">
                        {#if hotel.image}
                            <img 
                                src={hotel.image} 
                                alt={hotel.title}
                                on:error={(e) => {
                                    e.target.src = '/images/placeholder.jpg';
                                }}
                            />
                        {/if}
                        <div class="hotel-info">
                            <h3>{hotel.title || 'Unnamed Hotel'}</h3>
                            <p>{hotel.city || 'Location not specified'}</p>
                            <p>Price: {hotel.price ? `฿${hotel.price.toLocaleString()}` : 'Price not available'}</p>
                        </div>
                    </div>
                {/each}
            </div>
        {:else}
            <p>No hotels added to this trip yet.</p>
        {/if}
    </div>
{/if}

<style>
    .loading {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 200px;
    }

    .error {
        color: red;
        padding: 1rem;
        text-align: center;
    }

    .trip-details {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    .hotels-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }

    .hotel-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        overflow: hidden;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .hotel-card img {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }

    .hotel-info {
        padding: 1rem;
    }

    .hotel-info h3 {
        margin: 0 0 0.5rem 0;
        font-size: 1.2rem;
    }

    .hotel-info p {
        margin: 0.25rem 0;
        color: #666;
    }
</style>