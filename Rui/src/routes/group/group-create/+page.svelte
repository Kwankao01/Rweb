<script>
  import { token, userId } from "$lib/stores/auth";
  
  let groupName = "";
  let location = "";
  let userEmails = "";
  let error = null;
  let success = false;
 
  async function handleFormSubmit(event) {
    event.preventDefault();
    error = null;
    success = false;
 
    const authToken = $token;
    const currentUserId = $userId;
 
    if (!authToken || !currentUserId) {
      error = "User is not logged in";
      return;
    }
 
    // Parse emails into array and remove whitespace
    const emails = userEmails.split(',').map(email => email.trim()).filter(email => email);
 
    try {
      // First fetch user IDs for the emails
      const userResponse = await fetch("/api/users/find", {
        method: "POST",
        headers: {
          "Content-Type": "application/json", 
          "Authorization": `Bearer ${authToken}`
        },
        body: JSON.stringify({ emails })
      });
 
      if (!userResponse.ok) {
        throw new Error("Failed to find users");
      }
 
      const users = await userResponse.json();
      const userIds = users.map(user => user.id);
 
      // Add current user to group
      userIds.push(parseInt(currentUserId));
 
      // Create group with found user IDs
      const response = await fetch("/api/groups", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${authToken}`
        },
        body: JSON.stringify({
          name: groupName,
          user_ids: userIds
        })
      });
 
      if (!response.ok) {
        throw new Error("Failed to create group");
      }
 
      const data = await response.json();
      success = true;
      groupName = "";
      location = "";
      userEmails = "";
      
    } catch (err) {
      error = err.message;
      console.error("Error creating group:", err);
    }
  }
 </script>
 
 <form class="box group-create" on:submit={handleFormSubmit}>
  {#if error}
    <div class="error">{error}</div>
  {/if}
  {#if success}
    <div class="success">Group created successfully!</div>
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
  }
  
  .success {
    color: green;
    margin-bottom: 1rem;
  }
</style>
