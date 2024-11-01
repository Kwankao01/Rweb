<script lang="ts">
    import { goto } from '$app/navigation'; // นำเข้า goto สำหรับการนำทาง

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
            location: "Chiang Rai"
        },
        {
            id: 2,
            name: "Hi Chiangrai Hotel",
            image: "Hi Chiangrai Hotel.jpg",
            rating: 4.6,
            reviews: 91,
            price: 1243,
            cancellation: "Free cancellation",
            location: "Chiang Rai"
        },
        {
            id: 3,
            name: "Phowadol Resort and Spa",
            image: "Phowadol Resort and Spa.jpg",
            rating: 3.6,
            reviews: 28,
            price: 903,
            cancellation: "Free cancellation",
            location: "Chiang Rai"
        }
       
    ];
    function handleSelect(hotelId: number) {
        goto(`/hotel/${hotelId}`); // นำไปยังหน้าที่พักที่เลือก
    }
</script>

<div style="text-align: center; margin-top: 20px">
    <h1 style="font-size: 46px; font-weight: bold;">Stay somewhere great</h1>
</div>

<div class="search-container">
    <input type="text" class="search-input" placeholder="Hotel or destination...">
    <button class="search-button"><i class="fas fa-search"></i></button>
</div>

<p style="text-align: center; font-size: 24px; margin-top: 20px;">Hotel List</p>

<section class="hotel-selection">
    <div class="hotel-list">
        {#each hotels as hotel}
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
                    <p class="price">เริ่มต้น ฿ {hotel.price.toLocaleString()}</p>
                    <p>{hotel.location}</p>
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