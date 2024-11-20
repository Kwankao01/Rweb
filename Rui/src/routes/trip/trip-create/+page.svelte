<h1 style="margin-left: 20px; font-size: 30px; font-weight: bold;">Create New Trip</h1>

<script>
// @ts-nocheck

  import { trips } from '$lib/trips.js'; 
  import { goto } from '$app/navigation'; 

  let tripName = '';
  let tripLocation = '';
  let startDate = '';
  let endDate = '';
  let suggestions = []; 

  async function fetchLocations() {
      const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${tripLocation}`);
      const locations = await response.json();
      suggestions = locations.map(location => location.display_name); 
  }

  async function selectLocation(location) {
      tripLocation = location; 
      suggestions = []; 
  }

  function createTrip() {
      if (tripName && tripLocation && startDate && endDate) {
          trips.update(currentTrips => [
              ...currentTrips,
              { 
                id: Date.now(), 
                name: tripName, 
                location: tripLocation, 
                startDate: startDate, 
                endDate: endDate 
              }
          ]);

          tripName = '';
          tripLocation = '';
          startDate = '';
          endDate = '';
          goto('/trip/Trip-list'); 
      }
  }
</script>

<form class="box trip-create" on:submit|preventDefault={createTrip}>

  <div class="field">
      <label class="label">Trip name</label>
      <div class="control">
          <input class="input" type="text" bind:value={tripName} placeholder="Your trip's name..." />
      </div>
  </div>

  <div class="field">
      <label class="label">Location</label>
      <div class="control">
          <input class="input" type="text" bind:value={tripLocation} placeholder="Location..." on:input={fetchLocations} />
      </div>
      {#if suggestions.length > 0}
      <ul class="suggestions-list">
          {#each suggestions as suggestion}
          <li on:click={() => selectLocation(suggestion)}>
            <span>{suggestion}</span>
          </li>
          {/each}
      </ul>
      {/if}
  </div>

  <div class="field">
      <label class="label">Start Date</label>
      <div class="control">
          <input class="input" type="date" bind:value={startDate} />
      </div>
  </div>

  <div class="field">
      <label class="label">End Date</label>
      <div class="control">
          <input class="input" type="date" bind:value={endDate} />
      </div>
  </div>

  <div class="button-container">
      <button type="submit" class="button">Confirm</button>
  </div>
</form>



<style>
  .suggestions-list {
      list-style-type: none;
      padding: 0;
      margin: 0;
      border: 1px solid #ddd;
      max-height: 150px; 
      overflow-y: auto; 
      position: absolute;
      z-index: 10;
      background-color: white; 
      width: calc(100% - 2rem); 
  }

  .suggestions-list li {
      padding: 8px; 
      cursor: pointer; 
  }

  .suggestions-list li:hover {
      background-color: #f0f0f0;
  }
</style>
