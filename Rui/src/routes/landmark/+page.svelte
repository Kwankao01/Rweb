<script>
    import ItemListContainer from '$lib/ItemListContainer.svelte';
    export let data;

    $: ({ landmarks, cities } = data);
    
    $: console.log('landmark data:', landmarks);
    $: console.log('Cities data:', cities);
</script>

<ItemListContainer 
    items={landmarks}
    {cities}
    top="Discover Landmarks"
    itemRoute="/landmark"
    filterType="city"
    pageType="landmark"
/>