<script>
  import { onMount } from 'svelte';
  import { token, userId } from '$lib/stores/auth';
 
  let groups = [];
  let selectedGroupId = null;
  let availabilityInput = '';
  let error = '';
  let success = '';
 
  onMount(async () => {
    try {
      const response = await fetch(`/api/groups`, {
        headers: {
          'Authorization': `Bearer ${$token}`
        }
      });
 
      if (response.ok) {
        groups = await response.json();
      } else {
        error = `Failed to fetch groups: ${response.status}`;
      }
    } catch (err) {
      error = `Error fetching groups: ${err.message}`;
      console.error(err);
    }
  });
 
  async function updateAvailability() {
    try {
      const dates = availabilityInput.split(',').map(date => date.trim());
 
      const response = await fetch(`/api/availability/${selectedGroupId}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${$token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: $userId,
          date: dates,
        }),
      });
 
      if (response.ok) {
        success = 'Availability updated successfully';
        availabilityInput = '';
      } else {
        error = 'Failed to update availability';
      }
    } catch (err) {
      error = 'Error updating availability';
      console.error(err);
    }
  }
</script>
 
<div class="page-container">
  <h1>Update Availability</h1>
 
  <div class="form-container">
    <div class="select-group">
      <label for="group-select">Select Group:</label>
      <select id="group-select" bind:value={selectedGroupId} class="group-select">
        <option value="">Choose a group...</option>
        {#each groups as group}
          <option value={group.id}>{group.name}</option>
        {/each}
      </select>
    </div>
 
    {#if selectedGroupId}
      <div class="input-group">
        <label for="availability-input">Enter dates (YYYY-MM-DD, comma-separated):</label>
        <input type="text" id="availability-input" bind:value={availabilityInput} class="availability-input" />
      </div>
 
      <button class="update-btn" on:click={updateAvailability}>Update Availability</button>
 
      {#if error}
        <div class="error">{error}</div>
      {/if}
 
      {#if success}
        <div class="success">{success}</div>
      {/if}
    {/if}
  </div>
</div>
 
<style>
  .page-container {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }
  h1 {
    color: #26796c;
    margin-bottom: 2rem;
    text-align: center;
  }
  .select-group {
    margin-bottom: 1rem;
  }
 
  .group-select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-top: 4px;
  }
  .update-btn {
    width: 100%;
    padding: 8px;
    background: #26796c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
  }
  .error, .success {
    margin-top: 1rem;
    padding: 8px;
    border-radius: 4px;
    font-size: 0.9rem;
    text-align: center;
  }
 
  .error {
    background: #fff5f5;
    color: #dc3545;
  }
 
  .success {
    background: #f0fff4;
    color: #28a745;
  }
</style>
 
 