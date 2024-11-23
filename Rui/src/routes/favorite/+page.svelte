<script>
    import { onMount } from 'svelte';
    import { favorites, loadFavorites } from '$lib/favoritesStore.js';
    import ItemListContainer from '$lib/ItemListContainer.svelte';
   
    const types = ['Restaurant', 'Hotel', 'Landmark'];
   
    onMount(() => {
        console.log('Loading favorites...');
        loadFavorites();
    });
 
    // Data is already in the correct format from the backend
    $: filteredItems = $favorites;
    $: console.log('Filtered Items:', filteredItems);
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