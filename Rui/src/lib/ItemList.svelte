<script lang="ts">
    import { goto } from '$app/navigation';

    export let title: string;
    export let searchPlaceholder: string;
    export let items: { 
        id: number; 
        name: string; 
        image: string; 
        rating: number; 
        reviews: number; 
        price: number; 
        cancellation: string; 
        city: string; 
    }[] = [];
    export let cities: string[] = [];
    export let itemRoute: string = "/item";
    export let selectedCity: string;
    export let onSelectItem: (id: number) => void = (id) => goto(`${itemRoute}/${id}`);

    let searchTerm = "";
    let favoriteItems = new Set<number>();

    function toggleFavorite(id: number, event: Event) {
        event.stopPropagation();
        if (favoriteItems.has(id)) {
            favoriteItems.delete(id);
        } else {
            favoriteItems.add(id);
        }
        favoriteItems = favoriteItems;
    }

    function handleSearch(event: Event) {
        const target = event.target as HTMLInputElement;
        searchTerm = target.value;
    }

    $: filteredItems = items.filter(item => {
        const matchesSearch = item.name.toLowerCase().includes(searchTerm.toLowerCase());
        const matchesCity = !selectedCity || selectedCity === item.city;
        return matchesSearch && matchesCity;
    });
</script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">

<div style="text-align: center; margin-top: 20px">
    <h1 style="font-size: 36px; font-weight: bold; color: #26796c;">{title}</h1>
</div>

<div class="search-container">
    <input 
        type="text" 
        class="search-input" 
        placeholder={searchPlaceholder}
        value={searchTerm}
        on:input={handleSearch}
    />
</div>

<div class="featured-items">
    <div class="guarantees">
        <span><i class="fas fa-money-bill-wave"></i> Price Match Guarantee</span> 
        <span><i class="fas fa-book-open"></i> Booking Guarantee</span> 
        <span><i class="fas fa-bed"></i> No Credit Card Fees</span> 
    </div>

    {#if cities.length > 0}
        <div class="city-filters">
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

<section class="item-selection">
    <div class="item-list">
        {#each filteredItems as item}
            <div 
                role="button" 
                tabindex="0" 
                on:click={() => onSelectItem(item.id)} 
                on:keydown={(e) => (e.key === 'Enter' || e.key === ' ') && onSelectItem(item.id)} 
                class="item-card"
            >
                <button
                    type="button"
                    class="heart-button"
                    aria-label={favoriteItems.has(item.id) ? "Remove from favorites" : "Add to favorites"}
                    on:click={(e) => toggleFavorite(item.id, e)}
                >
                    <i 
                        class="fas fa-heart" 
                        class:favorite={favoriteItems.has(item.id)}
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
        margin: 20px auto;
        padding: 20px;
        text-align: center;
    }

    .guarantees {
        display: flex;
        gap: 15px;
        font-size: 16px;
        color: #333;
        margin-bottom: 10px;
        justify-content: center;
    }

    .city-filters {
        display: flex;
        gap: 10px;
        justify-content: center;
        margin-top: 20px;
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
