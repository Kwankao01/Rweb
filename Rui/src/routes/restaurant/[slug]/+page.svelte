<script>
    export let data;
</script>

<style>
    .restaurant-container {
        max-width: 800px; /* ความกว้างสูงสุด */
        margin: 0 auto; /* จัดกลาง */
        padding: 20px; /* เพิ่มช่องว่างรอบ ๆ */
        background-color: #f9f9f9; /* สีพื้นหลัง */
        border-radius: 8px; /* มุมกลม */
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* เงา */
    }

    h1 {
        font-size: 2.5em; /* ขนาดตัวอักษร */
        color: #333; /* สีตัวอักษร */
        text-align: center; /* จัดกลาง */
        margin-bottom: 20px; /* เพิ่มช่องว่างด้านล่าง */
    }

    .restaurant-image {
        width: 100%; /* ทำให้ภาพกว้างเต็มที่ */
        height: auto; /* ปรับความสูงอัตโนมัติ */
        border-radius: 8px; /* มุมกลม */
        margin-bottom: 20px; /* เพิ่มช่องว่างด้านล่าง */
    }

    .restaurant-details {
        font-size: 1.2em; /* ขนาดตัวอักษร */
        line-height: 1.6; /* ระยะห่างระหว่างบรรทัด */
        color: #555; /* สีตัวอักษร */
    }

    .rating {
        font-weight: bold; /* ทำให้ตัวอักษรหนา */
        color: #ff9800; /* สีสำหรับเรทติ้ง */
    }

    .location {
        font-style: italic; /* ตัวอักษรเอียง */
        color: #888; /* สีตัวอักษร */
    }
</style>

<div class="restaurant-container">
    <h1>{data.post.title}</h1>
    <img src={data.post.image} alt="{data.post.title}" class="restaurant-image" />
    <div class="restaurant-details">
        <div>{@html data.post.content}</div>
        <p class="rating">Rating: {data.post.rating} ({data.post.reviews} reviews)</p>
        <p class="city">City: {data.post.city}</p>
    </div>
</div>
