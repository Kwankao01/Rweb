<div style="text-align: center; margin-top: 20px">
    <h1 style="font-size: 46px; font-weight: bold;">Discover Landmarks</h1>
</div>

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

    .button {
        position: absolute;
        top: 160px;
        left: 30%;
        transform: translateX(-50%);
        padding: 15px 30px;
        background-color: #ffffff;
        color: #4c4c4c;
        text-decoration: none;
        border-radius: 30px;
        font-size: 22px;
        transition: background-color 0.3s;
        z-index: 0;
    }

    .button:hover {
        background-color: #d0d0d0;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .search-input {
            width: 90%;
        }

        .button {
            top: 140px;
            font-size: 18px;
            padding: 10px 25px;
        }
    }

    /* Landmark selection styling */
    .landmark-selection {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    h2 {
        font-size: 1.8rem;
        color: #26796c;
        margin-bottom: 20px;
        text-align: center;
    }

    .landmark-list {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .landmark-card {
        display: flex;
        align-items: center;
        padding: 15px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        transition: transform 0.2s;
    }

    .landmark-card:hover {
        transform: scale(1.02);
    }

    .landmark-image {
        width: 120px;
        height: 90px;
        border-radius: 8px;
        object-fit: cover;
        margin-right: 15px;
    }

    .landmark-info h3 {
        font-size: 1.5rem;
        color: #26796c;
        margin: 0;
    }

    .landmark-info p {
        color: #555;
        margin: 5px 0;
    }
</style>

<div class="search-container">
    <input type="text" class="search-input" placeholder="Search for a landmark...">
    <button class="search-button"><i class="fas fa-search"></i></button>
</div>
<p>Landmark List</p>

<script lang="ts">
    import { goto } from '$app/navigation';

    // รายการแลนมาร์กตัวอย่าง
    let landmarks = [
        {
            id: 1,
            name: "Khao Kheow Open Zoo",
            image: "https://img.salehere.co.th/p/1200x0/2022/10/18/0gwvo4aoquyw.jpg",
            rating: 4.9,
            reviews: 20,
            location: "Bang Phra Subdistrict, Si Racha District, Chonburi Province",
        },
        {
            id: 2,
            name: "Jungle Coaster and other activities at Pongyang Adventure Park (Single attraction)",
            image: "https://static.ticket2attraction.com/gallery/14093126-a995-4a1a-8267-b7dc07532d71/41bdbb46-14e2-407d-a488-95e6026e429f-1200.webp",
            rating: 4.9,
            reviews: 15,
            location: "Mae Rim District, Chiang Mai.",
        },
        {
            id: 3,
            name: "Wat Arun Ratchawararam Ratchawaramahawihan",
            image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpCcHTHgvheu4aFE0JcbWhfIsFrzNwmA4P_g&s",
            rating: 4.6,
            reviews: 10,
            location: "Wang Derm Road, Wat Arun Subdistrict; Bangkok Yai District Bangkok",
        }
    ];

    function handleSelect(landmarkId: number) {
        goto(`/landmark/${landmarkId}`);
    }
</script>

<section class="landmark-selection">
    <h2>Select a Landmark</h2>
    <div class="landmark-list">
        {#each landmarks as landmark}
            <div class="landmark-card" on:click={() => handleSelect(landmark.id)}>
                <img src={landmark.image} alt={landmark.name} class="landmark-image" />
                <div class="landmark-info">
                    <h3>{landmark.name}</h3>
                    <p>Rating: {landmark.rating} ({landmark.reviews} reviews)</p>
                    <p>{landmark.location}</p>
                </div>
            </div>
        {/each}
    </div>
</section>
