<script>
  import { CalendarLogic } from '$lib/CalendarLogic.js';
  const {
    dayStore,
    groups,
    selectedGroup,
    loading,
    error,
    showConfirmModal,
    selectedDate,
    availabilityDates,
    weeks,
    TODAY,
    handleDateClick,
    changeMonth,
    confirmAvailability,
    closeModal,
    getDateString,
    fetchGroups,
    perfectMatchDates
  } = CalendarLogic();
 
  fetchGroups();
</script>
 
<main class="container mx-auto p-4 max-w-4xl">
  <div class="mb-6">
    <select
      bind:value={$selectedGroup}
      class="w-full p-2 border rounded-md"
      disabled={$loading}
    >
      <option value={null}>Select a group...</option>
      {#each $groups as group}
        <option value={group.id}>{group.name}</option>
      {/each}
    </select>
  </div>
 
  {#if $selectedGroup}
    <div class="mt-8 bg-white shadow rounded-lg p-4">
      <h2 class="text-lg font-semibold mb-4">Perfect Match Dates</h2>
      {#if $perfectMatchDates.length > 0}
        <div class="space-y-2">
          {#each $perfectMatchDates as date}
            <div class="p-3 bg-green-50 border border-green-200 rounded-md flex items-center justify-between">
              <span class="font-medium">
                {date.toLocaleDateString('en-US', {
                  weekday: 'long',
                  year: 'numeric',
                  month: 'long',
                  day: 'numeric'
                })}
              </span>
              <span class="text-green-600 flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                </svg>
                Everyone Available
              </span>
            </div>
          {/each}
        </div>
      {:else}
        <div class="text-center p-4 bg-gray-50 rounded-lg">
          <p class="text-gray-600">No dates found where everyone is available.</p>
          <p class="text-sm text-gray-500 mt-2">Try adding more availability dates or coordinating with group members.</p>
        </div>
      {/if}
    </div>
  {/if}
 
  {#if $error}
    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
      {$error}
    </div>
  {/if}
 
  <table class="w-full border-collapse">
    <thead>
      <tr class="text-center">
        <th class="p-2">
          <button
            on:click={changeMonth(-1)}
            class="month-nav-btn px-4 py-2 rounded hover:bg-gray-100"
          >
            &lt;
          </button>
        </th>
        <th colspan="5" class="p-2 text-xl font-bold">
          {$dayStore.toLocaleString(undefined, { month: "long" })}
          {$dayStore.getFullYear()}
        </th>
        <th class="p-2">
          <button
            on:click={changeMonth(1)}
            class="month-nav-btn px-4 py-2 rounded hover:bg-gray-100"
          >
            &gt;
          </button>
        </th>
      </tr>
      <tr>
        {#each ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] as dayName}
          <th class="p-2 text-sm">{dayName}</th>
        {/each}
      </tr>
    </thead>
    <tbody>
      {#each $weeks as week}
        <tr>
          {#each week as day}
            <td
              class="p-2 text-center border relative"
              class:bg-green-100={$availabilityDates[getDateString(day)]}
              class:bg-gray-50={!day}
            >
              {#if day}
                <button
                  class="calendar-btn w-8 h-8 rounded-full transition-colors relative overflow-hidden"
                  class:bg-blue-500={day.toDateString() === TODAY.toDateString()}
                  class:text-white={day.toDateString() === TODAY.toDateString()}
                  class:ring-2={day.toDateString() === $dayStore.toDateString()}
                  class:ring-blue-500={day.toDateString() === $dayStore.toDateString()}
                  class:bg-green-100={$availabilityDates[getDateString(day)]}
                  on:click={(e) => handleDateClick(day, e)}
                  disabled={$loading || $availabilityDates[getDateString(day)]}
                >
                  {day.getDate()}
                </button>
              {/if}
            </td>
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
 
  {#if $showConfirmModal && $selectedDate}
    <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full mx-4 transform scale-in">
        <h2 class="text-xl font-bold mb-4">Confirm Availability</h2>
        <p class="mb-6">
          Are you sure you want to add your availability for {$selectedDate.toLocaleDateString()}?
        </p>
        <div class="flex justify-end gap-4">
          <button
            class="px-4 py-2 rounded bg-gray-200 hover:bg-gray-300 transition-colors"
            on:click={closeModal}
          >
            Cancel
          </button>
          <button
            class="confirm-btn px-4 py-2 rounded bg-blue-500 text-white hover:bg-blue-600 transition-colors"
            on:click={confirmAvailability}
          >
            Confirm
          </button>
        </div>
      </div>
    </div>
  {/if}
 
  {#if $loading}
    <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white p-4 rounded-lg shadow-lg">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
      </div>
    </div>
  {/if}
</main>
 
<style>
  .calendar-btn {
    transition: transform 0.1s;
  }
 
  .calendar-btn:active {
    transform: scale(0.95);
  }
 
  .calendar-btn:hover:not(:disabled) {
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
 
  .ripple {
    position: absolute;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 50%;
    transform: scale(0);
    animation: ripple 0.6s linear;
    pointer-events: none;
  }
 
  .success-pulse {
    animation: successPulse 1s ease-out;
  }
 
  @keyframes ripple {
    to {
      transform: scale(4);
      opacity: 0;
    }
  }
 
  @keyframes successPulse {
    0% {
      box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
    }
    70% {
      box-shadow: 0 0 0 10px rgba(34, 197, 94, 0);
    }
    100% {
      box-shadow: 0 0 0 0 rgba(34, 197, 94, 0);
    }
  }
 
  :global(.scale-in) {
    animation: scaleIn 0.2s ease-out;
  }
 
  @keyframes scaleIn {
    from {
      transform: scale(0.95);
      opacity: 0;
    }
    to {
      transform: scale(1);
      opacity: 1;
    }
  }
 
  button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
 
  .month-nav-btn {
    transition: transform 0.1s;
  }
 
  .month-nav-btn:active {
    transform: scale(0.95);
  }
 
  .confirm-btn {
    position: relative;
    overflow: hidden;
  }
</style>