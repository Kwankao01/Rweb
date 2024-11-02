<script>
    import { onMount } from 'svelte';
    import { trips } from '$lib/store.js';
    import { getContext } from 'svelte';
  
    let tripId;
    let tripDetails = null; // Initialize to null for clarity
    let errorMessage = ''; // To hold any error messages
  
    onMount(async () => {
      tripId = getContext('id'); // Ensure this context is set in a parent component
      try {
        const response = await fetch(`http://localhost:5173/Trip/${tripId}`);
        if (response.ok) {
          tripDetails = await response.json();
        } else {
          errorMessage = 'Failed to fetch trip details. Please try again later.';
          console.error('Failed to fetch trip details:', response.statusText);
        }
      } catch (error) {
        errorMessage = 'An error occurred while fetching trip details.';
        console.error('Error fetching trip details:', error);
      }
    });
  </script>
  
  <h1>Trip Details</h1>
  {#if errorMessage}
    <p>{errorMessage}</p>
  {:else if tripDetails}
    <h2>{tripDetails.name}</h2>
    <p>Location: {tripDetails.location}</p>
    <p>Start Date: {tripDetails.startDate}</p>
    <p>End Date: {tripDetails.endDate}</p>
  {:else}
    <p>Loading...</p>
  {/if}
  