<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickable Boxes with Images</title>
    <style>
        body {
            font-family: Arial, sans-serif; /* Font for better appearance */
            background-color: #ffffff; /* White background */
            margin: 0; /* Remove default margin */
            padding: 2rem; /* Add some padding */
        }

        h1 {
            text-align: center; /* Center the header */
            color: #26796c; /* Header color */
            margin-bottom: 2rem; /* Space below the header */
        }

        .box {
            width: 1000px; 
            height: 200px; 
            margin: 1rem auto; /* Center boxes with margin */
            padding: 1rem; 
            border-radius: 8px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); /* Softer shadow */
            text-align: left; /* Align text to the left */
            text-decoration: none;
            color: #000;
            display: flex; /* Use flexbox for layout */
            transition: transform 0.2s ease, box-shadow 0.2s ease; /* Smooth transitions */
            overflow: hidden; /* Prevent content overflow */
        }

        .box img {
            width: 50%; /* Responsive images */
            height: 100%; /* Maintain aspect ratio */
            border-radius: 8px 0 0 8px; /* Rounded corners on the left */
            object-fit: cover; /* Ensure image covers the space */
        }

        .box-content {
            padding: 1rem; /* Add some padding */
            display: flex;
            flex-direction: column; /* Stack text vertically */
            justify-content: center; /* Center content vertically */
            background-color: #f8f8f8; /* Light gray background for content */
            flex: 1; /* Allow content to fill remaining space */
            border-radius: 0 8px 8px 0; /* Rounded corners on the right */
        }

        .trip-name {
            font-size: 2rem; /* Bigger font for trip name */
            font-weight: bold; /* Make it bold */
            color: #26796c; /* Trip name color */
            margin-bottom: 0.5rem; /* Space below the trip name */
        }

        .small-text {
            font-size: 0.9rem; /* Slightly smaller text */
            color: #555; /* Dark gray color for contrast */
        }

        .box:hover {
            transform: scale(1.03); /* Slightly smaller scale effect */
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2); /* Darker shadow on hover */
        }

        .box-container {
            display: flex;
            justify-content: center;
            gap: 20px; /* Space between boxes */
            flex-wrap: wrap; /* Allow wrapping to next line */
        }
    </style>
</head>
<body>
    <h1>All Trips</h1>
    <div class="box-container">
        <a href="/trip" class="box">
            <img src="/samui.jpg" alt="Samui Trip">
            <div class="box-content">
                <div class="trip-name">Samui</div>
                <div class="small-text">Duration: 5 days</div>
                <div class="small-text">Countdown: 10 days</div>
            </div>
        </a>
    </div>    
</body>
</html>

