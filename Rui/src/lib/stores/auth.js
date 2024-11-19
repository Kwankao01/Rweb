import { writable } from "svelte/store";

// Check if code is running in the browser
const isBrowser = typeof window !== "undefined";

const storedToken = isBrowser ? localStorage.getItem("token") : null;
const storedUserId = isBrowser ? localStorage.getItem("user_id") : null;

export const token = writable(storedToken);
export const userId = writable(storedUserId);

// Sync the store with localStorage (only in the browser)
if (isBrowser) {
  token.subscribe(value => {
    if (value) localStorage.setItem("token", value);
    else localStorage.removeItem("token");
  });

  userId.subscribe(value => {
    if (value) localStorage.setItem("user_id", value);
    else localStorage.removeItem("user_id");
  });
}
