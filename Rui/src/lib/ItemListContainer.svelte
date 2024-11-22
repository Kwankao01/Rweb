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
    let visibleItems = []; // รายการที่แสดงบนหน้า
    let loading = true; // สำหรับ loading spinner
    const itemsPerPage = 8; // จำนวนรายการต่อหน้า
    let currentPage = 1; // หน้าปัจจุบัน

    $: selectTitle = () => {
        if (pageType === 'hotel') return 'Select a hotel';
        if (pageType === 'restaurant') return 'Select a restaurant';
        if (pageType === 'landmark') return 'Select a landmark';
        if (pageType === 'favorite') return 'Your Favorites';
        return 'Select an item';
    };

    function FilterSelect(filter) {
        if (pageType === 'favorite') {
            selectedType = filter?.toString() || "";
        } else {
            selectedCity = filter?.toString() || "";
        }
        resetVisibleItems();
    }

    function Search(value) {
        searchTerm = value?.toString() || "";
        resetVisibleItems();
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

    // โหลดข้อมูลเริ่มต้น
    function resetVisibleItems() {
        visibleItems = [];
        currentPage = 1;
        loadMore();
    }

    function loadMore() {
        loading = true;
        const start = (currentPage - 1) * itemsPerPage;
        const end = start + itemsPerPage;

        // เพิ่มรายการใหม่ทีละชุด
        setTimeout(() => {
            visibleItems = [...visibleItems, ...filteredItems.slice(start, end)];
            currentPage++;
            loading = false;
        }, 500); // เพิ่ม delay เล็กน้อยเพื่อแสดง loading spinner
    }

    function SelectItem(slug) {
        if (slug) goto(`${itemRoute}/${slug}`);
    }

    // โหลดข้อมูลเริ่มต้นเมื่อเปิดหน้า
    resetVisibleItems();
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
        {#if visibleItems.length === 0 && !loading}
            <div class="no-results">
                <p>No items found matching your criteria</p>
            </div>
        {:else}
            {#each visibleItems as item (item.slug)}
                <div>
                    <ItemCard {item} {SelectItem} />
                </div>
            {/each}
        {/if}
    </div>

    {#if loading}
        <!-- Spinner สำหรับ loading -->
        <div class="loading-spinner" aria-label="Loading items..."></div>
    {:else if visibleItems.length < filteredItems.length}
        <!-- ปุ่มโหลดเพิ่มเติม -->
        <button class="load-more" on:click={loadMore}>Load More</button>
    {/if}
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
    .loading-spinner {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 40px auto;
        border: 4px solid #f3f3f3;
        border-top: 4px solid #26796c;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 1s linear infinite;
    }
    .load-more {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        background-color: #26796c;
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1rem;
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

    @keyframes spin {
        from {
            transform: rotate(0deg);
    }
    to {
            transform: rotate(360deg);
    }
}
    
</style>