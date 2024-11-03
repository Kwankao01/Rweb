<script lang="ts" context="module">
    export async function load({ params }) {
        // สมมติว่าเราใช้ UserID ใน URL เช่น /profile/12345
        const userId = params.slug; // รับ slug (UserID)

        // โหลดข้อมูลผู้ใช้จาก API หรือ Store ตาม UserID
        // สำหรับตัวอย่างนี้ เราจะส่งข้อมูล UserID ไปยัง component
        return {
            props: {
                userId
            }
        };
    }
</script>

<script lang="ts">
    import { onDestroy } from 'svelte';
    import { userStore } from '$lib/stores/userStore';

    export let userId; // รับ UserID จาก props
    let user;

    // โหลดข้อมูลผู้ใช้จาก Store
    const unsubscribe = userStore.subscribe(value => {
        user = { ...value }; // รับข้อมูลจาก Store
    });

    onDestroy(() => {
        unsubscribe(); // ยกเลิกการสมัครรับข้อมูลเมื่อคอมโพเนนต์ถูกทำลาย
    });
</script>

<section class="profile-slug">
    <h2>Profile ID: {userId}</h2>
    <div class="profile-info">
        <h3>User Information</h3>
        <p><strong>Name:</strong> {user.name}</p>
        <p><strong>Email:</strong> {user.email}</p>
        <p><strong>Birthdate:</strong> {user.birthdate}</p>
        <p><strong>Gender:</strong> {user.gender}</p>
        <p><strong>Address:</strong> {user.address}</p>
        <p><strong>Phone Number:</strong> {user.phoneNumber}</p>
    </div>
</section>

<style>
    .profile-slug {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    h2 {
        color: #26796c;
    }

    .profile-info {
        padding: 15px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    strong {
        color: #26796c;
    }
</style>
