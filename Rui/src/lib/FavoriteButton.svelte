<script>
  import { goto } from '$app/navigation'; // SvelteKit navigation helper
  import { favorites, addToFavorites, removeFromFavorites } from '$lib/favoritesStore.js';

  export let item;

  let token = null; // Token for authentication, fetched from localStorage or API response

  // Check if the user is logged in
  $: isLoggedIn = !!token;

  // Function to toggle favorite
  async function toggleFavorite(event) {
      event.stopPropagation();

      if (!isLoggedIn) {
          // Redirect to login page if not logged in
          goto('/login');
          return;
      }

      // Check if the item is already a favorite
      const isFavorite = $favorites.some((fav) => fav.slug === item.slug);

      if (isFavorite) {
          // Remove from favorites
          removeFromFavorites(item.slug);
          await sendFavoriteRequest(item.slug, "DELETE");
      } else {
          // Add to favorites
          const itemType = item.type || 'Other';
          addToFavorites({ ...item, type: itemType });
          await sendFavoriteRequest(item.slug, "POST");
      }
  }

  // Function to send favorite request to the backend
  async function sendFavoriteRequest(slug, method) {
      try {
          const response = await fetch(`/api/favorites/${slug}`, {
              method: method,
              headers: {
                  Authorization: `Bearer ${token}`,
                  'Content-Type': 'application/json',
              },
          });

          if (!response.ok) {
              throw new Error('Failed to update favorites');
          }
      } catch (error) {
          console.error(error);
          alert('An error occurred while updating favorites');
      }
  }
</script>

<button
  type="button"
  class="heart-button"
  aria-label={$favorites.some(fav => fav.slug === item.slug) ? "Remove from favorites" : "Add to favorites"}
  on:click={toggleFavorite}
>
  <i class="fas fa-heart" class:favorite={$favorites.some(fav => fav.slug === item.slug)}></i>
</button>

<style>
  .heart-button {
    background: rgba(255, 255, 255, 0.8);
    border: none;
    border-radius: 50%;
    padding: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 1;
  }

  .heart-button:hover {
    background: rgba(255, 255, 255, 0.9);
    transform: scale(1.1);
  }

  .heart-button:active {
    transform: scale(0.95);
  }

  .heart-button i {
    color: #ccc;
    font-size: 20px;
    transition: color 0.3s ease;
  }

  .heart-button i.favorite {
    color: #FF0000;
  }
</style>
