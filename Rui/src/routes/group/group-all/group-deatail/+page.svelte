<script>
    import { page } from "$app/stores"; // To access URL params
    import { onMount } from "svelte";
    
    let group = null;
    let error = null;
    let groupId;
  
    // Get the dynamic group ID from the URL
    $: groupId = $page.params.id;
  
    // Fetch the group details based on the group ID
    async function fetchGroupDetails() {
      try {
        const response = await fetch(`/api/groups/${groupId}`, {
          headers: {
            "Content-Type": "application/json",
          },
        });
  
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
  
        group = await response.json();
      } catch (err) {
        console.error("Error fetching group details:", err);
        error = "Failed to fetch group details";
      }
    }
  
    onMount(fetchGroupDetails);
  </script>
  
  {#if error}
    <p class="error">{error}</p>
  {:else if !group}
    <p>Loading group details...</p>
  {:else}
    <h1>{group.name}</h1>
    <p>{group.description}</p>
    <p>Group Size: {group.size}</p>
    <p>Invite Code: {group.invite_code}</p>
    <img src={group.imageUrl || '/g1.jpeg'} alt={group.name} style="width: 100%; border-radius: 8px;" />
  {/if}
  
  <style>
    .error {
      color: red;
      text-align: center;
    }
  </style>
  