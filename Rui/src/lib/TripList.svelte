<script>
    let trips = [
        { id: 'trip1', name: 'First Trip' },
        { id: 'trip2', name: 'Second Trip' }
    ];

    // ฟังก์ชันสำหรับการแก้ไขทริป
    function editTrip(tripId) {
        // ค้นหา index ของทริปที่ต้องการแก้ไข
        const tripIndex = trips.findIndex(t => t.id === tripId);
        if (tripIndex !== -1) { // ตรวจสอบว่าทริปมีอยู่จริง
            const newName = prompt('Enter new trip name:', trips[tripIndex].name); // ขอให้ผู้ใช้กรอกชื่อใหม่
            if (newName) {
                trips[tripIndex].name = newName; // อัปเดตชื่อทริป
            }
        }
    }
</script>

<style>
    .trip-box {
        max-width: 300px;
        margin: 2rem auto;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.13);
        cursor: pointer;
        text-align: center;
        font-weight: bold;
        position: relative;
    }
    .trip-box button {
        position: absolute;
        right: 10px;
        top: 10px;
        padding: 0.2rem 0.6rem;
        cursor: pointer;
    }
</style>

{#each trips as trip}
    <div class="trip-box" id={trip.id}>
        <span>{trip.name}</span>
        <button on:click={() => editTrip(trip.id)}>Edit</button>
    </div>
{/each}
