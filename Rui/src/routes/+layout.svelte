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
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }

        nav {
            display: flex;
            justify-content: center;
            margin-bottom: 10px;
            gap: 10px;
            position: relative;
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
            max-width: 50px;
            height: auto;
            vertical-align: middle;
            margin-right: 10px;
        }

        /* New styles for dropdown */
        .dropdown {
            position: relative;
            display: inline-block;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
            border-radius: 5px;
            top: 100%;
        }

        .dropdown-content a {
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
            margin: 0;
            border-radius: 0;
        }

        .dropdown-content a:hover {
            background-color: #f1f1f1;
        }

        .dropdown:hover .dropdown-content {
            display: block;
        }

        .dropdown:hover #group {
            background-color: #26796c;
            color: #fff;
        }
    </style>
</head>

<body>
    <div class="header">
        <img src="Rlogo.png" alt="Logo" class="logo">
        <h1 style="font-size: 36px; font-weight: bold;">Route Ready</h1>
    </div>

    <nav>
        <a href="/" id="home">Home</a>
        <a href="/trip" id="trip">Trip</a>
        <a href="/calendar" id="calendar">Calendar</a>
        <a href="/hotel" id="hotel">Hotel</a>
        <a href="/restaurant" id="restaurant">Restaurant</a>
        <a href="/landmark" id="landmark">Landmark</a>
        <a href="/transportation" id="transportation">Transportation</a>
        <div class="dropdown">
            <a href="#" id="group">Group ▼</a>
            <div class="dropdown-content">
                <a href="/group-create">Create Group</a>
                <a href="/group-join">Join Group</a>
                <a href="/group-all">My Groups</a>
                <a href="/group-settings">Group Settings</a>
            </div>
        </div>
        <a href="/profile" id="profile">Account</a>
    </nav>

    <slot></slot>

    <script>
        function setActiveLink() {
            const currentPath = window.location.pathname;
            document.querySelectorAll('nav a').forEach(a => a.classList.remove('active'));
            document.querySelectorAll('nav a').forEach(a => {
                if (a.getAttribute('href') === currentPath) {
                    a.classList.add('active');
                }
            });
        }

        window.onload = setActiveLink;
    </script>
</body>
</html>


