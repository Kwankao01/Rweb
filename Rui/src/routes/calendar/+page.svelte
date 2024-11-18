<!-- Calendar.svelte -->
<script>
    import { onMount } from 'svelte';
  
    export let groupId;
    export let userId;
    
    let currentDate = new Date();
    let selectedDates = new Set();
    let availableDates = [];
    let error = '';
    let success = '';
    let currentMonth = currentDate.getMonth();
    let currentYear = currentDate.getFullYear();
  
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
  
    async function fetchAvailableDates() {
      try {
        const response = await fetch(`/groups/${groupId}/available-dates/`);
        if (!response.ok) throw new Error('Failed to fetch dates');
        const data = await response.json();
        availableDates = data;
      } catch (err) {
        error = 'Failed to fetch available dates';
        console.error(err);
      }
    }
  
    async function updateAvailability() {
      try {
        const dates = Array.from(selectedDates);
        const response = await fetch(`/availability/group/${groupId}/user/${userId}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            group_id: groupId,
            user_id: userId,
            date: dates
          })
        });
  
        if (!response.ok) throw new Error('Failed to update');
        success = 'Availability updated successfully';
        setTimeout(() => success = '', 3000);
      } catch (err) {
        error = 'Failed to update availability';
        console.error(err);
      }
    }
  
    onMount(() => {
      fetchAvailableDates();
    });
  </script>
  
  <div class="calendar">
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
        <div 
          class="day"
          class:empty={!date}
          class:selected={selected}
          class:available={available}
          on:click={() => dateString && toggleDate(dateString)}
        >
          {date || ''}
        </div>
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
  
  <style>
    :global(.calendar) {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
  
    :global(.calendar-header) {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }
  
    :global(.calendar-header button) {
      padding: 8px 16px;
      background: #f0f0f0;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
  
    :global(.calendar-header button:hover) {
      background: #e0e0e0;
    }
  
    :global(.calendar-grid) {
      display: grid;
      grid-template-columns: repeat(7, 1fr);
      gap: 4px;
    }
  
    :global(.weekday) {
      text-align: center;
      font-weight: bold;
      padding: 8px;
      background: #f5f5f5;
    }
  
    :global(.day) {
      aspect-ratio: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      background: white;
      border: 1px solid #ddd;
      cursor: pointer;
      transition: all 0.2s;
    }
  
    :global(.day:hover:not(.empty)) {
      background: #f0f0f0;
    }
  
    :global(.day.empty) {
      background: #f5f5f5;
      cursor: default;
    }
  
    :global(.day.selected) {
      background: #007bff;
      color: white;
      border-color: #0056b3;
    }
  
    :global(.day.available) {
      border: 2px solid #28a745;
    }
  
    :global(.error) {
      color: #dc3545;
      margin-top: 16px;
      text-align: center;
    }
  
    :global(.success) {
      color: #28a745;
      margin-top: 16px;
      text-align: center;
    }
  
    :global(.update-btn) {
      display: block;
      width: 100%;
      padding: 12px;
      margin-top: 20px;
      background: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
  
    :global(.update-btn:hover) {
      background: #0056b3;
    }
  </style>