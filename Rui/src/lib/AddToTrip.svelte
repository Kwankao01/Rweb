<script>
    import { onMount } from 'svelte';
    import { token } from '$lib/stores/auth';
    import { createEventDispatcher } from 'svelte';

    export let item;
    let trips = [];
    let selectedTrip = null;
    let showModal = false;
    let loading = false;
    let error = null;

    const dispatch = createEventDispatcher();

    onMount(async () => {
        await fetchTrips();
    });

    async function fetchTrips() {
        try {
            const response = await fetch('/api/trips/', {
                headers: {
                    'Authorization': `Bearer ${$token}`,
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                trips = await response.json();
                console.log('Fetched trips:', trips);
            } else {
                error = `Failed to fetch trips: ${response.status}`;
            }
        } catch (err) {
            error = 'Error fetching trips';
            console.error('Error fetching trips:', err);
        }
    }

    async function addToTrip() {
        if (!selectedTrip) return;

        loading = true;
        error = null;

        try {
            const response = await fetch(
                `/api/trips/${selectedTrip}/add_item?hotel_id=${item.id}`,
                {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${$token}`,
                        'Content-Type': 'application/json'
                    }
                }
            );

            if (response.ok) {
                const result = await response.json();
                showModal = false;
                dispatch('itemAdded', { 
                    tripId: selectedTrip,
                    item: item
                });
                // Refresh trips list
                await fetchTrips();
            } else {
                const errorData = await response.json();
                error = errorData.detail || 'Failed to add hotel to trip';
            }
        } catch (err) {
            error = 'Error adding hotel to trip';
            console.error('Error:', err);
        } finally {
            loading = false;
        }
    }
</script>

<button on:click={() => showModal = true} class="add-trip-btn">
    Add To Trip
</button>

{#if showModal}
    <div class="modal" on:click|self={() => showModal = false}>
        <div class="modal-content">
            <h2>Select a Trip</h2>
            
            {#if error}
                <div class="error-message">{error}</div>
            {/if}
            
            <div class="select-wrapper">
                <select bind:value={selectedTrip} class="input" disabled={loading}>
                    <option value={null}>Choose a trip...</option>
                    {#each trips as trip}
                        <option value={trip.id}>
                            {trip.name} - {trip.destination}
                        </option>
                    {/each}
                </select>
            </div>

            <div class="button-group">
                <button 
                    on:click={() => showModal = false} 
                    class="cancel-btn"
                    disabled={loading}
                >
                    Cancel
                </button>
                <button 
                    on:click={addToTrip} 
                    disabled={!selectedTrip || loading} 
                    class="button"
                >
                    {loading ? 'Adding...' : 'Add'}
                </button>
            </div>
        </div>
    </div>
{/if}


<style>
     .modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }

    .modal-content {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        max-width: 400px;
        width: 90%;
    }

    .select-wrapper {
        position: relative;
        margin: 0.75rem 0;
    }

    .input {
        width: 100%;
        padding: 0.5rem;
        border: 1px solid #dbdbdb;
        border-radius: 4px;
        font-size: 14px;
        color: #333;
        background: white;
        -webkit-appearance: none;
        appearance: none;
        background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: right 0.75rem center;
        background-size: 0.75em;
        padding-right: 2rem;
    }

    .input:focus {
        outline: none;
        border-color: #26796c;
        box-shadow: 0 0 0 2px rgba(38, 121, 108, 0.2);
    }

    .button-group {
        margin-top: 1rem;
        display: flex;
        gap: 0.75rem;
        justify-content: flex-end;
    }

    .add-trip-btn,
    .cancel-btn,
    .button {
        padding: 0.5rem 1rem;
        font-size: 14px;
        border-radius: 4px;
        cursor: pointer;
    }

    .add-trip-btn,
    .button {
        background: #26796c;
        color: white;
        border: none;
    }

    .cancel-btn {
        background: #f0f0f0;
        border: none;
    }

    .button:hover:not(:disabled) {
        background-color: #1f665b;
    }

    .button:disabled {
        background: #ccc;
        cursor: not-allowed;
    }

    h2 {
        font-size: 16px;
        color: #333;
        margin-bottom: 0.75rem;
    }

    select option {
        font-size: 14px;
        padding: 4px;
        color: #333;
    }

    .error-message {
        color: #dc2626;
        margin-bottom: 1rem;
        padding: 0.5rem;
        background-color: #fef2f2;
        border-radius: 4px;
    }
    
</style>
