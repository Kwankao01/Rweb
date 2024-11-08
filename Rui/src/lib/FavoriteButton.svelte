<script>
  import { favorites, addToFavorites, removeFromFavorites } from '$lib/favoritesStore.js';
  export let item;

  function toggleFavorite(event) {
    event.stopPropagation();
    const isFavorite = $favorites.some(fav => fav.slug === item.slug);

    if (isFavorite) {
      removeFromFavorites(item.slug);
    } else {
      const itemType = item.type || 'Other';
      addToFavorites({ ...item, type: itemType });
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