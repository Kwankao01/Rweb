export async function login(username, password){
    const response = await fetch('/api/login',{
        method: 'POST',
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify({ username, password })
    })
}