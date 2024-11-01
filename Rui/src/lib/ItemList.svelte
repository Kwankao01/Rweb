<script lang="ts">
    import { goto } from '$app/navigation';

    // Define props for flexibility and reuse
    export let title = "Items"; // Title of the section
    export let searchPlaceholder = "Search..."; // Placeholder for the search bar
    export let items = []; // List of items (hotels, restaurants, landmarks, etc.)
    export let cities = []; // List of cities for filtering
    export let itemRoute = "/item"; // Base route for navigation, customizable
    export let selectedCity = ""; // Initial selected city
    export let onSelectItem = (id) => goto(`${itemRoute}/${id}`); // Default handler for item selection

    // Function to select a city
    function selectCity(city: string) {
        selectedCity = city;
    }
</script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">

<div style="text-align: center; margin-top: 20px">
    <h1 style="font-size: 46px; font-weight: bold;">{title}</h1>
</div>

<div class="search-container">
    <input type="text" class="search-input" placeholder={searchPlaceholder} />
    <button class="search-button"><i class="fas fa-search"></i></button>
</div>

<div class="featured-items">
    <h2>{title}</h2>
    <div class="guarantees">
        <span><i class="fas fa-money-bill-wave"></i> Price Match Guarantee</span> 
        <span><i class="fas fa-book-open"></i> Booking Guarantee</span> 
        <span><i class="fas fa-bed"></i> Stay Guarantee</span> 
    </div>

    <!-- City Filters -->
    <div class="city-filters">
        {#each cities as city}
            <button
                class:selected={selectedCity === city}
                on:click={() => selectCity(city)}
            >
                {city}
            </button>
        {/each}
    </div>
</div>

<section class="item-selection">
    <div class="item-list">
        {#each items.filter(item => item.city === selectedCity) as item}
            <div class="item-card" on:click={() => onSelectItem(item.id)}>
                <img src={item.image} alt={item.name} class="item-image" />
                <div class="item-info">
                    <h3>{item.name}</h3>
                    <div class="rating">
                        {#each Array(5) as _, index}
                            <i class={`fas fa-star ${index < Math.floor(item.rating) ? 'filled' : ''}`}></i>
                        {/each}
                        <span>({item.reviews} reviews)</span>
                    </div>
                    <p class="cancellation">{item.cancellation}</p>
                    <p class="price">From ฿ {item.price.toLocaleString()}</p>
                    <p>{item.city}</p>
                </div>
            </div>
        {/each}
    </div>
</section>

<style>
    /* Search bar styling */
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

    .featured-items {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    h2 {
        font-size: 30px;
        font-weight: bold;
        color: #2b2b2b;
    }

    .guarantees {
        display: flex;
        gap: 20px;
        font-size: 18px;
        color: #333;
        margin-bottom: 10px;
    }

    /* City filter buttons */
    .city-filters {
        display: flex;
        gap: 10px;
        margin: 20px 0;
    }

    .city-filters button {
        padding: 10px 20px;
        border: none;
        border-radius: 20px;
        background-color: #f1f1f1;
        color: #333;
        cursor: pointer;
        font-size: 18px;
        font-weight: bold;
    }

    .city-filters button.selected {
        background-color: #26796c;
        color: white;
    }

    .item-selection {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    .item-list {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
    }

    .item-card {
        display: flex;
        flex-direction: column;
        padding: 15px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        transition: transform 0.2s;
    }

    .item-card:hover {
        transform: scale(1.02);
    }

    .item-image {
        width: 100%;
        height: 120px;
        border-radius: 8px;
        object-fit: cover;
        margin-bottom: 10px;
    }

    .item-info h3 {
        font-size: 1.5rem;
        color: #26796c;
        margin: 0;
    }

    .item-info p {
        color: #555;
        margin: 5px 0;
    }

    .rating {
        display: flex;
        align-items: center;
        color: #26796c;
        margin-bottom: 5px;
    }

    .rating .fa-star {
        color: #ccc;
        margin-right: 3px;
    }

    .rating .fa-star.filled {
        color: #ffcc00;
    }

    .cancellation {
        font-size: 14px;
        color: #26796c;
    }

    .price {
        font-size: 1.2em;
        font-weight: bold;
        color: #26796c;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .search-input {
            width: 90%;                    
        }

        .item-list {
            grid-template-columns: 1fr; 
        }
    }
</style>
