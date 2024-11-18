<script>
    import Footer from '$lib/Footer.svelte';
    import { showPopup, popupMessage } from '$lib/favoritesStore.js';
    import { onMount } from 'svelte'; 

    onMount(() => {
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', function(e) {
                document.querySelectorAll('.nav-links a').forEach(l => l.classList.remove('active'));
                this.classList.add('active');
            });
        });
    });
</script>

<svelte:head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <title>Route Ready</title>
</svelte:head>

<div class="header">
    <div class="logo-container">
        <a href="/" class="logo-link">
            <img src="/Rlogo.png" alt="Logo" class="logo">
            <h1 class="brand-name">Route Ready</h1>
        </a>
    </div>

    <nav class="main-nav">
        <div class="dropdown">
            <button id="group">Group</button>
            <div class="dropdown-content">
                <a href="/group/group-create">Create Group</a>
                <a href="/group/group-join">Join Group</a>
                <a href="/group/group-all">My Groups</a>
            </div>
        </div>

        <div class="dropdown">
            <button id="trip">Trips</button>
            <div class="dropdown-content">
                <a href="/Trip-list">My Trip</a>
                <a href="/trip-create">Create Trip</a>
            </div>
        </div>
        
        <a href="/calendar" id="calendar">Calendar</a>
    </nav>
    
    <a href="/favorite" id="favorite" class="favorite-link">
        <i class="fas fa-heart" style="font-size: 30px;"></i>
    </a>

    <a href="/login" id="profile" class="profile-link">
        <i class="fas fa-user-circle" style="font-size: 30px;"></i>
    </a>

</div>

<nav>
    <div class="nav-links">
        <a href="/" id="all"><i class="fas fa-home"></i> Search all</a>
        <a href="/hotel" id="hotel"><i class="fas fa-hotel"></i> Hotels</a>
        <a href="/restaurant" id="restaurant"><i class="fas fa-utensils"></i> Restaurants</a>
        <a href="/landmark" id="landmark"><i class="fas fa-landmark"></i> Landmarks</a>
        <a href="/transportation" id="transportation"><i class="fas fa-plane"></i> Flights</a>
    </div>
</nav>

<slot />

{#if $showPopup}
    <div class="popup-container">
        <div class="popup-message show" role="alert">
            {$popupMessage}
        </div>
    </div>
{/if}

<div style="margin-bottom: 40px;"></div> 

<Footer />

<style>
    /* Basic reset */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .popup-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 9999;
        pointer-events: none;
    }

    .popup-message {
        padding: 15px 25px;
        border-radius: 8px;
        background-color: #26796c;
        color: white;
        opacity: 1;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        pointer-events: auto;
        animation: slideIn 0.3s ease;
    }

    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    body {
        min-width: 320px;
    }

    .header {
        display: flex;
        align-items: center;
        padding: 0.625rem 1.25rem;
        margin: 0.625rem;
    }

    .logo-container {
        display: flex;
        align-items: center;
        flex-shrink: 0;
    }

    .logo-link {
        text-decoration: none;
        color: black;
        display: flex;
        align-items: center;
    }

    .logo {
        height: 50px;
        width: auto;
        margin-right: 0.625rem;
    }

    .brand-name {
        font-size: 1.875rem;
        font-weight: bold;
        margin: 0;
    }

    .main-nav {
        color: black;
        display: flex;
        gap: 1.25rem;
        margin-left: 15rem;
        flex-grow: 1;
        justify-content: flex-start;
        align-items: center;
    }

    .nav-item {
        height: 2rem;
        display: flex;
        align-items: center;
    }

    .profile-link {
        color: black;
    }

    .favorite-link {
        margin-left: auto;
        color: black;
        text-decoration: none;
    }

    .nav-links {
        display: flex;
        justify-content: center;
        gap: 0.625rem;
        font-size: 1.25rem;
        margin-top: 0.625rem;
    }

    .nav-links a {
        display: inline-block;
        padding: 0.3125rem 0.625rem;
        margin: 0.3125rem;
        text-decoration: none;
        border-radius: 5px;
        color: #000;
        font-size: 1.25rem;
    }

    .nav-links a:hover {
        text-decoration: underline;
        background-color: #f1f1f1;
    }

    .nav-links a.active {
        text-decoration: underline;
        color: #000;
    }

    .dropdown {
        position: relative;
        height: 2rem;
        display: flex;
        align-items: center;
    }

    .dropdown > a {
        color: black;
        text-decoration: none;
        padding: 0.3125rem 0.625rem;
        height: 100%;
        display: flex;
        align-items: center;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        border-radius: 5px;
        top: 100%;
        opacity: 0;
        transition: opacity 0.2s ease-in-out;
    }

    .dropdown-content a {
        color: black;
        padding: 0.75rem 1rem;
        text-decoration: none;
        display: block;
        margin: 0;
    }

    .dropdown-content a:hover {
        background-color: #f1f1f1;
    }

    .dropdown:hover .dropdown-content {
        display: block;
        opacity: 1;
    }

    .dropdown:hover, #calendar:hover {
        background-color: #f1f1f1;
        border-radius: 20px;
    }

    #calendar {
        color: black;
        text-decoration: none;
        transition: color 0.3s;
        padding: 0.3125rem 0.625rem;
        height: 2rem;
        display: flex;
        align-items: center;
    }

    #profile {
        display: flex;
        padding: 0.3125rem;
        align-items: center;
    }

    #favorite {
        display: flex;
        padding: 0.3125rem;
        align-items: center;
    }

    #profile:hover {
        background-color: #f1f1f1;
        border-radius: 20px;
    }

    #favorite:hover {
        background-color: #f1f1f1;
        border-radius: 20px;
    }

    @media (max-width: 1024px) {
        .main-nav {
            margin-left: 2rem;
        }

        .profile-link {
            margin-left: 1rem;
        }

        .favorite-link {
            margin-left: 1rem;
        }
    }

    @media (max-width: 768px) {
        .header {
            flex-wrap: wrap;
        }

        .main-nav {
            margin-left: 0;
            margin-top: 1rem;
            order: 2;
            width: 100%;
            justify-content: center;
        }

        .profile-link {
            order: 1;
        }

        .favorite-link {
            order: 1;
        }

        .nav-links {
            flex-wrap: wrap;
        }
    }
</style>