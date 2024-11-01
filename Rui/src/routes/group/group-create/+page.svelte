<form class="box group-create">
    <div class="field">
      <label class="label">Group name</label>
      <div class="control">
        <input class="input" type="name" placeholder="Your group's name..." />
      </div>
    </div>
  
    <div class="field">
      <label class="label">Location</label>
      <div class="control">
        <input class="input" type="Location" placeholder="London..." />
      </div>
    </div>
  
    <div class="button-container">
      <button class="button">Confirm</button>
    </div>
  </form>
  
  <style>
    .group-create {
      max-width: 600px; /* Form width */
      margin: 5rem auto;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.13);
    }
  
    .group-create .field {
      margin-bottom: 1.5rem;
    }
  
    /* Style for the button container */
    .button-container {
      text-align: center; /* Align the button to the right */
    }
  
    /* Style for the Confirm button */
    .group-create .button {
      background-color: #26796c;
      color: white;
      border: none;
      padding: 0.75rem 1.5rem; /* Padding to reduce size */
      font-weight: bold;
      border-radius: 6px; /* Rounded corners */
      cursor: pointer;
      transition: background-color 0.3s ease;
    }
  
    /* Hover effect */
    .group-create .button:hover {
      background-color: #1f665b;
    }
  </style>
  