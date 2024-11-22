<script>
    import { token, userId } from "$lib/stores/auth";
    import { onMount } from "svelte";
    import { page } from "$app/stores";

    let trip = null;
    let error = null;
    let loading = true;

    async function fetchTripDetails() {
        const authToken = $token;
        const currentUserId = $userId;
        const tripId = $page.params.id;

        if (!authToken || !currentUserId) {
            error = "User is not logged in.";
            loading = false;
            return;
        }

        try {
            const response = await fetch(`/api/groups/${tripId}`, {
                headers: {
                    "Authorization": `Bearer ${authToken}`,
                    "Content-Type": "application/json"
                }
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            trip = data;
            console.log('Fetched trip details:', trip);
        } catch (err) {
            console.error("Error fetching trip details:", err);
            error = "Failed to fetch trip details";
        } finally {
            loading = false;
        }
    }

    onMount(fetchTripDetails);
</script>

{#if loading}
    <div class="loading">Loading...</div>
{:else if error}
    <div class="error">{error}</div>
{:else if trip}
    <div class="trip-detail">
        <div class="trip-header">
            <img src={group.imageUrl || '/g1.jpeg'} alt={group.name} class="group-image">
            <h1>{group.name}</h1>
        </div>
        
        <div class="group-info">
            <div class="info-section">
                <h2>Description</h2>
                <p>{group.description || 'No description available.'}</p>
            </div>

            {#if group.members}
            <div class="info-section">
                <h2>Members ({group.members.length})</h2>
                <div class="members-list">
                    {#each group.members as member}
                        <div class="member-item">
                            <img src={member.avatarUrl || '/default-avatar.png'} alt={member.name}>
                            <span>{member.name}</span>
                        </div>
                    {/each}
                </div>
            </div>
            {/if}
        </div>
    </div>
{:else}
    <div class="error">Group not found</div>
{/if}

<style>
    .group-detail {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }

    .group-header {
        text-align: center;
        margin-bottom: 2rem;
    }

    .group-image {
        width: 100%;
        max-width: 500px;
        height: auto;
        border-radius: 8px;
        margin-bottom: 1rem;
    }

    .group-info {
        display: grid;
        gap: 2rem;
    }

    .info-section {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .members-list {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }

    .member-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .member-item img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        object-fit: cover;
    }

    .loading {
        text-align: center;
        padding: 2rem;
    }

    .error {
        color: red;
        text-align: center;
        padding: 2rem;
    }

    h1 {
        font-size: 2rem;
        margin-bottom: 1rem;
    }

    h2 {
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }

    .details-button {
         padding: 4px 8px;
        font-size: 0.8em;
        background-color: #007BFF;
        color: white;
        border: 1px solid #007BFF;
        border-radius: 4px;
        cursor: pointer;
        text-decoration: none;
        transition: background-color 0.3s;
    }

    .details-button:hover {
        background-color: #0056b3;
    }
</style>