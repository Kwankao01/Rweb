<script>
    import ItemList from "$lib/ItemList.svelte";

    let cities = ["Chiang Rai", "Chiang Mai", "Phuket", "Chonburi", "Hatyai"];
    let selectedCity = "Chiang Rai"; // Default selected city

    let hotels = [
        {
            id: 1,
            name: "The Riverie by Katathani",
            image: "The Riverie by Katathani.jpg",
            rating: 4.5,
            reviews: 125,
            price: 3795,
            cancellation: "Free cancellation",
            city: "Chiang Rai"
        },
        {
            id: 2,
            name: "Hi Chiangrai Hotel",
            image: "Hi Chiangrai Hotel.jpg",
            rating: 4.6,
            reviews: 91,
            price: 1243,
            cancellation: "Free cancellation",
            city: "Chiang Rai"
        },
        {
            id: 3,
            name: "Phowadol Resort and Spa",
            image: "Phowadol Resort and Spa.jpg",
            rating: 3.6,
            reviews: 28,
            price: 903,
            cancellation: "Free cancellation",
            city: "Chiang Rai"
        },
        {
            id: 4,
            name: "Lotus Pang Suan Kaew Hotel",
            image: "https://ak-d.tripcdn.com/images/20010d0000006tw544E6B_W_1280_853_R5.webp?proc=watermark/image_trip1,l_ne,x_16,y_16,w_67,h_16;digimark/t_image,logo_tripbinary;ignoredefaultwm,1A8F",
            rating: 4.0,
            reviews: 169,
            price: 1061,
            cancellation: "",
            city: "Chiang Mai"
        },
        {
            id: 5,
            name: "Le Ville Lanna Chiang Mai Gate Old Town Hotel",
            image: "https://ak-d.tripcdn.com/images/1mc3j12000dh5o1ii4EDE_R_600_400_R5.webp",
            rating: 4.5,
            reviews: 43,
            price: 3144,
            cancellation: "",
            city: "Chiang Mai"
        },
        {
            id: 6,
            name: "B2 Resort Boutique & Budget Hotel",
            image: "https://ak-d.tripcdn.com/images/1mc6q12000awv7obz43AB_R_600_400_R5.webp",
            rating: 2.8,
            reviews: 54,
            price: 589,
            cancellation: "Free cancellation",
            city: "Chiang Mai"
        },
        {
            id: 7,
            name: "Wyndham Royal Lee Phuket",
            image: "https://ak-d.tripcdn.com/images/20010u000000jiurfB993_W_1280_853_R5.webp?proc=watermark/image_trip1,l_ne,x_16,y_16,w_67,h_16;digimark/t_image,logo_tripbinary;ignoredefaultwm,1A8F",
            rating: 4.9,
            reviews: 342,
            price: 2400,
            cancellation: "",
            city: "Phuket"
        },
        {
            id: 8,
            name: "Meir Jarr",
            image: "https://ak-d.tripcdn.com/images/1mc4a12000bivju8yCB89_W_1280_853_R5.webp?proc=watermark/image_trip1,l_ne,x_16,y_16,w_67,h_16;digimark/t_image,logo_tripbinary;ignoredefaultwm,1A8F",
            rating: 4.1,
            reviews: 107,
            price: 1073,
            cancellation: "Free cancellation",
            city: "Phuket"
        },
        {
            id: 9,
            name: "Bangsaen Heritage Hotel",
            image: "https://ak-d.tripcdn.com/images/220j0v000000k1hcyA834_Z_320_220_R5_D.webp",
            rating: 4.5,
            reviews: 288,
            price: 1966,
            cancellation: "Free cancellation",
            city: "Chonburi"
        },
        {
            id: 10,
            name: "Golden Crown Grand Hotel",
            image: "https://ak-d.tripcdn.com/images/0224d12000cga8844AA01_W_1280_853_R5.webp?proc=watermark/image_trip1,l_ne,x_16,y_16,w_67,h_16;digimark/t_image,logo_tripbinary;ignoredefaultwm,1A8F",
            rating: 3.2,
            reviews: 259,
            price: 1837,
            cancellation: "Free cancellation",
            city: "Hatyai"
        }
       
    ];

</script>

<ItemList
    top="Stay somewhere great"
    searchPlaceholder="Hotel or destination..."
    title="Featured Hotels"
    items={hotels}
    cities={cities}
    selectedCity={selectedCity}
    itemRoute="/hotel"
/>