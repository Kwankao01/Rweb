<script>
  import { token } from '$lib/stores/auth';
  import { goto } from '$app/navigation';
  
  let inviteCode = '';
  let error = '';
  let success = '';
 
  async function handleJoinGroup() {
    error = '';
    success = '';
    try {
      const response = await fetch('/api/groups/join', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${$token}`
        },
        body: JSON.stringify({ invite_code: inviteCode })
      });
 
      const data = await response.json();
 
      if (response.ok) {
        success = 'Successfully joined group!';
        setTimeout(() => {
          goto('/group-all'); // Redirect to groups page after success
        }, 1500);
        inviteCode = '';
      } else {
        error = data.detail || 'Failed to join group';
        console.error('Error:', data);
      }
    } catch (err) {
      error = err.message;
      console.error('Error:', err);
    }
  }
 </script>
 
 <div class="box join-group">
  {#if error}
    <p class="error">{error}</p>
  {/if}
  
  {#if success}
    <p class="success">{success}</p>
  {/if}
  
  <div class="field">
    <label class="label">Invite Code</label>
    <div class="control">
      <input class="input" type="text" bind:value={inviteCode} placeholder="Enter invite code"/>
    </div>
  </div>
 
  <div class="button-container">
    <button type="button" class="button" on:click={handleJoinGroup}>Confirm</button>
  </div>
 </div>
 
 <style>
  .join-group {
    max-width: 600px;
    margin: 5rem auto;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.13);
  }
 
  .field {
    margin-bottom: 1.5rem;
  }
 
  .button-container {
    text-align: center;
  }
 
  .button {
    background-color: #26796c;
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    font-weight: bold;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
 
  .button:hover {
    background-color: #1f665b;
  }
 
  .error {
    color: red;
    text-align: center;
    margin-top: 1rem;
  }
 
  .success {
    color: green;
    text-align: center;
    margin-top: 1rem;
  }
 </style>