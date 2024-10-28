<form class="box join-group">
    <div class="field">
      <label class="label">Group ID</label>
      <div class="control">
        <input class="input" type="ID" placeholder="eg. AAA333" />
      </div>
    </div>
  
  
    <div class="button-container">
      <button class="button">Confirm</button>
    </div>
  </form>
  
  <style>
    .join-group {
      max-width: 600px; /* Form width */
      margin: 5rem auto;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.13);
    }
  
    .join-group .field {
      margin-bottom: 1.5rem;
    }
  
    /* Style for the button container */
    .button-container {
      text-align: center; /* Align the button to the right */
    }
  
    /* Style for the Confirm button */
    .join-group .button {
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
    .join-group .button:hover {
      background-color: #1f665b;
    }
  </style>
  
