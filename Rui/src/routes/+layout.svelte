<style>
    nav a {
      display: inline-block;
      padding: 10px 20px;
      margin: 5px;
      text-decoration: none;
      border: 2px solid #000; 
      border-radius: 5px; 
      background-color: #f0f0f0; 
      color: #000; 
    }
    
    nav a:hover {
      background-color: #ddd; /* เปลี่ยนสีพื้นหลังเมื่อ hover */
    }
  </style>
  
  <nav>
      <a href="/">Trip</a>
      <a href="/calendar">Calendar</a>
      <a href="/hospitallity">Hospitallity</a>
      <a href="/restaurant">Restaurant</a>
      <a href="/landmark">Landmark</a>
      <a href="/transportation">Transportation</a>
      <a href="/group">Group</a>
      <a href="/account">Account</a>
  </nav>
  
  <slot />
  
  <p> Have a nice trip! </p>
  