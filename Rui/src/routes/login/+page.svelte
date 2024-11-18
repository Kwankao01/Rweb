<script>
  import { goto } from '$app/navigation'; // For navigation on successful login
  let email = '';
  let password = '';

  // Function to handle form submission
  async function handleLogin(event) {
      event.preventDefault();
      try {
          const response = await fetch('/api/login', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ email, password }),
          });

          if (!response.ok) {
              throw new Error('Invalid login');
          }

          const data = await response.json();
          // Navigate to profile or another protected page after successful login
          goto('/profile');
      } catch (error) {
          alert(error.message);
      }
  }
</script>

<main>
  <form on:submit|preventDefault={handleLogin} class="login-form">
      <div class="form-group">
          <label for="email">Email address</label>
          <input
              id="email"
              type="email"
              placeholder="Email"
              bind:value={email}
              required
          />
      </div>

      <div class="form-group">
          <label for="password">Password</label>
          <input
              id="password"
              type="password"
              placeholder="Password"
              bind:value={password}
              required
          />
      </div>

      <button type="submit" class="login-button">Login</button>
  </form>
</main>

<style>
  main {
      max-width: 400px;
      margin: auto;
      padding: 20px;
      font-family: Arial, sans-serif;
  }

  .form-group {
      margin-bottom: 20px;
  }

  label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
  }

  input {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-size: 14px;
  }

  .login-button {
      width: 100%;
      padding: 10px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
  }

  .login-button:hover {
      background-color: #0056b3;
  }
</style>
