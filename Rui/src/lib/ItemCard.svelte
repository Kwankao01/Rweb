<script>
    import FavoriteButton from './FavoriteButton.svelte';
    export let item;
    export let onSelectItem;
  
    function handleKeyDown(event) {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        onSelectItem(item.slug);
      }
    }
</script>
  
<div 
    class="item-card" 
    on:click={() => onSelectItem(item.slug)}
    on:keydown={handleKeyDown}
    role="button"
    tabindex="0"
    aria-label={`View details for ${item.title}`}
>
    <FavoriteButton {item} />
    <img src={item.image} alt={item.title} class="item-image" loading="lazy" />
    <div class="item-info">
        <h3 class="item-title">{item.title}</h3>
        <div class="rating" aria-label={`Rating: ${item.rating} out of 5 stars`}>
            {#each Array(5) as _, index}
                <i 
                  class={`fas fa-star ${index < Math.floor(item.rating) ? 'filled' : ''}`}
                  aria-hidden="true"
                ></i>
            {/each}
            <span class="reviews">({item.reviews} reviews)</span>
        </div>
        
        {#if item.type === 'landmark'}
            <p class="location">{item.location}</p>
        {:else if item.type === 'hotel' || item.type === 'restaurant'}
            {#if item.cancellation}
                <p class="cancellation">{item.cancellation}</p>
            {/if}
            {#if item.price !== undefined}
                <p class="price">From ฿ {item.price.toLocaleString()}</p>
            {/if}
        {/if}
        <p class="city">{item.city}</p>
    </div>
</div>
  
<style>
    .item-card {
        position: relative;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        overflow: hidden;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        outline: none;
        height: 400px;
        display: flex;
        flex-direction: column;
    }
  
    .item-card:focus {
        box-shadow: 0 0 0 2px #26796c, 0 4px 8px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
  
    .item-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
  
    .item-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 8px 8px 0 0;
        transition: transform 0.3s ease;
    }
  
    .item-card:hover .item-image {
        transform: scale(1.05);
    }
  
    .item-info {
        padding: 15px;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
  
    .item-title {
        font-size: 1.2rem;
        color: #26796c;
        margin: 0 0 8px 0;
        font-weight: 600;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        line-clamp: 2;
        white-space: normal;
        line-height: 1.3;
        height: 2.6em;
    }
  
    .rating {
        display: flex;
        align-items: center;
        gap: 4px;
        margin-bottom: 8px;
        height: 24px;
    }
  
    .rating .fa-star {
        color: #ccc;
    }
  
    .rating .fa-star.filled {
        color: #ffcc00;
    }
  
    .reviews {
        color: #666;
        font-size: 0.9rem;
        margin-left: 4px;
    }
  
    .cancellation {
        color: #4CAF50;
        font-size: 0.9rem;
        margin: 4px 0;
        height: 1.2em;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    .location {
        color: #666;
        font-size: 0.9rem;
        margin: 4px 0;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
  
    .price {
        color: #26796c;
        font-weight: bold;
        font-size: 1.1rem;
        margin: 4px 0;
    }
  
    .city {
        color: #666;
        font-size: 0.9rem;
        margin: 4px 0;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
  
    @media (prefers-reduced-motion: reduce) {
        .item-card,
        .item-image {
            transition: none;
        }
    }
</style>