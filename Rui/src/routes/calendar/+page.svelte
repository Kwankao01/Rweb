<script>
    let currentDate = new Date();
    
    const months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];
  
    const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    
    // Generate array of years from 2024 to 2029
    const years = Array.from({ length: 6 }, (_, i) => 2024 + i);
  
    function daysInMonth(date) {
        return new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    }
  
    function firstDayOfMonth(date) {
        return new Date(date.getFullYear(), date.getMonth(), 1).getDay();
    }
  
    function handleMonthChange(event) {
        const newMonth = parseInt(event.target.value);
        currentDate.setMonth(newMonth);
    }
  
    function handleYearChange(event) {
        const newYear = parseInt(event.target.value);
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
        margin: 5rem auto 5rem;  
        padding: 0 1rem;
    }
  
    .calendar-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 2rem;
        background: white;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.14); /* หลังสุดคือเบลอ */
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
  
    select {
        padding: 0.75rem 1.5rem;
        font-size: 1.2rem;
        border: 2px solid #26796c;
        border-radius: 8px;
        background-color: white;
        color: #26796c;
        cursor: pointer;
        outline: none;
        transition: all 0.2s;
    }
  
    select:hover {
        background-color: rgba(38, 121, 108, 0.1);
    }
  
    select:focus {
        box-shadow: 0 0 0 2px rgba(38, 121, 108, 0.2);
    }
  
    .month-dropdown {
        min-width: 140px;
    }
  
    .year-dropdown {
        min-width: 100px;
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

    /* Custom dropdown styling */
    select {
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%2326796c%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E");
        background-repeat: no-repeat;
        background-position: right 0.7rem top 50%;
        background-size: 0.65rem auto;
        padding-right: 2.5rem;
    }
</style>
