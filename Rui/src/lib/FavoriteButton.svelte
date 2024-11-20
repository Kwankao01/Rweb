<script>
  import { goto } from '$app/navigation';
  import { favorites, addToFavorites, removeFromFavorites } from '$lib/favoritesStore';
  import { token } from '$lib/stores/auth.js';

  export let item;

  // Check if logged in using the token from the store
  $: isLoggedIn = !!$token;

  async function toggleFavorite(event) {
      event.stopPropagation();

      if (!isLoggedIn) {
          goto('/login');
          return;
      }

      const isFavorite = $favorites.some((fav) => fav.slug === item.slug);

      try {
          if (isFavorite) {
              await sendFavoriteRequest(item.slug, "DELETE");
              removeFromFavorites(item.slug);
          } else {
              await sendFavoriteRequest(item.slug, "POST");
              addToFavorites(item);
          }
      } catch (error) {
          console.error('Failed to update favorites:', error);
          alert('An error occurred while updating favorites');
      }
  }

  async function sendFavoriteRequest(slug, method) {
      // Fixed the API endpoint path to include /api/
      const response = await fetch(`/api/favorites/${slug}`, {
          method: method,
          headers: {
              'Authorization': `Bearer ${$token}`,
              'Content-Type': 'application/json',
          },
          // Adding credentials to ensure cookies are sent
          credentials: 'include'
      });

      if (!response.ok) {
          const error = await response.text();
          console.error('Server response:', error);
          throw new Error('Failed to update favorites');
      }

      return response.json();
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
