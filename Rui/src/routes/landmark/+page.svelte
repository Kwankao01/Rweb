<script>
    import ItemList from '$lib/ItemList.svelte';

    let cities = ["Ayutthaya", "Bangkok", "Chiang Mai"];
    let selectedCity = "Bangkok";

    let landmarks = [
        {
            id: 1,
            name: "Wat Mahathat",
            image: "https://dmc.tatdataapi.io/assets/b2fed746-7567-43e9-8ef1-d6419a1f2b37.jpeg",
            rating: 4.8,
            reviews: 2000,
            price: 50, // Free entry or use as placeholder for no price
            cancellation: "Free cancellation",
            city: "Ayutthaya"
        },
        {
            id: 2,
            name: "Jungle Coaster and other activities at Pongyang Adventure Park (Single attraction)",
            image: "https://static.ticket2attraction.com/gallery/14093126-a995-4a1a-8267-b7dc07532d71/41bdbb46-14e2-407d-a488-95e6026e429f-1200.webp",
            rating: 4.9,
            reviews: 15,
            price: 300,
            cancellation: "Free cancellation",
            city: "Chiang Mai"
        },
        {
            id: 3,
            name: "Wat Arun Ratchawararam Ratchawaramahawihan",
            image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpCcHTHgvheu4aFE0JcbWhfIsFrzNwmA4P_g&s",
            rating: 4.6,
            reviews: 10,
            price: 0,
            cancellation: "Free cancellation",
            city: "Bangkok",
        }
    ];
        
</script>

<ItemList
    title="Must-Visit Landmarks"
    searchPlaceholder="Landmark or destination..."
    items={landmarks}
    cities={cities}
    selectedCity={selectedCity}
    itemRoute="/landmark"
/>
