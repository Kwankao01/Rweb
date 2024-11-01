<script lang="ts">
    import { goto } from '$app/navigation';

    let restaurants = [
        {
            id: 1,
            name: "Sushi Shin",
            image: "sushi.jpg",
            rating: 4.8,
            reviews: 112,
            price: 1200,
            location: "Bangkok",
            cuisine: "Japanese"
        },
        {
            id: 2,
            name: "Bistro by the Park",
            image: "mexican.jpg",
            rating: 4.5,
            reviews: 86,
            price: 800,
            location: "Chiang Mai",
            cuisine: "Mexican"
        },
        {
            id: 3,
            name: "Nong Rim Nam",
            image: "thai.jpg",
            rating: 4.7,
            reviews: 135,
            price: 500,
            location: "Bangkok",
            cuisine: "Thai"
        },
        {
            id: 4,
            name: "Le Du",
            image: "italian.jpg",
            rating: 4.9,
            reviews: 155,
            price: 2000,
            location: "Bangkok",
            cuisine: "Italian"
        },
        {
            id: 5,
            name: "Burger Joint",
            image: "burger.jpg",
            rating: 4.6,
            reviews: 98,
            price: 1500,
            location: "Chiang Mai",
            cuisine: "International"
        }
    ];

    function handleSelect(restaurantId: number) {
        goto(`/restaurant/${restaurantId}`);
    }
</script>

<div style="text-align: center; margin-top: 20px">
    <h1 style="font-size: 46px; font-weight: bold;">Discover Delicious Places</h1>
</div>

<div class="search-container">
    <input type="text" class="search-input" placeholder="Restaurant or cuisine...">
    <button class="search-button"><i class="fas fa-search"></i></button>
</div>

<p style="text-align: center; font-size: 24px; margin-top: 20px;">Restaurant List</p>

<section class="restaurant-selection">
    <div class="restaurant-list">
        {#each restaurants as restaurant}
            <div class="restaurant-card" on:click={() => handleSelect(restaurant.id)}>
                <img src={restaurant.image} alt={restaurant.name} class="restaurant-image" />
                <div class="restaurant-info">
                    <h3>{restaurant.name}</h3>
                    <div class="rating">
                        {#each Array(5) as _, index}
                            <i class={`fas fa-star ${index < Math.floor(restaurant.rating) ? 'filled' : ''}`}></i>
                        {/each}
                        <span>({restaurant.reviews} reviews)</span>
                    </div>
                    <p class="cuisine">{restaurant.cuisine}</p>
                    <p class="price">เริ่มต้น ฿ {restaurant.price.toLocaleString()}</p>
                    <p>{restaurant.location}</p>
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

    .restaurant-selection {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    .restaurant-list {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
    }

    .restaurant-card {
        display: flex;
        flex-direction: column;
        padding: 15px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        transition: transform 0.2s;
    }

    .restaurant-card:hover {
        transform: scale(1.02);
    }

    .restaurant-image {
        width: 100%;
        height: 150px;
        border-radius: 8px;
        object-fit: cover;
        margin-bottom: 10px;
    }

    .restaurant-info h3 {
        font-size: 1.5rem;
        color: #26796c;
        margin: 0;
    }

    .restaurant-info p {
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
        color: #ffcc00;
    }

    .cuisine {
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

        .restaurant-list {
            grid-template-columns: 1fr;
        }
    }

    @media (min-width: 769px) and (max-width: 1024px) {
        .restaurant-list {
            grid-template-columns: repeat(2, 1fr);
        }
    }
</style>
