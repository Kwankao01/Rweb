<script lang="ts">
    import { onDestroy } from 'svelte';
    import { userStore } from '$lib/stores/userStore';
    import { goto } from '$app/navigation';

    let user;

    // โหลดข้อมูลผู้ใช้จาก Store
    const unsubscribe = userStore.subscribe(value => {
        user = { ...value }; // รับข้อมูลจาก Store
    });

    // ฟังก์ชันเพื่อเปลี่ยนไปยังหน้าแก้ไขโปรไฟล์
    function handleEdit() {
        goto('/profile/edit'); // นำไปยังหน้า Edit Profile
    }

    onDestroy(() => {
        unsubscribe(); // ยกเลิกการสมัครรับข้อมูลเมื่อคอมโพเนนต์ถูกทำลาย
    });
</script>

<section class="profile">
    <div class="profile-header">
        <img src={user.profileImage} alt="User Profile Image" class="profile-image" />
        <h2>{user.name}</h2>
        <p>{user.email}</p>
    </div>

    <div class="personal-info">
        <h3>Personal Information</h3>
        <ul>
            <li><strong>Birthdate:</strong> {user.birthdate}</li>
            <li><strong>Gender:</strong> {user.gender}</li>
            <li><strong>Address:</strong> {user.address}</li>
            <li><strong>Phone Number:</strong> {user.phoneNumber}</li>
        </ul>
    </div>

    <button class="edit-button" on:click={handleEdit}>Edit Info</button>
</section>

<style>
    .profile {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    .profile-header {
        text-align: center;
        margin-bottom: 20px;
    }

    .profile-image {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #26796c;
    }

    h2 {
        font-size: 1.8rem;
        color: #26796c;
        margin: 10px 0;
    }

    p {
        color: #555;
    }

    .personal-info {
        margin-bottom: 20px;
        padding: 15px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    h3 {
        font-size: 1.3rem;
        color: #26796c;
        margin-bottom: 10px;
    }

    ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    li {
        font-size: 1rem;
        color: #555;
        margin-bottom: 8px;
    }

    strong {
        color: #26796c;
    }

    .edit-button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: #26796c;
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 1.1rem;
        cursor: pointer;
        margin-top: 20px;
        transition: background-color 0.3s ease;
    }

    .edit-button:hover {
        background-color: #1f5f54;
    }
</style>
