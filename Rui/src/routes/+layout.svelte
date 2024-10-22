<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Link Color on Click</title>
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
          transition: background-color 0.3s;
        }

        nav a:hover {
          background-color: #ddd; /* เปลี่ยนสีพื้นหลังเมื่อ hover */
        }

        nav a.active {
          background-color: #00f; /* สีพื้นหลังเมื่ออยู่ในหน้า active */
          color: #fff; /* สีตัวอักษรเมื่ออยู่ในหน้า active */
        }
    </style>
</head>
<body>

<nav>
    <a href="/" id="home">Home</a>
    <a href="/trip" id="trip">Trip</a>
    <a href="/calendar" id="calendar">Calendar</a>
    <a href="/hospitallity" id="hospitallity">Hospitallity</a>
    <a href="/restaurant" id="restaurant">Restaurant</a>
    <a href="/landmark" id="landmark">Landmark</a>
    <a href="/transportation" id="transportation">Transportation</a>
    <a href="/group" id="group">Group</a>
    <a href="/account" id="account">Account</a>
</nav>

<slot></slot>

<p>Have a nice trip!</p>

<script>
  // ฟังก์ชันที่จะตรวจสอบ URL และเพิ่มคลาส active ให้ลิงก์ที่ตรงกัน
  function setActiveLink() {
    // ดึง URL ปัจจุบัน
    const currentPath = window.location.pathname;
    
    // ลบคลาส active ออกจากลิงก์ทั้งหมดก่อน
    document.querySelectorAll('nav a').forEach(a => a.classList.remove('active'));

    // เพิ่มคลาส active ให้กับลิงก์ที่ตรงกับ URL ปัจจุบัน
    document.querySelectorAll('nav a').forEach(a => {
      if (a.getAttribute('href') === currentPath) {
        a.classList.add('active');
      }
    });
  }

  // เรียกใช้งานฟังก์ชันเมื่อโหลดหน้าเสร็จ
  window.onload = setActiveLink;
</script>

</body>
</html>
