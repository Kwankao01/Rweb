<script>
  import { onMount } from 'svelte';
  import { token } from '$lib/stores/auth';
 
  let trips = [];
  let editingTrip = null;
  let showModal = false;
  let tripLocation = '';
  let suggestions = [];
  let error = '';
 
  async function fetchTrips() {
    try {
      const response = await fetch('/api/trips/', {
        headers: {
          'Authorization': `Bearer ${$token}`
        }
      });
      if (response.ok) {
        trips = await response.json();
      } else {
        error = 'Failed to load trips';
      }
    } catch (err) {
      error = 'Error loading trips';
    }
  }
 
  async function updateTrip() {
    try {
      const response = await fetch(`/api/trips/${editingTrip.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${$token}`
        },
        body: JSON.stringify({
          name: editingTrip.name,
          destination: tripLocation,
          start: editingTrip.start,
          end: editingTrip.end,
          group_id: editingTrip.group_id
        })
      });
 
      if (response.ok) {
        await fetchTrips();
        closeModal();
      }
    } catch (err) {
      error = err.toString();
    }
  }
 
  function openEditModal(trip) {
    editingTrip = { ...trip };
    tripLocation = trip.destination;
    showModal = true;
  }
 
  function closeModal() {
    editingTrip = null;
    tripLocation = '';
    suggestions = [];
    showModal = false;
  }
 
  async function fetchLocations() {
    const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${tripLocation}`);
    const locations = await response.json();
    suggestions = locations.map(location => location.display_name);
  }
 
  function selectLocation(location) {
    tripLocation = location;
    suggestions = [];
  }
 
  onMount(fetchTrips);
 </script>
 
 <h1 class="title">My Trips</h1>
 
 <main>
  {#if error}
    <p class="error">{error}</p>
  {/if}
 
  {#if trips.length > 0}
    <ul class="trip-list">
      {#each trips as trip}
        <li class="trip-item">
          <div class="trip-details">
            <div class="trip-info">
              <div class="trip-name">{trip.name}</div>
              <div class="trip-location">
                <i class="fas fa-map-marker-alt"></i> {trip.destination}
              </div>
              <div class="trip-dates">
                <span>Start: {new Date(trip.start).toLocaleDateString()}</span><br>
                <span>End: {new Date(trip.end).toLocaleDateString()}</span>
              </div>
              <div class="trip-info-extra">
                <span class="duration">Duration: {trip.duration} days</span>
                <span class="countdown">Days until trip: {trip.countdown}</span>
              </div>
            </div>
            <button on:click={() => openEditModal(trip)} class="edit-button">Edit</button>
          </div>
        </li>
      {/each}
    </ul>
  {:else}
    <p class="no-trips">No trips found.</p>
  {/if}
 
  {#if showModal}
    <div class="modal">
      <div class="modal-content">
        <h3>Edit Trip</h3>
        <label>
          Trip Name:
          <input type="text" bind:value={editingTrip.name} />
        </label>
        <label>
          Location:
          <input type="text" bind:value={tripLocation} on:input={fetchLocations} />
          {#if suggestions.length > 0}
            <ul class="suggestions-list">
              {#each suggestions as suggestion}
                <li on:click={() => selectLocation(suggestion)}>{suggestion}</li>
              {/each}
            </ul>
          {/if}
        </label>
        <label>
          Start Date:
          <input type="date" bind:value={editingTrip.start} />
        </label>
        <label>
          End Date:
          <input type="date" bind:value={editingTrip.end} />
        </label>
        <div class="modal-buttons">
          <button on:click={updateTrip}>Save</button>
          <button on:click={closeModal}>Cancel</button>
        </div>
      </div>
    </div>
  {/if}
 </main>
 
 <style>
  .trip-info-extra {
    margin-top: 10px;
    display: flex;
    gap: 20px;
  }
 
  .duration, .countdown {
    font-size: 14px;
    color: #555;
  }
  .error {
    color: #dc3545;
    text-align: center;
    margin: 1rem 0;
  }
  main {
    display: flex;
    flex-direction: column;
    padding: 20px;
  }
  .trip-list {
    list-style-type: none;
    padding: 0;
    margin-top: 5px;
    width: 100%;
  }
  .trip-item {
    display: flex;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin: 15px 0;
    background-color: #f9f9f9;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  }
  .trip-details {
    display: flex;
    flex-grow: 1;
    justify-content: space-between;
    align-items: center;
  }
  .trip-name {
    font-size: 30px;
    font-weight: bold;
    color: #26796c;
  }
  .trip-location {
    display: flex;
    align-items: center;
    font-size: 18px;
    color: #135e41;
  }
  .trip-location .fa-map-marker-alt {
    margin-right: 5px;
    color: black;
  }
  .edit-button {
    padding: 4px 8px;
    font-size: 0.8em;
    background-color: #e0e0e0;
    color: #333;
    border: 1px solid #ccc;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  .edit-button:hover {
    background-color: #d5d5d5;
  }
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    width: 300px;
  }
  .modal h3 {
    margin-top: 0;
  }
  .modal label {
    display: block;
    margin-top: 10px;
  }
  .modal input {
    width: 100%;
    padding: 5px;
    margin-top: 5px;
    box-sizing: border-box;
  }
  .modal-buttons {
    margin-top: 20px;
    display: flex;
    justify-content: space-between;
  }
  .suggestions-list {
    list-style-type: none;
    padding: 0;
    margin: 5px 0 0 0;
    border: 1px solid #ddd;
    max-height: 100px;
    overflow-y: auto;
  }
  .suggestions-list li {
    padding: 8px;
    cursor: pointer;
  }
  .suggestions-list li:hover {
    background-color: #f0f0f0;
  }
</style>
