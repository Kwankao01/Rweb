<div style="text-align: center; ; margin-top: 20px">
    <h1 style="font-size: 46px; font-weight: bold;">Explore places</h1>
</div>

<style>
    /* Search bar styling */
    .search-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }

    .search-input {
        padding: 10px 20px;                  /* ขนาดของ padding ให้กลมขึ้น */
        border: 1px solid #ccc;
        border-radius: 30px;                 /* เพิ่มความกลม */
        font-size: 18px;                     /* เพิ่มขนาดฟอนต์ */
        width: 800px;                        /* เพิ่มความกว้าง */
        max-width: 100%;                     /* ให้ปรับตามขนาดหน้าจอ */
        transition: width 0.3s ease;         /* เอฟเฟกต์การขยาย */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* เพิ่มเงา */
    }

    .search-button {
        margin-left: -40px;                  /* ปรับตำแหน่งให้ตรงกับ input */
        background: none;
        border: none;
        cursor: pointer;
        color: #26796c;
        font-size: 18px;
    }

    .centered-figure {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }

    .button {
        position: absolute;
        top: 160px;
        left: 30%;
        transform: translateX(-50%);
        padding: 15px 30px;
        background-color: #ffffff;
        color: #4c4c4c;
        text-decoration: none;
        border-radius: 30px;
        font-size: 22px;
        transition: background-color 0.3s;
        z-index: 0;
    }

    .button:hover {
        background-color: #d0d0d0;
    }

    .button i {
        margin-right: 10px;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        .search-input {
            width: 90%;                    /* ลดความกว้างบนหน้าจอเล็ก */
        }

        .button {
            top: 140px;
            font-size: 18px;
            padding: 10px 25px;
        }

        .centered-figure img {
            width: 90%;                   /* ลดขนาดรูปบนหน้าจอเล็ก */
        }
    }
</style>

<div class="search-container">
    <input type="text" class="search-input" placeholder="Destination...">
    <button class="search-button"><i class="fas fa-search"></i></button>
</div>
<p>Landmark List</p>