<script>
    import { token, userId } from "$lib/stores/auth"; // Import token and userId from the store
    import { onMount } from "svelte";
  
    let userDetails = null; // To hold user data
    let error = null;
  
    // Fetch user data on page load
    async function fetchUserDetails() {
      const authToken = $token; // Access the token using $store syntax
      const currentUserId = $userId;
  
      if (!authToken || !currentUserId) {
        error = "User is not logged in.";
        return;
      }
  
      try {
        const response = await fetch(`/api/users/${currentUserId}`, {
          headers: {
            "Authorization": `Bearer ${authToken}`,
            "Content-Type": "application/json"
          }
        });
  
        if (!response.ok) {
          throw new Error("Failed to fetch user details.");
        }
  
        userDetails = await response.json();
      } catch (err) {
        error = err.message;
      }
    }
  
    onMount(fetchUserDetails); // Fetch data when the component is mounted
  </script>
  
  {#if error}
    <div class="error">{error}</div>
  {:else if !userDetails}
    <div class="loading">Loading user details...</div>
  {:else}
    <div class="user-details">
      <h1>User Profile</h1>
      <p><strong>Name:</strong> {userDetails.name}</p>
      <p><strong>Display Name:</strong> {userDetails.display_name}</p>
      <p><strong>Email:</strong> {userDetails.email}</p>
      <p><strong>Phone Number:</strong> {userDetails.phone_number}</p>
      <p><strong>Address:</strong> {userDetails.address}</p>
      <p><strong>User ID:</strong> {userDetails.id}</p>
    </div>
  {/if}
  
  <style>
    .user-details {
      max-width: 600px;
      margin: 2rem auto;
      padding: 1.5rem;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f9f9f9;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
  
    .user-details h1 {
      text-align: center;
      color: #26796c;
      margin-bottom: 1rem;
    }
  
    .user-details p {
      margin: 0.5rem 0;
      font-size: 1rem;
    }
  
    .user-details strong {
      color: #26796c;
    }
  
    .error {
      color: red;
      text-align: center;
      margin-top: 2rem;
    }
  
    .loading {
      text-align: center;
      margin-top: 2rem;
      font-size: 1.2rem;
      color: #666;
    }
  </style>
  