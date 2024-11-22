<script>
    import { token, userId } from "$lib/stores/auth";
    import { onMount } from "svelte";
    import { page } from "$app/stores";

    let trip = null;
    let error = null;
    let loading = true;

    async function fetchTripDetails() {
    try {
        const tripId = $page.params.id;
        console.log('Fetching trip:', tripId); // Debug log
        
        const response = await fetch(`/api/trips/${tripId}`, {
            headers: {
                "Authorization": `Bearer ${$token}`,
                "Content-Type": "application/json"
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        trip = await response.json();
        console.log('Trip data:', trip); // Debug log
    } catch (err) {
        console.error("Error fetching trip details:", err);
        error = err.message;
    } finally {
        loading = false;
    }
}

    onMount(fetchTripDetails);
</script>

{#if loading}
    <div class="loading">Loading...</div>
{:else if error}
    <div class="error">{error}</div>
{:else if trip}
    <div class="trip-detail">
        <div class="trip-header">
            <h1>{trip.name}</h1>
            <div class="trip-meta">
                <p class="destination">Destination: {trip.destination}</p>
                <p class="dates">
                    {new Date(trip.start).toLocaleDateString()} - 
                    {new Date(trip.end).toLocaleDateString()}
                </p>
                <p class="duration">Duration: {trip.duration} days</p>
                <p class="countdown">Countdown: {trip.countdown} days</p>
            </div>
        </div>
    </div>
{:else}
    <div class="error">Trip not found</div>
{/if}

<style>
    /* Container for the trip details */
    .trip-detail {
        max-width: 800px;
        margin: 2rem auto;
        padding: 1.5rem;
        background: #f9f9f9;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: 'Arial', sans-serif;
        color: #333;
        line-height: 1.6;
    }

    /* Header for trip details */
    .trip-header {
        background: #fff;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
        text-align: center;
    }

    .trip-header h1 {
        font-size: 1.8rem;
        margin: 0;
        color: #007bff;
    }

    .trip-header p {
        font-size: 1rem;
        margin: 0.5rem 0 0;
        color: #555;
    }

    /* Meta information section */
    .trip-meta {
        margin-top: 1.5rem;
        padding: 1rem;
        background: #fff;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }

    .trip-meta h2 {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: #333;
    }

    .trip-meta ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .trip-meta ul li {
        margin: 0.5rem 0;
        padding: 0.5rem;
        background: #f0f8ff;
        border-radius: 6px;
        border: 1px solid #d9edf7;
        color: #31708f;
    }

    /* Loading state */
    .loading, .error {
        text-align: center;
        padding: 2rem;
        border-radius: 8px;
        background: #fff;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }

    .loading {
        color: #007bff;
        font-size: 1.2rem;
        font-weight: bold;
    }

    /* Error state */
    .error {
        color: #d9534f;
        font-size: 1.2rem;
        font-weight: bold;
    }

    /* Mobile responsiveness */
    @media screen and (max-width: 600px) {
        .trip-detail {
            padding: 1rem;
        }

        .trip-header h1 {
            font-size: 1.5rem;
        }

        .trip-meta h2 {
            font-size: 1.2rem;
        }
    }
</style>
