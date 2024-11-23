<script>
  import { goto } from '$app/navigation';
  import { favorites, addToFavorites, removeFromFavorites } from '$lib/favoritesStore';
  import { token } from '$lib/stores/auth.js';
 
  export let item;
 
  $: isLoggedIn = !!$token;
  $: isFavorite = $favorites.some(fav => fav.slug === item.slug);
 
  async function toggleFavorite(event) {
      event.stopPropagation();
 
      if (!isLoggedIn) {
          goto('/login');
          return;
      }
 
      try {
          if (isFavorite) {
              await removeFromFavorites(item.slug);
          } else {
              await addToFavorites({
                  id: item.id,
                  type: item.type,
                  slug: item.slug,
                  // add any other required properties
              });
          }
      } catch (error) {
          console.error('Failed to update favorites:', error);
      }
  }
</script>
 
<button
  type="button"
  class="heart-button"
  aria-label={isFavorite ? "Remove from favorites" : "Add to favorites"}
  on:click={toggleFavorite}
>
  <i class="fas fa-heart" class:favorite={isFavorite}></i>
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
