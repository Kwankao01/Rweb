<script>
    import ItemList from '$lib/ItemList.svelte';

    let cities = ["Bangkok", "Chiang Mai", "Phuket"];
    let selectedCity = "Bangkok";
    
    let restaurants = [
        {
            id: 1,
            name: "Sushi Shin",
            image: "https://hello2day.com/wp-content/uploads/2019/06/sushi-shin-0.jpg",
            rating: 4.8,
            reviews: 112,
            price: 1200,
            cancellation: "",
            city: "Bangkok",
        },
        {
            id: 2,
            name: "Bistro by the Park",
            image: "https://img1.wsimg.com/isteam/ip/019a9d30-806b-4ab2-8c2d-8d2f3be68221/image-0001.JPG",
            rating: 4.5,
            reviews: 86,
            price: 800,
            cancellation: "Free cancellation",
            city: "Chiang Mai",
        },
        {
            id: 3,
            name: "JAY FAI",
            image: "https://www.prachachat.net/wp-content/uploads/2024/10/AFP__20200715__1V85JO__v1__HighRes__ThailandLifestyleFood_0-2048x1365.jpg",
            rating: 4.3,
            reviews: 135,
            price: 1000,
            cancellation: "",
            city: "Bangkok",
        },
        {
            id: 4,
            name: "Le Du",
            image: "https://ledubkk.com/assets/img/Ledu.brand.jpg",
            rating: 4.9,
            reviews: 155,
            price: 2000,
            cancellation: "Free cancellation",
            city: "Bangkok",
        },
        {
            id: 5,
            name: "Burger Joint",
            image: "https://scontent.fbkk9-3.fna.fbcdn.net/v/t39.30808-6/327178515_717730493124899_3010554239486917480_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=tZVNIIqEf6UQ7kNvgEKdxjz&_nc_zt=23&_nc_ht=scontent.fbkk9-3.fna&_nc_gid=A7gAAhEIxWUgTvu5ZGHxLRP&oh=00_AYCtWxAqsxeX6Dtn-_Llz2JDS9dXc8eoVVDpfafYB3f71w&oe=672ABB7A",
            rating: 4.6,
            reviews: 98,
            price: 1500,
            cancellation: "Free cancellation",
            city: "Chiang Mai",
        },
        {
            id: 6,
            name: "Red sauce",
            image: "https://images.rosewoodhotels.com/is/image/rwhg/redsauce-007:SQUARE-LARGE-1-1",
            rating: 4.6,
            reviews: 120,
            price: 2500,
            cancellation: "",
            city: "Phuket",
        }

    ];
    

</script>

<ItemList 
    top="Find places to eat"
    title="Top Restaurants"
    searchPlaceholder="Search for restaurants..."
    items={restaurants}
    cities={cities}
    selectedCity={selectedCity}
    itemRoute="/restaurant"
/>



