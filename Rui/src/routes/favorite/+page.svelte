<script>
    import { favorites } from '$lib/favoritesStore.js';
    import ItemListContainer from '$lib/ItemListContainer.svelte'; 
    
    const types = ['Restaurant', 'Hotel', 'Landmark'];
    let filteredItems = [];

    $: {
        filteredItems = $favorites.map(item => ({
            ...item,
            type: item.type || 'Undefined' 
        }));
        console.log('Filtered Items:', filteredItems);
    }

    const cities = types;
</script>

<ItemListContainer 
    items={filteredItems}  
    {cities}
    top="Your Favorites"
    itemRoute="/favorite"
    filterType="type"      
    pageType="favorite"
/>