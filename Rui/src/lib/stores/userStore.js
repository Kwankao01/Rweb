import { writable } from 'svelte/store';

export const userStore = writable({
    id: "12345",
    name: "Taylor Swift",
    email: "taylor@example.com",
    profileImage: "taylor.jpg",
    birthdate: "1989-12-13",
    gender: "Female",
    address: "123 Ladprao, Bangkok, Thailand",
    phoneNumber: "+66 123 456 789"
});
