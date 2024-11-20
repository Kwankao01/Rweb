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

  async function fetchGroups() {
    try {
      const response = await fetch('/api/groups', {
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
      error = 'Error loading groups';
    }
  }

  function getDaysInMonth(month, year) {
    return new Date(year, month + 1, 0).getDate();
  }

  function getFirstDayOfMonth(month, year) {
    return new Date(year, month, 1).getDay();
  }

  function getCalendarDays() {
    const daysInMonth = getDaysInMonth(currentMonth, currentYear);
    const firstDay = getFirstDayOfMonth(currentMonth, currentYear);
    const days = [];

    for (let i = 0; i < firstDay; i++) {
      days.push({ date: null, disabled: true });
    }

    for (let i = 1; i <= daysInMonth; i++) {
      const date = new Date(currentYear, currentMonth, i);
      const dateString = date.toISOString().split('T')[0];
      days.push({
        date: i,
        dateString,
        selected: selectedDates.has(dateString),
        available: availableDates.includes(dateString)
      });
    }

    return days;
  }

  async function fetchAvailableDates() {
    if (!selectedGroupId) return;
    
    try {
      const response = await fetch(`/api/groups/${selectedGroupId}/available-dates/`, {
        headers: {
          'Authorization': `Bearer ${$token}`
        }
      });
      if (!response.ok) throw new Error('Failed to fetch dates');
      const data = await response.json();
      availableDates = Array.isArray(data) ? data : [];
    } catch (err) {
      error = 'Failed to fetch available dates';
      console.error(err);
    }
  }

  async function updateAvailability() {
    if (!selectedGroupId) {
      error = 'Please select a group';
      return;
    }

    try {
      const dates = Array.from(selectedDates);
      const response = await fetch(`/api/availability/group/${selectedGroupId}/user/${$userId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${$token}`
        },
        body: JSON.stringify({
          group_id: parseInt(selectedGroupId),
          user_id: parseInt($userId),
          date: dates
        })
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || 'Failed to update');
      }
      
      success = 'Availability updated successfully';
      await fetchAvailableDates();
      setTimeout(() => success = '', 3000);
    } catch (err) {
      error = typeof err === 'string' ? err : err.message;
      console.error(err);
    }
  }

  function previousMonth() {
    if (currentMonth === 0) {
      currentMonth = 11;
      currentYear--;
    } else {
      currentMonth--;
    }
    currentDate = new Date(currentYear, currentMonth);
  }

  function nextMonth() {
    if (currentMonth === 11) {
      currentMonth = 0;
      currentYear++;
    } else {
      currentMonth++;
    }
    currentDate = new Date(currentYear, currentMonth);
  }

  function toggleDate(dateString) {
    if (selectedDates.has(dateString)) {
      selectedDates.delete(dateString);
    } else {
      selectedDates.add(dateString);
    }
    selectedDates = selectedDates;
  }

  function handleGroupChange() {
    selectedDates = new Set();
    if (selectedGroupId) {
      fetchAvailableDates();
    }
  }

  onMount(() => {
    if ($token) {
      fetchGroups();
    }
  });
</script>
  
<div class="container">
  <h1>Group Availability Calendar</h1>
  
  <div class="group-selector">
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
    <div class="calendar">
      <div class="info-text">
        <p><span class="color-sample available"></span> Everyone's available dates</p>
        <p><span class="color-sample selected"></span> Your selected dates</p>
      </div>

      <div class="calendar-header">
        <button class="nav-btn" on:click={previousMonth}>&lt;</button>
        <h2>{new Date(currentYear, currentMonth).toLocaleString('default', { month: 'long', year: 'numeric' })}</h2>
        <button class="nav-btn" on:click={nextMonth}>&gt;</button>
      </div>

      <div class="calendar-grid">
        <div class="weekday">Sun</div>
        <div class="weekday">Mon</div>
        <div class="weekday">Tue</div>
        <div class="weekday">Wed</div>
        <div class="weekday">Thu</div>
        <div class="weekday">Fri</div>
        <div class="weekday">Sat</div>

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

      {#if error}
        <div class="error">{error}</div>
      {/if}

      {#if success}
        <div class="success">{success}</div>
      {/if}

      <button class="update-btn" on:click={updateAvailability}>
        Update Availability
      </button>
    </div>
  {:else}
    <p class="select-group-message">Please select a group to view the calendar</p>
  {/if}
</div>

<style>
  .container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  h1 {
    text-align: center;
    color: #26796c;
    margin-bottom: 2rem;
    font-size: 28px;
    font-weight: bold;
  }

  .group-selector {
    margin-bottom: 2rem;
  }

  .group-selector label {
    display: block;
    margin-bottom: 0.5rem;
    color: #333;
    font-weight: 500;
  }

  .group-select {
    width: 100%;
    padding: 12px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    font-size: 16px;
    color: #333;
    background-color: #f8f9fa;
    transition: all 0.2s;
  }

  .group-select:focus {
    border-color: #26796c;
    outline: none;
    box-shadow: 0 0 0 2px rgba(38, 121, 108, 0.1);
  }

  .calendar {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }

  .info-text {
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 1.5rem;
  }

  .info-text p {
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 4px 0;
    color: #555;
  }

  .color-sample {
    width: 24px;
    height: 24px;
    border-radius: 6px;
    display: inline-block;
  }

  .calendar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
    padding: 0 1rem;
  }

  .calendar-header h2 {
    font-size: 1.2rem;
    font-weight: bold;
    color: #333;
  }

  .calendar-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 8px;
    margin-bottom: 1.5rem;
  }

  .weekday {
    text-align: center;
    font-weight: 600;
    padding: 12px;
    background: #f8f9fa;
    border-radius: 6px;
    color: #555;
    font-size: 0.9rem;
  }

  .day {
    aspect-ratio: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s;
    font-size: 1rem;
    color: #333;
    padding: 0;
  }

  .day:hover:not(.empty):not(:disabled) {
    background: #e8f5f2;
  }

  .day.empty, .day:disabled {
    background: #f5f5f5;
    cursor: default;
    border: none;
  }

  /* Change this style for the selected state */
  .day.selected {
    background: #26796c !important; /* Added !important to override hover */
    color: white;
    border: none;
    font-weight: bold;
  }

  .day.available {
    border: 2px solid #28a745;
  }

  /* When a date is both selected and available */
  .day.selected.available {
    background: #26796c !important;
    color: white;
    border: 2px solid #28a745;
  }

  .nav-btn {
    padding: 8px 16px;
    background: #f0f0f0;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1.2rem;
    color: #333;
    transition: all 0.2s;
  }

  .nav-btn:hover {
    background: #e0e0e0;
    color: #26796c;
  }

  .update-btn {
    display: block;
    width: 100%;
    padding: 14px;
    background: #26796c;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;
    font-size: 1rem;
    transition: all 0.2s;
    margin-top: 1.5rem;
  }

  .update-btn:hover {
    background: #1f665b;
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .error, .success {
    text-align: center;
    margin: 1rem 0;
    padding: 12px;
    border-radius: 8px;
    font-weight: 500;
  }

  .error {
    background-color: #fff5f5;
    color: #dc3545;
    border: 1px solid #ffebee;
  }

  .success {
    background-color: #f0fff4;
    color: #28a745;
    border: 1px solid #ebfff0;
  }

  .select-group-message {
    text-align: center;
    color: #666;
    margin-top: 2rem;
    padding: 2rem;
    background: #f8f9fa;
    border-radius: 8px;
    font-size: 1.1rem;
  }
</style>