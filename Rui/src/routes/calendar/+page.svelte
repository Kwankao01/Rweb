<script>
  import { onMount } from 'svelte';
  import { token, userId } from '$lib/stores/auth';
 
  let groups = [];
  let selectedGroupId = null;
  let currentDate = new Date();
  let selectedDates = new Set();
  let availableDates = [];
  let error = '';
  let success = '';
  let currentMonth = currentDate.getMonth();
  let currentYear = currentDate.getFullYear();
  let isCalendarOpen = false;
 
  onMount(async () => {
    try {
      const response = await fetch(`/api/users/${$userId}/groups`, {
        headers: {
          'Authorization': `Bearer ${$token}`
        }
      });
 
      if (response.ok) {
        groups = await response.json();
      } else {
        error = 'Failed to fetch groups';
      }
    } catch (err) {
      error = 'Error fetching groups';
      console.error(err);
    }
  });

  function toggleCalendar() {
    isCalendarOpen = !isCalendarOpen;
  }

  function previousMonth() {
    if (currentMonth === 0) {
      currentMonth = 11;
      currentYear--;
    } else {
      currentMonth--;
    }
  }

  function nextMonth() {
    if (currentMonth === 11) {
      currentMonth = 0;
      currentYear++;
    } else {
      currentMonth++;
    }
  }

  function getCalendarDays() {
    const firstDayOfMonth = new Date(currentYear, currentMonth, 1);
    const lastDayOfMonth = new Date(currentYear, currentMonth + 1, 0);
    
    const daysInMonth = [];
    const startDay = firstDayOfMonth.getDay();
    const endDate = lastDayOfMonth.getDate();

    for (let i = 0; i < startDay; i++) {
      daysInMonth.push({ date: null, dateString: null, available: false });
    }

    for (let date = 1; date <= endDate; date++) {
      const dateString = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}-${String(date).padStart(2, '0')}`;
      const available = availableDates.includes(dateString);
      const selected = selectedDates.has(dateString);
      daysInMonth.push({ date, dateString, available, selected });
    }
    
    return daysInMonth;
  }

  function toggleDate(dateString) {
    if (selectedDates.has(dateString)) {
      selectedDates.delete(dateString);
    } else {
      selectedDates.add(dateString);
    }
  }

  async function updateAvailability() {
    try {
      const response = await fetch(`/api/availability/${selectedGroupId}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${$token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ dates: Array.from(selectedDates) })
      });

      if (response.ok) {
        success = 'Availability updated successfully';
      } else {
        error = 'Failed to update availability';
      }
    } catch (err) {
      error = 'Error updating availability';
      console.error(err);
    }
  }

  function handleGroupChange() {
    selectedDates.clear();
    availableDates = [];
  }
</script>
 
<div class="page-container">
  <h1>Availability Calendar</h1>
 
  <div class="calendar-container">
    <div class="select-group">
      <label for="group-select">Select Group:</label>
      <select
        id="group-select"
        bind:value={selectedGroupId}
        on:change={handleGroupChange}
        class="group-select"
      >
        <option value="">Choose a group...</option>
        {#each groups as group}
          <option value={group.id}>{group.name}</option>
        {/each}
      </select>
    </div>
 
    {#if selectedGroupId}
      <div class="dropdown-calendar">
        <button class="calendar-toggle" on:click={toggleCalendar}>
          Select Dates
          <span class="arrow">{isCalendarOpen ? '▼' : '▲'}</span>
        </button>
 
        {#if isCalendarOpen}
          <div class="calendar-popup">
            <div class="info-text">
              <p><span class="color-sample available"></span> Everyone's available</p>
              <p><span class="color-sample selected"></span> Your selections</p>
            </div>
 
            <div class="calendar-header">
              <button class="nav-btn" on:click={previousMonth}>&lt;</button>
              <h2>{new Date(currentYear, currentMonth).toLocaleString('default', { month: 'long', year: 'numeric' })}</h2>
              <button class="nav-btn" on:click={nextMonth}>&gt;</button>
            </div>
 
            <div class="calendar-grid">
              <div class="weekday">S</div>
              <div class="weekday">M</div>
              <div class="weekday">T</div>
              <div class="weekday">W</div>
              <div class="weekday">T</div>
              <div class="weekday">F</div>
              <div class="weekday">S</div>
 
              {#each getCalendarDays() as { date, dateString, selected, available }}
                <button
                  class="day"
                  class:empty={!date}
                  class:selected={selected}
                  class:available={available}
                  disabled={!dateString}
                  on:click={() => dateString && toggleDate(dateString)}
                  type="button"
                >
                  {date || ''}
                </button>
              {/each}
            </div>
 
            <button class="update-btn" on:click={updateAvailability}>
              Update Availability
            </button>
          </div>
        {/if}
      </div>
 
      {#if error}
        <div class="error">{error}</div>
      {/if}
 
      {#if success}
        <div class="success">{success}</div>
      {/if}
    {/if}
  </div>
</div>
 
<style>
  .page-container {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }
 
  h1 {
    color: #26796c;
    margin-bottom: 2rem;
    text-align: center;
  }
  .calendar-container {
    width: 300px;
    margin: 0 auto;
    position: relative;
  }
 
  .select-group {
    margin-bottom: 1rem;
  }
 
  .calendar-toggle {
    width: 100%;
    padding: 10px;
    background: white;
    border: 1px solid #ddd;
    border-radius: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
  }
 
  .calendar-popup {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 1rem;
    margin-top: 0.5rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    z-index: 1000;
  }
 
  .group-select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-top: 4px;
  }
 
  .calendar-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 2px;
    margin: 1rem 0;
  }
 
  .weekday {
    text-align: center;
    font-size: 0.8rem;
    padding: 4px;
    color: #666;
  }
 
  .day {
    aspect-ratio: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
    border: 1px solid #ddd;
    font-size: 0.9rem;
    padding: 0;
    cursor: pointer;
  }
 
  .day.selected {
    background: #26796c !important;
    color: white;
    border: none;
  }
 
  .day.available {
    border: 2px solid #28a745;
  }
 
  .day:disabled {
    background: #f5f5f5;
    cursor: default;
  }
 
  .update-btn {
    width: 100%;
    padding: 8px;
    background: #26796c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
  }
 
  .info-text {
    font-size: 0.8rem;
    margin-bottom: 1rem;
  }
 
  .color-sample {
    width: 12px;
    height: 12px;
    display: inline-block;
    margin-right: 4px;
  }
 
  .color-sample.available {
    border: 2px solid #28a745;
    background: white;
  }
 
  .color-sample.selected {
    background: #26796c;
  }
 
  .calendar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
  }
 
  .nav-btn {
    padding: 4px 8px;
    background: none;
    border: none;
    cursor: pointer;
  }
 
  .error, .success {
    margin-top: 1rem;
    padding: 8px;
    border-radius: 4px;
    font-size: 0.9rem;
    text-align: center;
  }
 
  .error {
    background: #fff5f5;
    color: #dc3545;
  }
 
  .success {
    background: #f0fff4;
    color: #28a745;
  }
</style>
 