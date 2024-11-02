<script lang="js">
    import { goto } from '$app/navigation';

    export let top;
    export let title;
    export let items = []; 
    export let cities = []; 
    export let itemRoute = "/item"; 
    export let selectedCity;

    let searchTerm = "";
    let favoriteItems = new Set(); 

    export let onSelectItem = (slug) => goto(`${itemRoute}/${slug}`);

    // Toggle favorite status for an item
    function toggleFavorite(slug, event) {
        event.stopPropagation();
        if (favoriteItems.has(slug)) {
            favoriteItems.delete(slug);
        } else {
            favoriteItems.add(slug);
        }
        favoriteItems = favoriteItems; // Trigger reactivity
    }

    // Handle search input changes
    function handleSearch(event) {
        searchTerm = event.target.value;
    }

    // Filter items based on search term and selected city
    $: filteredItems = items.filter(item => {
        const matchesSearch = item.name.toLowerCase().includes(searchTerm.toLowerCase());
        const matchesCity = !selectedCity || selectedCity === item.city;
        return matchesSearch && matchesCity;
    });
</script>

<div style="margin-top: 20px; text-align: center;">
    <h1 style="font-size: 46px; font-weight: bold;">{top}</h1>
</div>

<div class="search-container">
    <input 
        type="text" 
        class="search-input" 
        placeholder="Search..."
        value={searchTerm}
        on:input={handleSearch}
    />
</div>

<div class="guarantees" style="text-align: center; margin-top: 30px; font-size: 22px">
    <span><i class="fas fa-money-bill-wave"></i> Price Match Guarantee</span> 
    <span><i class="fas fa-book-open"></i> Booking Guarantee</span> 
    <span><i class="fas fa-credit-card"></i> No Credit Card Fees</span> 
</div>

<div style="margin-top: 20px; padding-left: 30px;">
    <h1 style="font-size: 30px; font-weight: 600; color: black;">{title}</h1>
</div>

<div class="featured-items">
    {#if cities.length > 0}
        <div class="city-filters" style="margin-top: 5px; padding-left: 5px;">
            <button
                class:selected={!selectedCity}
                on:click={() => selectedCity = ""}
            >
                All Cities
            </button>
            {#each cities as city}
                <button
                    class:selected={selectedCity === city}
                    on:click={() => selectedCity = city}
                >
                    {city}
                </button>
            {/each}
        </div>
    {/if}
</div>

<section class="item-selection" style="margin-top: 5px">
    <div class="item-list">
        {#each filteredItems as item}
            <div 
                role="button" 
                tabindex="0" 
                on:click={() => onSelectItem(item.slug)}
                on:keydown={(e) => (e.key === 'Enter' || e.key === ' ') && onSelectItem(item.slug)} 
                class="item-card"
            >
                <button
                    type="button"
                    class="heart-button"
                    aria-label={favoriteItems.has(item.slug) ? "Remove from favorites" : "Add to favorites"}
                    on:click={(e) => toggleFavorite(item.slug, e)}
                >
                    <i 
                        class="fas fa-heart" 
                        class:favorite={favoriteItems.has(item.slug)}
                    ></i>
                </button>
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
    .search-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .search-input {
        padding: 10px 20px;
        border: 1px solid #ccc;
        border-radius: 30px;
        font-size: 18px;
        width: 60%;
        max-width: 800px;
        transition: width 0.3s ease;
    }

    .featured-items {
        max-width: 1200px;
        padding: 20px;
        text-align: left;
    }

    .guarantees {
        display: flex;
        justify-content: center;
        gap: 20px;
        text-align: center;
        margin-top: 30px;
        font-size: 22px;
    }

    .guarantees span {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .city-filters {
        display: flex;
        gap: 10px;
    }

    .city-filters button {
        padding: 8px 16px;
        border: none;
        border-radius: 20px;
        background-color: #f1f1f1;
        color: #333;
        cursor: pointer;
        font-size: 16px;
        font-weight: bold;
    }

    .city-filters button.selected {
        background-color: #26796c;
        color: white;
    }

    .item-list {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 20px;
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    .item-card {
        position: relative;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        cursor: pointer;
        transition: transform 0.2s;
    }

    .item-card:hover {
        transform: scale(1.02);
    }

    .item-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 8px 8px 0 0;
    }

    .item-info {
        padding: 15px;
        text-align: left;
    }

    .item-info h3 {
        font-size: 1.2rem;
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
    }

    .rating .fa-star {
        color: #ccc;
        margin-right: 3px;
    }

    .rating .fa-star.filled {
        color: #ffcc00;
    }

    .heart-button {
        position: absolute;
        top: 10px;
        right: 10px;
        background: rgba(255, 255, 255, 0.8);
        border: none;
        border-radius: 50%;
        padding: 8px;
        cursor: pointer;
        transition: color 0.3s;
    }

    .heart-button i {
        color: #ccc;
        font-size: 20px;
    }

    .heart-button i.favorite {
        color: #FF0000;
    }
</style>
