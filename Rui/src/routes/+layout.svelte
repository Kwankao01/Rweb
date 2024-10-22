<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Route Ready</title>
    <style>

        .header {
            margin-left: 20px;
            margin-top: 10px;
            display: flex; /* ใช้ flexbox เพื่อให้โลโก้และข้อความอยู่ในบรรทัดเดียวกัน */
            align-items: center; /* จัดแนวให้กลางในแนวตั้ง */
            margin-bottom: 10px; /* ระยะห่างด้านล่าง */
        }

        nav {
            display: flex; /* ใช้ flexbox สำหรับจัดลิงก์ */
            justify-content: center; /* จัดกลางลิงก์ */
            margin-bottom: 10px; /* ระยะห่างด้านล่าง */
            gap: 10px; /* ระยะห่างระหว่างลิงก์ */
        }

        nav a {
            display: inline-block;
            padding: 5px 10px;
            margin: 5px;
            text-decoration: none;
            border-radius: 5px;
            background-color: #f0f0f0;
            color: #000;
        }

        nav a.active {
            background-color: #26796c; 
            color: #fff; 
        }

        .logo {
            max-width: 50px; /* กำหนดความกว้างสูงสุดของรูป */
            height: auto; /* ความสูงปรับอัตโนมัติตามสัดส่วน */
            vertical-align: middle; /* ให้แนวนอนของรูปอยู่ตรงกลาง */
            margin-right: 10px; /* ระยะห่างระหว่างรูปและข้อความ */
        }
    </style>

    
  <div class="header">
    <img src="Rlogo.png" alt="Logo" class="logo">
    <h1 style="font-size: 36px; font-weight: bold;">Route Ready</h1>
</div>

</head>


<body>

<nav>
    <a href="/" id="home">Home</a>
    <a href="/trip" id="trip">Trip</a>
    <a href="/calendar" id="calendar">Calendar</a>
    <a href="/hotel" id="hotel">Hotel</a>
    <a href="/restaurant" id="restaurant">Restaurant</a>
    <a href="/landmark" id="landmark">Landmark</a>
    <a href="/transportation" id="transportation">Transportation</a>
    <a href="/group" id="group">Group</a>
    <a href="/profile" id="profile">Account</a>
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
