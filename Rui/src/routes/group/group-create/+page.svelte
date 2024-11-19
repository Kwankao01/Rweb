<script>
  //@ts-nocheck
  import { onMount } from "svelte";
  import { token, userId } from "$lib/stores/auth.js"; // Import the store for token and user ID
  let groupName = ""; // Bind to the group name input
  let location = ""; // Bind to the location input

  async function handleFormSubmit(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const token = localStorage.getItem("token");
    const userId = localStorage.getItem("user_id");

    if (!token || !userId) {
      console.error("User is not logged in");
      return;
    }

    // Prepare the API request payload
    const payload = {
      name: groupName,
      user_ids: [userId, 2, 3], // Add more user IDs if needed
    };

    // Make the API request
    const response = await fetch("/api/groups", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`,
      },
      body: JSON.stringify(payload),
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Group created:", data);
    } else {
      console.error("Failed to create group");
    }
  }
</script>

<form class="box group-create" on:submit|preventDefault={handleFormSubmit}>
  <div class="field">
    <label class="label">Group name</label>
    <div class="control">
      <input
        class="input"
        type="text"
        bind:value={groupName}
        placeholder="Your group's name..."
        required
      />
    </div>
  </div>

  <div class="field">
    <label class="label">Location</label>
    <div class="control">
      <input
        class="input"
        type="text"
        bind:value={location}
        placeholder="London..."
      />
    </div>
  </div>

  <div class="button-container">
    <button class="button" type="submit">Confirm</button>
  </div>
</form>

<style>
  .group-create {
    max-width: 600px; /* Form width */
    margin: 5rem auto;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.13);
  }

  .group-create .field {
    margin-bottom: 1.5rem;
  }

  /* Style for the button container */
  .button-container {
    text-align: center; /* Align the button to the right */
  }

  /* Style for the Confirm button */
  .group-create .button {
    background-color: #26796c;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem; /* Padding to reduce size */
    font-weight: bold;
    border-radius: 6px; /* Rounded corners */
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  /* Hover effect */
  .group-create .button:hover {
    background-color: #1f665b;
  }
</style>
