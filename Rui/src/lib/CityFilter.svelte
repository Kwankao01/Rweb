<script>
  export let filterOptions = []; 
  export let selectedFilter = "";
  export let filterType = 'city';
  export let FilterSelect;
  export let pageType = ""; 

  function selectFilter(filter) {
    FilterSelect(filter);
  }

  $: allButtonText = () => {
    if (pageType === 'favorite') {
      return 'All Types';
    } else {
      return 'All Cities';
    }
  }
</script>

<div class="city-filters">
  <button
    class:selected={!selectedFilter}
    on:click={() => selectFilter("")}
  >
    {allButtonText()}
  </button>
  {#each filterOptions as filter}
    <button
      class:selected={selectedFilter === filter}
      on:click={() => selectFilter(filter)}
    >
      {filter}
    </button>
  {/each}
</div>


<style>
  .city-filters {
      display: flex;
      gap: 10px;
      flex-wrap: wrap; 
      padding-left: 5px;
      margin-top: 5px;
  }

  button {
      padding: 8px 16px;
      border: none;
      border-radius: 20px;
      background-color: #f1f1f1;
      color: #333;
      cursor: pointer;
      font-size: 16px;
      font-weight: bold;
      transition: all 0.2s ease; /* Smooth transition for all changes */
  }

  button:hover {
      background-color: #e0e0e0;
      transform: translateY(-1px); /* Subtle lift effect */
  }

  button.selected {
      background-color: #26796c;
      color: white;
      box-shadow: 0 2px 4px rgba(38, 121, 108, 0.2); /* Subtle shadow for selected state */
  }

  /* Active state when clicking */
  button:active {
      transform: translateY(1px);
  }

  /* Focus state for accessibility */
  button:focus {
      outline: none;
      box-shadow: 0 0 0 2px rgba(38, 121, 108, 0.3);
  }

  /* Ensure selected button maintains shadow when focused */
  button.selected:focus {
      box-shadow: 0 0 0 2px rgba(38, 121, 108, 0.3),
                  0 2px 4px rgba(38, 121, 108, 0.2);
  }
</style>