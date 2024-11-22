<script>
    import ItemListContainer from '$lib/ItemListContainer.svelte';
    export let data;

    $: ({ hotels, cities } = data);
    
    $: console.log('Hotel data:', hotels);
    $: console.log('Cities data:', cities);
</script>

<ItemListContainer 
    items={hotels}
    {cities}
    top="Discover Hotels"
    itemRoute="/hotel"
    filterType="city"
    pageType="hotel"
/>
