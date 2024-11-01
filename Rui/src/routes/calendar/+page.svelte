<script lang="ts">
    let currentDate = new Date();
    let selectedGroup: string = ''; // Track the selected group
    
    const months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

    // Generate array of years from 2024 to 2029
    const years = Array.from({ length: 6 }, (_, i) => 2024 + i);

    function daysInMonth(date: Date): number {
        return new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    }

    function firstDayOfMonth(date: Date): number {
        return new Date(date.getFullYear(), date.getMonth(), 1).getDay();
    }

    function handleMonthChange(event: Event): void {
        const newMonth = parseInt((event.target as HTMLSelectElement).value);
        currentDate.setMonth(newMonth);
    }

    function handleYearChange(event: Event): void {
        const newYear = parseInt((event.target as HTMLSelectElement).value);
        currentDate.setFullYear(newYear);
    }

    // Reactive statements
    $: selectedMonth = currentDate.getMonth();
    $: selectedYear = currentDate.getFullYear();
    $: totalDays = daysInMonth(currentDate);
    $: firstDay = firstDayOfMonth(currentDate);
    $: calendarDays = Array.from({ length: totalDays }, (_, i) => i + 1);
    $: emptyStartDays = Array.from({ length: firstDay }, (_, i) => null);
    $: allDays = [...emptyStartDays, ...calendarDays];
    $: weeks = Array.from({ length: Math.ceil(allDays.length / 7) }, (_, i) => 
        allDays.slice(i * 7, (i + 1) * 7)
    );
</script>

<div class="calendar-wrapper">
    <div class="dropdown-group">
        <select id="group-select" class="group-dropdown" bind:value={selectedGroup}>
            <option value="">Select a group</option>
            <option value="group1">Group 1</option>
            <option value="group2">Group 2</option>
            <option value="group3">Group 3</option>
        </select>
    </div>

    <div class="calendar-container">
        <div class="calendar-header">
            <div class="dropdown-container">
                <select 
                    class="month-dropdown"
                    bind:value={selectedMonth}
                    on:change={handleMonthChange}
                >
                    {#each months as month, i}
                        <option value={i}>{month}</option>
                    {/each}
                </select>
  
                <select 
                    class="year-dropdown"
                    bind:value={selectedYear}
                    on:change={handleYearChange}
                >
                    {#each years as year}
                        <option value={year}>{year}</option>
                    {/each}
                </select>
            </div>
        </div>
  
        <table class="calendar-table">
            <thead>
                <tr>
                    {#each days as day}
                        <th>{day}</th>
                    {/each}
                </tr>
            </thead>
            <tbody>
                {#each weeks as week}
                    <tr>
                        {#each week as day}
                            <td class="calendar-day">
                                {day || ''}
                            </td>
                        {/each}
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
</div>

<style>
    .calendar-wrapper {
    display: flex;
    flex-direction: column; /* Stack items vertically */
    align-items: center; /* Align items to the left */
    margin: 3rem auto; /* Reduce top margin to lift the calendar up */
    padding: 0 1rem;
}

.calendar-container {
    width: 100%; /* Full width for the calendar */
    max-width: 1000px; /* Control the max width */
    padding: 2rem;
    background: white;
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.25); /* Add shadow */
    margin-top: 0; /* Remove any top margin if it exists */
}

.dropdown-group {
    margin-bottom: 2rem; /* Space between dropdown and calendar */
    display: flex;
    flex-direction: column; /* Stack label and dropdown vertically */
    align-items: flex-start; /* Align items to the left */
    width: 100%; /* Make it full width */
    margin-left: 180px; /* Adjust this value to move it right */
}

.calendar-header {
    margin-bottom: 2rem;
}

.dropdown-container {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 1rem;
}

/* Shared styles for all dropdowns */
select {
    padding: 0.75rem 1.5rem;
    font-size: 1.2rem;
    border: 2px solid #d3d3d3; /* Light grey border */
    border-radius: 8px;
    background-color: #26796c; /* Dropdown background */
    color: white; /* Text color */
    cursor: pointer;
    outline: none;
    transition: all 0.2s;
    -webkit-appearance: none; /* Remove default arrow */
    -moz-appearance: none;
    appearance: none; /* Remove default styling */
    position: relative; /* For positioning the custom arrow */
}

/* Hover and focus styles for all dropdowns */
select:hover {
    background-color: rgba(38, 121, 108, 0.8); /* Darken on hover */
}

select:focus {
    background-color: #3a9b85; /* Darker shade on focus */
    color: white; /* Ensure text remains white */
    box-shadow: 0 0 0 2px rgba(38, 121, 108, 0.4); /* Focus shadow */
}

/* Specific styles for dropdowns */
.month-dropdown {
    min-width: 140px;
}

.year-dropdown {
    min-width: 100px;
}

.group-dropdown {
    min-width: 200px; /* Adjust width as needed */
}

.calendar-table {
    width: 100%;
    border-collapse: collapse;
}

th {
    padding: 1.5rem;
    color: #26796c;
    font-weight: 500;
    text-align: center;
    font-size: 1.2rem;
}

.calendar-day {
    padding: 1.5rem;
    text-align: center;
    cursor: pointer;
    transition: background-color 0.2s;
    font-size: 1.1rem;
    height: 2rem;
    vertical-align: middle;
}

.calendar-day:hover {
    background-color: rgba(38, 121, 108, 0.1);
}

/* Custom dropdown arrow styling */
select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2210%22%20height%3D%2210%22%20viewBox%3D%220%200%2010%2010%22%3E%3Cpath%20fill%3D%22white%22%20d%3D%22M0%200%20L10%200%20L5%205%20Z%22%2F%3E%3C%2Fsvg%3E");
    background-repeat: no-repeat;
    background-position: right 0.7rem top 50%;
    background-size: 0.65rem auto;
    padding-right: 2.5rem;
}

</style>

