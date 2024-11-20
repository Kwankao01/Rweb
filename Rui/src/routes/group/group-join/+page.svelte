<script>
  import { token } from '$lib/stores/auth';

  let inviteCode = '';

  async function handleJoinGroup() {
    try {
      const response = await fetch('/groups/join', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${$token}`
        },
        body: JSON.stringify({ invite_code: inviteCode })
      });

      if (response.ok) {
        console.log('Joined group successfully');
        inviteCode = '';
      } else {
        console.error('Failed to join group');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }
</script>

<form class="box join-group">
  <div class="field">
    <label class="label">Invite Code</label>
    <div class="control">
      <input class="input" type="text" bind:value={inviteCode} placeholder="Enter invite code" />
    </div>
  </div>

  <div class="button-container">
    <button class="button" on:click={handleJoinGroup}>Confirm</button>
  </div>
</form>

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
</style>
  
