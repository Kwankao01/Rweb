import { writable } from 'svelte/store';

export const isLoggedIn = writable(false); // Default: Not logged in
