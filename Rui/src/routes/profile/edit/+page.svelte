<script lang="ts">
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';

    let user = {
        id: "12345",
        name: "Taylor Swift",
        email: "taylor@example.com",
        profileImage: "https://example.com/path/to/profile-image.jpg",
        birthdate: "1989-12-13",
        gender: "Female",
        address: "123 Ladprao, Bangkok, Thailand",
        phoneNumber: "+66 123 456 789"
    };

    // Event dispatcher for saving edited info
    const dispatch = createEventDispatcher();

    function handleSave() {
        // Dispatch event to save the user data
        dispatch('save', { user });
        // Redirect back to profile page after saving
        window.location.href = '/profile';
    }

    // Optionally: load user data when the component mounts
    onMount(() => {
        // Here you can fetch user data if needed
    });
</script>

<section class="edit-profile">
    <h2>Edit Profile</h2>
    <form on:submit|preventDefault={handleSave}>
        <div>
            <label for="name">Name:</label>
            <input type="text" id="name" bind:value={user.name} required />
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" bind:value={user.email} required />
        </div>
        <div>
            <label for="birthdate">Birthdate:</label>
            <input type="date" id="birthdate" bind:value={user.birthdate} required />
        </div>
        <div>
            <label for="gender">Gender:</label>
            <select id="gender" bind:value={user.gender} required>
                <option value="Female">Female</option>
                <option value="Male">Male</option>
                <option value="Other">Other</option>
            </select>
        </div>
        <div>
            <label for="address">Address:</label>
            <input type="text" id="address" bind:value={user.address} required />
        </div>
        <div>
            <label for="phoneNumber">Phone Number:</label>
            <input type="tel" id="phoneNumber" bind:value={user.phoneNumber} required />
        </div>
        <button type="submit">Save Changes</button>
    </form>
</section>

<style>
    .edit-profile {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    h2 {
        color: #26796c;
    }

    div {
        margin-bottom: 15px;
    }

    label {
        display: block;
        margin-bottom: 5px;
    }

    input, select {
        width: 100%;
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    button {
        padding: 10px 15px;
        background-color: #26796c;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    button:hover {
        background-color: #1f5f54;
    }
</style>
