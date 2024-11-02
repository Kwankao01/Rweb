<script>
    import { favorites } from '$lib/favoritesStore.js';
    import ItemList from '$lib/ItemList.svelte';

    const types = ['Restaurant', 'Hotel', 'Landmark'];

    $: filteredItems = $favorites.map(item => ({
        ...item,
        type: item.type || 'Landmark' // ถ้าไม่มี type ให้เป็น Landmark
    }));

    console.log('Filtered Items:', filteredItems); // เพิ่ม debug log

    $: props = {
        top: "My Favorites",
        title: "Favorite Items",
        items: filteredItems,
        cities: types,
        itemRoute: "/",
        selectedCity: "",
        filterType: 'type'
    };
</script>

<ItemList {...props} />