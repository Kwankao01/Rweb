<script>
  export let searchTerm = "";
  export let onSearch;

  function handleSearch(event) {
    onSearch(event.target.value);
  }
</script>

<div class="search-container">
  <input
    type="text"
    class="search-input"
    placeholder="Search..."
    value={searchTerm}
    on:input={handleSearch}
  />
</div>

<style>
  .search-container {
      display: flex;
      justify-content: center;
      margin-top: 20px;
  }

  .search-input {
      padding: 10px 20px;
      border: 1px solid #ccc;
      border-radius: 30px;
      font-size: 18px;
      width: 60%;
      max-width: 800px;
      transition: width 0.3s ease;
      outline: none;
  }

  .search-input:focus {
      border-color: #26796c;
      box-shadow: 0 0 5px rgba(38, 121, 108, 0.2);
  }

  .search-input::placeholder {
      color: #999;
  }

  .search-input:hover {
      border-color: #26796c;
  }
</style>