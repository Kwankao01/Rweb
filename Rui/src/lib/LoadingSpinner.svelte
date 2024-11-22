<!-- src/lib/LoadingSpinner.svelte -->
<script>
    export let isLoading = false;
  </script>
  
  {#if isLoading}
    <div class="spinner-container">
      <div class="spinner"></div>
    </div>
  {/if}
  
  <style>
    .spinner-container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
  
    .spinner {
      border: 4px solid #f3f3f3;
      border-top: 4px solid #26796c;
      border-radius: 50%;
      width: 50px;
      height: 50px;
      animation: spin 1s linear infinite;
    }
  
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
  </style>
  