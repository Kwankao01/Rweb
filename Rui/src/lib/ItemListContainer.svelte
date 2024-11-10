<script>
    import { goto } from '$app/navigation';
    import SearchBar from '$lib/SearchBar.svelte';
    import CityFilter from '$lib/CityFilter.svelte';
    import ItemCard from '$lib/ItemCard.svelte';
  
    export let items = [];
    export let cities = [];
    export let top = "";
    export let itemRoute = "/hotel";
    export let filterType = 'city';
    export let selectedType = "";
    export let selectedCity = "";
    export let pageType = "hotel"; 
    
    let searchTerm = "";

    $: selectTitle = () => {
        if (pageType === 'hotel') {
            return 'Select a hotel';
        } else if (pageType === 'restaurant') {
            return 'Select a restaurant';
        } else if (pageType === 'landmark') {
            return 'Select a landmark';
        } else if (pageType === 'favorite') {
            return 'Your Favorites';
        } else {
            return 'Select an item';
        }
    }
  
    function FilterSelect(filter) {
        if (pageType === 'favorite') {
            selectedType = filter?.toString() || "";
        } else {
            selectedCity = filter?.toString() || "";
        }
    }

    $: filteredItems = items.filter(item => {
        if (!item || typeof item !== 'object') return false;
        
        const matchesSearch = item.title?.toLowerCase().includes(searchTerm.toLowerCase());
        let matchesFilter;
        
        if (pageType === 'favorite') {
            matchesFilter = selectedType ? item.type === selectedType : true;
        } else {
            matchesFilter = selectedCity ? item[filterType] === selectedCity : true;
        }

        return matchesSearch && matchesFilter;
    });
  
    function Search(value) {
        searchTerm = value?.toString() || "";
    }
  
    function SelectItem(slug) {
        if (slug) {
            goto(`${itemRoute}/${slug}`);
        }
    }
</script>

<div class="container">
    {#if top}
        <div class="header">
            <h1>{top}</h1>
        </div>
    {/if}

    {#if pageType !== 'favorite'}
        <div class="guarantees">
            <span><i class="fas fa-money-bill-wave"></i> Price Match Guarantee</span> 
            <span><i class="fas fa-book-open"></i> Booking Guarantee</span> 
            <span><i class="fas fa-credit-card"></i> No Credit Card Fees</span>
        </div>
    {/if}

    <div class="search-section">
        <SearchBar 
            searchTerm={searchTerm} 
            {Search} 
        />
    </div>

    <h2 class="select-title">{selectTitle()}</h2>
    
    <div class="filter-section">
        <CityFilter
            filterOptions={cities}
            selectedFilter={pageType === 'favorite' ? selectedType : selectedCity}
            filterType={filterType}
            FilterSelect={FilterSelect}
            {pageType}
        />
    </div>
 
    <div class="item-list" role="list">
        {#if filteredItems.length === 0}
            <div class="no-results">
                <p>No items found matching your criteria</p>
            </div>
        {:else}
            {#each filteredItems as item (item.slug)}
                <div>
                    <ItemCard {item} {SelectItem} />
                </div>
            {/each}
        {/if}
    </div>
</div>

<style>
    .container {
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }

    .header {
        margin: 40px auto; 
        text-align: center;
        max-width: 800px; 
    }

    .header h1 {
        font-size: 46px;
        font-weight: bold;
        color: #333;
        margin: 0;
        text-align: center;
    }

    .search-section {
        margin: 30px auto;
        max-width: 3000px;
    }

    .guarantees {
        text-align: center;
        margin-top: 30px;
        margin-bottom: 30px;
        font-size: 22px;
    }

    .guarantees span {
        margin: 0 20px;
        color: #333;
    }

    .guarantees i {
        margin-right: 8px;
        color: #26796c;
    }

    .select-title {
        font-size: 1.8rem;
        color: #333;
        margin: 30px 0 20px 0;
        font-weight: bold; 
    }

    .filter-section {
        margin: 20px 0;
    }

    .item-list {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 20px;
        margin: 20px 0;
    }

    .no-results {
        grid-column: 1 / -1;
        text-align: center;
        padding: 40px;
        color: #666;
        font-size: 1.1rem;
    }

    @media (max-width: 768px) {
        .header h1 {
            font-size: 32px;
        }

        .guarantees {
            font-size: 18px;
        }

        .guarantees span {
            display: block;
            margin: 10px 0;
        }
    }

    @media (max-width: 480px) {
        .container {
            padding: 0 10px;
        }

        .header h1 {
            font-size: 28px;
        }
    }
</style>