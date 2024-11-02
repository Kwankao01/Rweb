<script>
  import { trips } from '$lib/store.js'; // นำเข้าจาก store
  import { goto } from '$app/navigation'; // สำหรับการนำทาง

  let tripName = '';
  let tripLocation = '';
  let startDate = '';
  let endDate = '';
  let suggestions = []; // สำหรับเก็บรายการที่แนะนำ

  async function fetchLocations() {
      if (tripLocation.length < 3) { // เริ่มค้นหาหลังจากพิมพ์ครบ 3 ตัว
          suggestions = [];
          return;
      }

      const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${tripLocation}`);
      const locations = await response.json();
      suggestions = locations.map(location => location.display_name); // สร้างรายการแนะนำ
  }

  async function selectLocation(location) {
      tripLocation = location; // ตั้งค่าที่อยู่ที่เลือกใน input
      suggestions = []; // ลบ suggestions หลังจากเลือก
  }

  function createTrip() {
      if (tripName && tripLocation && startDate && endDate) {
          trips.update(currentTrips => [
              ...currentTrips,
              { 
                id: Date.now(), 
                name: tripName, 
                location: tripLocation, 
                startDate: startDate, 
                endDate: endDate 
              }
          ]);
          // ล้างค่าหลังจากสร้างทริปใหม่
          tripName = '';
          tripLocation = '';
          startDate = '';
          endDate = '';
          goto('/Trip-list'); // นำทางไปยังหน้า Trip-list หลังจากสร้างเสร็จ
      }
  }
</script>

<h1 style="margin-left: 20px; font-size: 30px; font-weight: bold;">Create New Trip</h1>

<form class="box group-create" on:submit|preventDefault={createTrip}>
  <div class="field">
      <label class="label">Trip name</label>
      <div class="control">
          <input class="input" type="text" bind:value={tripName} placeholder="Your trip's name..." />
      </div>
  </div>

  <div class="field">
      <label class="label">Location</label>
      <div class="control">
          <input class="input" type="text" bind:value={tripLocation} placeholder="Location..." on:input={fetchLocations} />
      </div>
      {#if suggestions.length > 0}
      <ul class="suggestions-list">
          {#each suggestions as suggestion}
          <li on:click={() => selectLocation(suggestion)}>
            <span>{suggestion}</span>
          </li>
          {/each}
      </ul>
      {/if}
  </div>

  <div class="field">
      <label class="label">Start Date</label>
      <div class="control">
          <input class="input" type="date" bind:value={startDate} />
      </div>
  </div>

  <div class="field">
      <label class="label">End Date</label>
      <div class="control">
          <input class="input" type="date" bind:value={endDate} />
      </div>
  </div>

  <div class="button-container">
      <button type="submit" class="button">Confirm</button>
  </div>
</form>

<style>
  .suggestions-list {
      list-style-type: none;
      padding: 0;
      margin: 0;
      border: 1px solid #ddd;
      max-height: 150px; /* กำหนดความสูงสูงสุดของ suggestions */
      overflow-y: auto; /* เพิ่มการเลื่อนเมื่อรายการยาวเกินไป */
      position: absolute;
      z-index: 10;
      background-color: white; /* ให้พื้นหลังของรายการ */
      width: calc(100% - 2rem); /* ทำให้กว้างเท่ากับ input */
  }

  .suggestions-list li {
      padding: 8px; /* เพิ่ม padding */
      cursor: pointer; /* แสดง cursor pointer เมื่อ hover */
  }

  .suggestions-list li:hover {
      background-color: #f0f0f0; /* เปลี่ยนพื้นหลังเมื่อ hover */
  }
</style>
