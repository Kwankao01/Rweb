<script>
    import { onMount } from 'svelte';
    import { token } from '$lib/stores/auth';
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();

    export let item;
    let trips = [];

    let selectedTrip = null;
    let showModal = false;
    let loading = false;
    let error = null;
    let isItemAdded = false; // To check if the item is already added to the trip

    // Fetch trips on mount
    onMount(async () => {
        await fetchTrips();
    });

    // Fetch trips from the API
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
                // Check if item is already in any trip
                trips.forEach(trip => {
                    trip.isItemAdded = trip.items?.some(tripItem => tripItem.id === item.id);
                });
                console.log('Fetched trips:', trips);
            } else {
                error = `Failed to fetch trips: ${response.status}`;
            }
        } catch (err) {
            error = 'Error fetching trips';
            console.error('Error fetching trips:', err);
        }
    }

    // Toggle the item in the trip (add/remove)
    async function toggleTripItem() {
        if (!selectedTrip) return;

        loading = true;
        error = null;

        try {
            const selectedTripObj = trips.find(trip => trip.id === selectedTrip);
            const alreadyAdded = selectedTripObj?.isItemAdded;

            // Define the URL and method based on whether the item is already added
            const url = `/api/trips/${selectedTrip}/places`;
            const method = alreadyAdded ? 'DELETE' : 'POST';

            // Make the request to add or remove the item
            const response = await fetch(url, {
                method,
                headers: {
                    'Authorization': `Bearer ${$token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id: item.id,
                    type: item.type
                })
            });

            if (response.ok) {
                // Refresh trips after the action
                await fetchTrips();
                dispatch('itemUpdated', {
                    tripId: selectedTrip,
                    item,
                    action: alreadyAdded ? 'removed' : 'added'
                });
            } else {
                const errorData = await response.json();
                error = errorData.detail || `Failed to ${alreadyAdded ? 'remove' : 'add'} item to trip`;
            }
        } catch (err) {
            error = `Error ${alreadyAdded ? 'removing' : 'adding'} item to trip`;
            console.error('Error:', err);
        } finally {
            loading = false;
        }
    }

    // Close the modal
    function closeModal() {
        showModal = false;
    }

    // Open the modal to choose a trip
    function openModal() {
        showModal = true;
    }
</script>

<!-- Button to open modal -->
<button on:click={openModal} class="add-trip-btn">
    Add to Trip
</button>

<!-- Modal to select trip -->
{#if showModal}
    <div class="modal" on:click|self={closeModal}>
        <div class="modal-content">
            <h2>Select a Trip</h2>

            {#if error}
                <div class="error-message">{error}</div>
            {/if}

            <div class="select-wrapper">
                <select bind:value={selectedTrip} class="input" disabled={loading}>
                    <option value={null}>Choose a trip...</option>
                    {#each trips as trip}
                        <option 
                            value={trip.id}
                            class:selected={trip.id === selectedTrip}
                        >
                            {trip.name} - {trip.destination}
                            {#if trip.isItemAdded}
                                (Already Added)
                            {/if}
                        </option>
                    {/each}
                </select>
            </div>

            <div class="button-group">
                <button 
                    on:click={closeModal} 
                    class="cancel-btn"
                    disabled={loading}
                >
                    Cancel
                </button>
                <button 
                    on:click={toggleTripItem} 
                    disabled={!selectedTrip || loading} 
                    class="button"
                >
                    {loading 
                        ? 'Processing...' 
                        : trips.find(trip => trip.id === selectedTrip)?.isItemAdded
                            ? 'Remove from Trip'
                            : 'Add to Trip'}
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

    .input option.selected {
        background-color: #f0f4f1;
        color: #26796c;
    }

    .input option:checked {
        background-color: #e0f7f3;
        color: #1f665b;
    }
</style>
