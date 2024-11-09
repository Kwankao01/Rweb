<script>
    import { favorites } from '$lib/favoritesStore.js';
    import ItemListContainer from '$lib/ItemListContainer.svelte'; 
    
    const types = ['Restaurant', 'Hotel', 'Landmark'];
    let filteredItems = [];

    $: {
        filteredItems = $favorites.map(item => ({
            ...item,
            type: item.type.charAt(0).toUpperCase() + item.type.slice(1) 
        }));
        console.log('Filtered Items:', filteredItems);
    }
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