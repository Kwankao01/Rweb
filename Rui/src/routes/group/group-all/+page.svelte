<script>
    import { token, userId } from "$lib/stores/auth";
    import { onMount } from "svelte";
  
    let groups = [];
    let error = null;
  
    async function fetchGroups() {
      const authToken = $token;
      const currentUserId = $userId;
  
      if (!authToken || !currentUserId) {
        error = "User is not logged in.";
        return;
      }
  
      try {
        const response = await fetch(`/api/groups`, {
          headers: {
            "Authorization": `Bearer ${authToken}`,
            "Content-Type": "application/json"
          }
        });
  
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
  
        const data = await response.json();
        groups = data || [];
        console.log('Fetched groups:', groups);
      } catch (err) {
        console.error("Error fetching groups:", err);
        error = "Failed to fetch groups";
      }
    }
  
    onMount(fetchGroups);
</script>

{#if error}
    <p class="error">{error}</p>
{:else if groups.length === 0}
    <p>No groups found.</p>
{:else}
    <div class="box-container">
        {#each groups as group}
            <a href="/group/group-all/{group.id}" class="box">
                <img src={group.imageUrl || '/g1.jpeg'} alt={group.name}>
                <div>{group.name}</div>
            </a>
        {/each}
    </div>
{/if}

<style>
    .box-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap;
    }

    .box {
        max-width: 300px;
        margin: 2rem;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.13);
        text-align: center;
        text-decoration: none;
        color: #000;
        transition: transform 0.2s ease;
    }

    .box img {
        width: 100%;
        height: auto;
        border-radius: 5px;
        margin-bottom: 1rem;
    }

    .box:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
    }

    .error {
        color: red;
        text-align: center;
    }
</style>