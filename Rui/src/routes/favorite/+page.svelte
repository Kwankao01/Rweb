<script>
    import { favorites } from '$lib/favoritesStore.js';
    import ItemListContainer from '$lib/ItemListContainer.svelte'; 
    
    const types = ['Restaurant', 'Hotel', 'Landmark'];
    let filteredItems = [];

    $: filteredItems = [...$favorites];
</script>

<ItemListContainer 
    items={filteredItems}  
    cities={types}        
    top="Your Favorites"
    itemRoute="/favorite"
    filterType="type"     
    pageType="favorite"
    selectedType=""       
/>