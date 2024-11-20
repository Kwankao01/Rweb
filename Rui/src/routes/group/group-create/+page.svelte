<script>
  import { token, userId } from "$lib/stores/auth";
  
  let groupName = "";
  let location = "";
  let userEmails = "";
  let generatedInviteCode = "";
  let error = null;
  let success = false;
 
  async function handleFormSubmit(event) {
    event.preventDefault();
    error = null;
    success = false;
    const authToken = $token;
    const currentUserId = $userId;
 
    try {
      // Parse emails
      const emails = userEmails.split(',').map(email => email.trim()).filter(Boolean);
      
      // First get user IDs for emails if any are provided
      let allUserIds = [parseInt(currentUserId)];
      
      if (emails.length > 0) {
        const userResponse = await fetch("/api/users/find", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${authToken}`
          },
          body: JSON.stringify({ emails })
        });
        
        if (!userResponse.ok) throw new Error("Failed to find users");
        const users = await userResponse.json();
        allUserIds = [...allUserIds, ...users.map(user => user.id)];
      }
 
      const response = await fetch("/api/groups", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${authToken}`
        },
        body: JSON.stringify({
          name: groupName,
          user_ids: allUserIds
        })
      });
 
      if (!response.ok) throw new Error("Failed to create group");
      
      const data = await response.json();
      generatedInviteCode = data.invite_code;
      success = true;
      groupName = "";
      location = "";
      userEmails = "";
    } catch (err) {
      console.error("Error:", err);
      error = err.message;
    }
  }
 </script>
 
 <form class="box group-create" on:submit={handleFormSubmit}>
  {#if error}
    <div class="error">{error}</div>
  {/if}
  
  {#if success && generatedInviteCode}
    <div class="success">
      <p>Group created successfully!</p>
      <p>Invitation Code: <strong>{generatedInviteCode}</strong></p>
      <small>Share this code with others to join your group</small>
    </div>
  {/if}
 
  <div class="field">
    <label class="label">Group name</label>
    <div class="control">
      <input
        class="input"
        type="text"
        bind:value={groupName}
        placeholder="Your group's name..."
        required
      />
    </div>
  </div>
 
  <div class="field">
    <label class="label">Location</label>
    <div class="control">
      <input
        class="input"
        type="text"
        bind:value={location}
        placeholder="London..."
      />
    </div>
  </div>
 
  <div class="field">
    <label class="label">Add users by email (comma separated)</label>
    <div class="control">
      <textarea
        class="input"
        bind:value={userEmails}
        placeholder="user1@example.com, user2@example.com..."
      />
    </div>
  </div>
 
  <div class="button-container">
    <button class="button" type="submit">Confirm</button>
  </div>
 </form>
 
 <style>
  .box {
    max-width: 600px;
    margin: 5rem auto;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.13);
  }
 
  .input {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
 
  textarea.input {
    min-height: 100px;
    resize: vertical;
  }
 
  .error {
    color: red;
    margin-bottom: 1rem;
    text-align: center;
  }
  
  .success {
    color: green;
    margin-bottom: 1rem;
    text-align: center;
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
 
  .field {
    margin-bottom: 1.5rem;
  }
 </style>