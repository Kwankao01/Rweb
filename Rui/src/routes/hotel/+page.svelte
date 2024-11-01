<script lang="ts">
    import { goto } from '$app/navigation'; // นำเข้า goto สำหรับการนำทาง

    let cities = ["Chiang Rai", "Chiang Mai", "Phuket", "Chonburi", "Hatyai"];
    let selectedCity = "Chiang Rai"; // Default selected city

    // รายการที่พักตัวอย่าง
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
            cancellation: "-",
            city: "Chiang Mai"
        },
        {
            id: 5,
            name: "Le Ville Lanna Chiang Mai Gate Old Town Hotel",
            image: "https://ak-d.tripcdn.com/images/1mc3j12000dh5o1ii4EDE_R_600_400_R5.webp",
            rating: 4.5,
            reviews: 43,
            price: 3144,
            cancellation: "-",
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
            cancellation: "-",
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

    function handleSelect(hotelId: number) {
        goto(`/hotel/${hotelId}`); // นำไปยังหน้าที่พักที่เลือก
    }
    function selectCity(city: string) {
        selectedCity = city;
    }
    
</script>

<div style="text-align: center; margin-top: 20px">
    <h1 style="font-size: 46px; font-weight: bold;">Stay somewhere great</h1>
</div>

<div class="search-container">
    <input type="text" class="search-input" placeholder="Hotel or destination...">
    <button class="search-button"><i class="fas fa-search"></i></button>
</div>

<div class="featured-hotels">
    <h2>Featured Hotels</h2>
    <div class="guarantees">
        <span>✅ We Price Match</span>
        <span>📑 Hotel Booking Guarantee</span>
        <span>🚗 Hotel Stay Guarantee</span>
    </div>

    <!-- City Filters -->
    <div class="city-filters">
        {#each cities as city}
            <button
                class:selected={selectedCity === city}
                on:click={() => selectCity(city)}
            >
                {city}
            </button>
        {/each}
    </div>
</div>

<section class="hotel-selection">
    <div class="hotel-list">
        {#each hotels.filter(hotel => hotel.city === selectedCity) as hotel}
            <div class="hotel-card" on:click={() => handleSelect(hotel.id)}>
                <img src={hotel.image} alt={hotel.name} class="hotel-image" />
                <div class="hotel-info">
                    <h3>{hotel.name}</h3>
                    <div class="rating">
                        {#each Array(5) as _, index}
                            <i class={`fas fa-star ${index < Math.floor(hotel.rating) ? 'filled' : ''}`}></i>
                        {/each}
                        <span>({hotel.reviews} reviews)</span>
                    </div>
                    <p class="cancellation">{hotel.cancellation}</p>
                    <p class="price">From ฿ {hotel.price.toLocaleString()}</p>
                    <p>{hotel.city}</p>
                </div>
            </div>
        {/each}
    </div>
</section>



<style>
    /* Search bar styling */
    .search-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }

    .search-input {
        padding: 10px 20px;                  
        border: 1px solid #ccc;
        border-radius: 30px;                 
        font-size: 18px;                     
        width: 800px;                        
        max-width: 100%;                     
        transition: width 0.3s ease;         
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
    }

    .search-button {
        margin-left: -40px;                  
        background: none;
        border: none;
        cursor: pointer;
        color: #26796c;
        font-size: 18px;
    }

    .featured-hotels {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    h2 {
        font-size: 30px;
        font-weight: bold;
        color: #003580;
    }

    .guarantees {
        display: flex;
        gap: 20px;
        font-size: 18px;
        color: #333;
        margin-bottom: 10px;
    }

    /* City filter buttons */
    .city-filters {
        display: flex;
        gap: 10px;
        margin: 20px 0;
    }

    .city-filters button {
        padding: 10px 20px;
        border: none;
        border-radius: 20px;
        background-color: #f1f1f1;
        color: #333;
        cursor: pointer;
        font-size: 18px;
        font-weight: bold;
    }

    .city-filters button.selected {
        background-color: #003580;
        color: white;
    }

    .hotel-selection {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    .hotel-list {
        display: grid;
        grid-template-columns: repeat(3, 1fr); /* 3 คอลัมน์ */
        gap: 15px;
    }

    .hotel-card {
        display: flex;
        flex-direction: column;
        padding: 15px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        transition: transform 0.2s;
    }

    .hotel-card:hover {
        transform: scale(1.02);
    }

    .hotel-image {
        width: 100%;
        height: 120px;
        border-radius: 8px;
        object-fit: cover;
        margin-bottom: 10px;
    }

    .hotel-info h3 {
        font-size: 1.5rem;
        color: #26796c;
        margin: 0;
    }

    .hotel-info p {
        color: #555;
        margin: 5px 0;
    }

    .rating {
        display: flex;
        align-items: center;
        color: #26796c;
        margin-bottom: 5px;
    }

    .rating .fa-star {
        color: #ccc;
        margin-right: 3px;
    }

    .rating .fa-star.filled {
        color: #ffcc00; /* สีดาวที่เต็ม */
    }

    .cancellation {
        font-size: 14px;
        color: #26796c;
    }

    .price {
        font-size: 1.2em;
        font-weight: bold;
        color: #26796c;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .search-input {
            width: 90%;                    
        }

        .rental-list {
            grid-template-columns: 1fr; /* 1 คอลัมน์บนหน้าจอเล็ก */
        }
    }
</style>