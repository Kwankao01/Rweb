<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickable Boxes with Images</title>
    <style>
        .box {
            max-width: 300px;
            margin: 2rem;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.13);
            text-align: center;
            text-decoration: none;
            color: #000;
            transition: transform 0.2s ease;
        }

        .box img {
            width: 100%;
            height: auto;
            border-radius: 5px;
            margin-bottom: 1rem;
        }

        .box:hover {
            transform: scale(1.05);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
        }

        .box-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }
    </style>
</head>
<body>

    <div class="box-container">
        <a href="/group/group-all/group1" class="box">
            <img src="/g1.jpeg" alt="Group 1">
            <div>Group 1</div>
        </a>
        <a href="/group/group-all/group2" class="box">
            <img src="/g2.jpeg" alt="Group 2">
            <div>Group 2</div>
        </a>
    </div>    

</body>

