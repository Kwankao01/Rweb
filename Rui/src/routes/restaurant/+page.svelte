<script>
    import ItemListContainer from '$lib/ItemListContainer.svelte';
    export let data;

    $: ({ restaurants, cities } = data);
    
    $: console.log('restaurant data:', restaurants);
    $: console.log('Cities data:', cities);
</script>

<ItemListContainer 
    items={restaurants}
    {cities}
    top="Discover Restaurants"
    itemRoute="/restaurant"
    filterType="city"
    pageType="restaurant"
/>