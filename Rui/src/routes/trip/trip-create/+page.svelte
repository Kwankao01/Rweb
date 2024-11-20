<script>
    import { token } from '$lib/stores/auth';
    import { goto } from '$app/navigation';
   
    let tripName = '';
    let tripLocation = '';
    let startDate = '';
    let endDate = '';
    let selectedGroupId = '';
    let groups = [];
    let suggestions = [];
    let error = '';
   
    async function fetchGroups() {
      try {
        const response = await fetch('/api/groups', {
          headers: {
            'Authorization': `Bearer ${$token}`
          }
        });
        if (response.ok) {
          groups = await response.json();
        }
      } catch (err) {
        console.error('Error fetching groups:', err);
      }
    }
    
    fetchGroups();
   
    async function fetchLocations() {
      const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${tripLocation}`);
      const locations = await response.json();
      suggestions = locations.map(location => location.display_name);
    }
   
    async function selectLocation(location) {
      tripLocation = location;
      suggestions = [];
    }
   
    async function createTrip() {
      if (!tripName || !tripLocation || !startDate || !endDate || !selectedGroupId) {
        error = 'Please fill all fields';
        return;
      }
   
      try {
        const response = await fetch('/api/trips/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${$token}`
          },
          body: JSON.stringify({
            name: tripName,
            destination: tripLocation,
            start: startDate,
            end: endDate,
            group_id: parseInt(selectedGroupId)
          })
        });
   
        if (response.ok) {
          const data = await response.json();
          console.log('Trip created:', data);
          goto('/trip/Trip-list');
        } else {
          const data = await response.json();
          error = data.detail || 'Failed to create trip';
        }
      } catch (err) {
        error = err.message;
        console.error('Error:', err);
      }
    }
   </script>
   
   <div class="container">
    <h1 class="title">Create New Trip</h1>
   
    <form class="box trip-create" on:submit|preventDefault={createTrip}>
      {#if error}
        <p class="error">{error}</p>
      {/if}
   
      <div class="field">
        <label class="label">Trip Name</label>
        <div class="control">
          <input class="input" type="text" bind:value={tripName} placeholder="Your trip's name..." required />
        </div>
      </div>
   
      <div class="field">
        <label class="label">Location</label>
        <div class="control">
          <input class="input" type="text" bind:value={tripLocation} placeholder="Location..." 
            on:input={fetchLocations} required />
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
          <input class="input" type="date" bind:value={startDate} required />
        </div>
      </div>
   
      <div class="field">
        <label class="label">End Date</label>
        <div class="control">
          <input class="input" type="date" bind:value={endDate} required />
        </div>
      </div>
   
      <div class="field">
        <label class="label">Select Group</label>
        <div class="control">
          <select class="input" bind:value={selectedGroupId} required>
            <option value="">Choose a group...</option>
            {#each groups as group}
              <option value={group.id}>{group.name}</option>
            {/each}
          </select>
        </div>
      </div>
   
      <div class="button-container">
        <button type="submit" class="button">Create Trip</button>
      </div>
    </form>
   </div>
   
   <style>
    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 2rem;
    }
   
    .title {
      font-size: 2rem;
      font-weight: bold;
      margin-bottom: 2rem;
      color: #333;
    }
   
    .trip-create {
      background: white;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
   
    .field {
      margin-bottom: 1.5rem;
      position: relative;
    }
   
    .label {
      display: block;
      font-weight: bold;
      margin-bottom: 0.5rem;
      color: #363636;
    }
   
    .input {
      width: 100%;
      padding: 0.75rem;
      border: 1px solid #dbdbdb;
      border-radius: 4px;
      font-size: 1rem;
    }
   
    .input:focus {
      border-color: #26796c;
      box-shadow: 0 0 0 2px rgba(38, 121, 108, 0.2);
      outline: none;
    }
   
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
      width: 100%;
      border-radius: 4px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
   
    .suggestions-list li {
      padding: 0.75rem;
      cursor: pointer;
      border-bottom: 1px solid #eee;
    }
   
    .suggestions-list li:last-child {
      border-bottom: none;
    }
   
    .suggestions-list li:hover {
      background-color: #f5f5f5;
    }
   
    .button-container {
      text-align: center;
      margin-top: 2rem;
    }
   
    .button {
      background-color: #26796c;
      color: white;
      border: none;
      padding: 0.75rem 1.5rem;
      font-size: 1rem;
      font-weight: bold;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }
   
    .button:hover {
      background-color: #1f665b;
    }
   
    .error {
      color: #dc3545;
      text-align: center;
      margin: 1rem 0;
      padding: 0.75rem;
      background-color: #f8d7da;
      border-radius: 4px;
    }
   
    select.input {
      appearance: none;
      background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");
      background-repeat: no-repeat;
      background-position: right 1rem center;
      background-size: 1em;
      padding-right: 2.5rem;
    }
   </style>