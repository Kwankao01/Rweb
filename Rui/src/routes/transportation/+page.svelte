<head>
    <div style="text-align: center; margin-top: 20px">
        <h1 style="font-size: 46px; font-weight: bold;">Find Flights</h1>
    </div>
    <style>
        /* Search bar styling */
        .search-container {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 10px;
        }

        .search-input, .date-input {
            padding: 10px 20px;
            border: 1px solid #ccc;
            border-radius: 30px;
            font-size: 18px;
            width: 250px;
            max-width: 100%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .search-button {
            margin-left: -40px;
            background: none;
            border: none;
            cursor: pointer;
            color: #26796c;
            font-size: 18px;
        }

        /* Flight list styling */
        .flight-selection {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        .flight-selection h2 {
            font-size: 1.8rem;
            color: #26796c;
            margin-bottom: 20px;
            text-align: center;
        }

        .flight-list {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .flight-card {
            display: flex;
            align-items: center;
            padding: 15px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            cursor: pointer;
            transition: transform 0.2s;
        }

        .flight-card:hover {
            transform: scale(1.02);
        }

        .flight-image {
            width: 120px;
            height: 90px;
            border-radius: 8px;
            object-fit: cover;
            margin-right: 15px;
        }

        .flight-info h3 {
            font-size: 1.5rem;
            color: #26796c;
            margin: 0;
        }

        .flight-info p {
            color: #555;
            margin: 5px 0;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>Find Flights</h1>
    </div>

    <!-- Flight search container -->
    <div class="search-container">
        <input type="text" class="search-input" placeholder="Departure city" id="departure">
        <input type="text" class="search-input" placeholder="Arrival city" id="arrival">
        <input type="date" class="date-input" id="flight-date">
        <button class="search-button" onclick="searchFlights()">Search</button>

    </div>

    <section class="flight-selection">
        <h2>Available Flights</h2>
        <div id="flight-list" class="flight-list">
            <!-- Flight results will be injected here -->
        </div>
    </section>

    <script>
        // Sample flight data
        const flights = [
            {
                id: 1,
                airline: "AirAsia",
                image: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/AirAsia_New_Logo.svg/1200px-AirAsia_New_Logo.svg.png",
                price: 1450,
                route: "Don Mueang - Chiang Mai",
                departureCity: "Don Mueang",
                arrivalCity: "Chiang Mai",
                departureTime: "06:00 AM",
                arrivalTime: "07:55 AM",
                date: "2024-12-01"
            },
            {
                id: 2,
                airline: "NokAir",
                image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbxVWAfKQKkb0BLbp9YS9N_IYB2CLtkOtsuw&s",
                price: 1000,
                route: "Don Mueang - Chiang Mai",
                departureCity: "Don Mueang",
                arrivalCity: "Chiang Mai",
                departureTime: "06:20 AM",
                arrivalTime: "07:25 PM",
                date: "2024-12-01"
            },
            {
                id: 3,
                airline: "AirAsia",
                image: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/AirAsia_New_Logo.svg/1200px-AirAsia_New_Logo.svg.png",
                price: 1450,
                route: "Don Mueang - Chiang Mai",
                departureCity: "Don Mueang",
                arrivalCity: "Chiang Mai",
                departureTime: "08:10 AM",
                arrivalTime: "09:30 AM",
                date: "2024-12-01"
            },
            {
                id: 4,
                airline: "NokAir",
                image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbxVWAfKQKkb0BLbp9YS9N_IYB2CLtkOtsuw&s",
                price: 1000,
                route: "Don Mueang - Chiang Mai",
                departureCity: "Don Mueang",
                arrivalCity: "Chiang Mai",
                departureTime: "09:20 PM",
                arrivalTime: "10:30 PM",
                date: "2024-12-01"
            },
            // More flights...
        ];

        // Function to search and display flights based on user input
        function searchFlights() {
            const departure = document.getElementById("departure").value;
            const arrival = document.getElementById("arrival").value;
            const date = document.getElementById("flight-date").value;

            // Filter flights based on input values
            const filteredFlights = flights.filter(flight => 
                flight.departureCity.toLowerCase() === departure.toLowerCase() &&
                flight.arrivalCity.toLowerCase() === arrival.toLowerCase() &&
                flight.date === date
            );

            // Display filtered flights
            const flightList = document.getElementById("flight-list");
            flightList.innerHTML = ""; // Clear previous results

            if (filteredFlights.length === 0) {
                flightList.innerHTML = "<p>No flights found for the selected route and date.</p>";
            } else {
                filteredFlights.forEach(flight => {
                    const flightCard = document.createElement("div");
                    flightCard.classList.add("flight-card");
                    flightCard.innerHTML = `
                        <img src="${flight.image}" alt="${flight.airline}" class="flight-image" />
                        <div class="flight-info">
                            <h3>${flight.airline}</h3>
                            <p>Price: ฿${flight.price}</p>
                            <p>Route: ${flight.route}</p>
                            <p>Departure: ${flight.departureTime} | Arrival: ${flight.arrivalTime}</p>
                        </div>
                    `;
                    flightList.appendChild(flightCard);
                });
            }
        }
    </script>

</body>
