import { onMount } from 'svelte';
import { writable, derived, get } from 'svelte/store';
import { token, userId } from '$lib/stores/auth';
 
export function CalendarLogic() {
 const dayStore = writable(new Date());
 const events = writable({});
 const groups = writable([]);
 const selectedGroup = writable(null);
 const loading = writable(false);
 const error = writable('');
 const showConfirmModal = writable(false);
 const selectedDate = writable(null);
 const clickedCell = writable(null);
 const availabilityDates = writable({});
 const perfectMatchDates = writable([]);
 
 const DAYS_IN_WEEK = 7;
 const TODAY = new Date();
 
 const weeks = derived(dayStore, ($dayStore) => {
   const year = $dayStore.getFullYear();
   const month = $dayStore.getMonth();
   const firstDay = new Date(year, month, 1);
   const lastDay = new Date(year, month + 1, 0);
   
   let currentWeek = [];
   const allWeeks = [];
 
   for (let i = 0; i < firstDay.getDay(); i++) {
     currentWeek.push(null);
   }
 
   for (let day = 1; day <= lastDay.getDate(); day++) {
     currentWeek.push(new Date(year, month, day));
     
     if (currentWeek.length === DAYS_IN_WEEK) {
       allWeeks.push(currentWeek);
       currentWeek = [];
     }
   }
 
   while (currentWeek.length < DAYS_IN_WEEK) {
     currentWeek.push(null);
   }
   if (currentWeek.length > 0) {
     allWeeks.push(currentWeek);
   }
 
   return allWeeks;
 });
 
 function getDateString(date, separator = "-") {
   if (!date) return "";
   return [
     date.getFullYear(),
     String(date.getMonth() + 1).padStart(2, "0"),
     String(date.getDate()).padStart(2, "0")
   ].join(separator);
 }
 
 function changeMonth(by) {
   return () => {
     dayStore.update(current =>
       new Date(
         current.getFullYear(),
         current.getMonth() + by,
         current.getDate()
       )
     );
   };
 }
 
 async function fetchGroups() {
   try {
     loading.set(true);
     const response = await fetch('/api/groups', {
       headers: {
         'Authorization': `Bearer ${get(token)}`
       }
     });
 
     if (response.ok) {
       const data = await response.json();
       groups.set(data);
 
       if (get(selectedGroup)) {
         await fetchAvailability(get(selectedGroup));
       }
     } else {
       const errorData = await response.json();
       error.set(errorData.detail || 'Failed to fetch groups');
     }
   } catch (err) {
     error.set('Error fetching groups');
     console.error('Error:', err);
   } finally {
     loading.set(false);
   }
 }
 
 async function fetchAvailability(groupId) {
   if (!groupId) return;
 
   try {
     const response = await fetch(`/api/groups/${groupId}/available-dates/`, {
       headers: {
         'Authorization': `Bearer ${get(token)}`
       }
     });
 
     if (response.ok) {
       const data = await response.json();
       if (Array.isArray(data)) {
         perfectMatchDates.set(data.map(date => new Date(date)));
         const availableDatesObj = data.reduce((acc, date) => {
           acc[getDateString(new Date(date))] = true;
           return acc;
         }, {});
         availabilityDates.set(availableDatesObj);
       } else if (typeof data === 'string') {
         perfectMatchDates.set([]);
         availabilityDates.set({});
       }
     } else {
       error.set('Failed to fetch availability');
       perfectMatchDates.set([]);
     }
   } catch (err) {
     error.set('Error fetching availability');
     console.error('Error:', err);
     perfectMatchDates.set([]);
   }
 }
 
 selectedGroup.subscribe(async (groupId) => {
   if (groupId) {
     await fetchAvailability(groupId);
   } else {
     availabilityDates.set({});
     perfectMatchDates.set([]);
   }
 });
 
 function handleDateClick(date, event) {
   if (!date || !event || !event.currentTarget) return;
   
   clickedCell.set(event.currentTarget);
   const button = event.currentTarget;
   
   const circle = document.createElement("span");
   const diameter = Math.max(button.clientWidth, button.clientHeight);
   const radius = diameter / 2;
 
   circle.style.width = circle.style.height = `${diameter}px`;
   circle.style.left = `${event.clientX - button.offsetLeft - radius}px`;
   circle.style.top = `${event.clientY - button.offsetTop - radius}px`;
   circle.classList.add("ripple");
 
   const ripple = button.getElementsByClassName("ripple")[0];
   if (ripple) {
     ripple.remove();
   }
 
   button.appendChild(circle);
   selectedDate.set(date);
   showConfirmModal.set(true);
 }
 
 async function confirmAvailability() {
   const currentDate = get(selectedDate);
   if (!currentDate || !get(selectedGroup)) {
     error.set('Please select a group and date');
     return;
   }
 
   try {
     loading.set(true);
     const response = await fetch('/api/availability', {
       method: 'POST',
       headers: {
         'Authorization': `Bearer ${get(token)}`,
         'Content-Type': 'application/json'
       },
       body: JSON.stringify({
         group_id: get(selectedGroup),
         user_id: get(userId),
         date: [getDateString(currentDate)]
       })
     });
 
     if (response.ok) {
       availabilityDates.update(dates => ({
         ...dates,
         [getDateString(currentDate)]: true
       }));
       
       const button = get(clickedCell);
       if (button) {
         button.classList.add('success-pulse');
         setTimeout(() => {
           button.classList.remove('success-pulse');
         }, 1000);
       }
       
       await fetchAvailability(get(selectedGroup));
     } else {
       const errorData = await response.json();
       error.set(errorData.detail || 'Failed to add availability');
     }
   } catch (err) {
     error.set('Error adding availability');
     console.error('Error:', err);
   } finally {
     loading.set(false);
     showConfirmModal.set(false);
     selectedDate.set(null);
     clickedCell.set(null);
   }
 }
 
 function closeModal() {
   showConfirmModal.set(false);
   selectedDate.set(null);
   clickedCell.set(null);
 }
 
 return {
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
 };
}