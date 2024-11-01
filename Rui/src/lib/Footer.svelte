<script>
    // Import any necessary icons or dependencies if needed.
</script>

<footer class="footer">
    <div class="footer-content">
        <!-- Contact Us Section -->
        <div class="footer-section">
            <h3>Contact Us</h3>
            <ul>
                <li><a href="/support">Customer Support</a></li>
                <li><a href="/service">Service Guarantee</a></li>
                <li><a href="/more-info">More Service Info</a></li>
            </ul>
            <div class="social-icons">
                <a href="#"><i class="fab fa-facebook-f"></i></a>
                <a href="#"><i class="fab fa-twitter"></i></a>
                <a href="#"><i class="fab fa-youtube"></i></a>
            </div>
        </div>

        <!-- About Section -->
        <div class="footer-section">
            <h3>About</h3>
            <ul>
                <li><a href="/about">About RouteReady.com</a></li>
                <li><a href="/news">News</a></li>
                <li><a href="/careers">Careers</a></li>
                <li><a href="/terms">Terms & Conditions</a></li>
                <li><a href="/privacy">Privacy Statement</a></li>
                <li><a href="/group">About RouteReady.com Group</a></li>
            </ul>
        </div>

        <!-- Other Services Section -->
        <div class="footer-section">
            <h3>Other Services</h3>
            <ul>
                <li><a href="/investors">Investor Relations</a></li>
                <li><a href="/rewards">Trip.com Rewards</a></li>
                <li><a href="/affiliate">Affiliate Program</a></li>
                <li><a href="/list-property">List Your Property</a></li>
                <li><a href="/all-hotels">All Hotels</a></li>
                <li><a href="/supplier">Become a Supplier</a></li>
                <li><a href="/security">Security</a></li>
            </ul>
        </div>

        <!-- Payment Methods Section -->
        <div class="footer-section payment-methods">
            <h3>Payment Methods</h3>
            <div class="payment-icons">
                <!-- Replace these with images or icons as needed -->
                <img src="Alipay.jpg" alt="Alipay">
                <img src="Visa.jpg" alt="Visa">
                <img src="MasterCard.jpg" alt="MasterCard">
                <img src="PayPal.jpg" alt="PayPal">
                

            </div>
        </div>

        <!-- Partners Section -->
        <div class="footer-section partners">
            <h3>Our Partners</h3>
            <div class="partner-logos">
                <img src="Google.jpg" alt="Google">
                <img src="TripAdvisor.png" alt="TripAdvisor">
            </div>
        </div>
    </div>
</footer>

<style>
    .footer {
        background-color: #f9f9f9;
        color: #26796c;
        padding: 30px 0;
    }

    .footer-content {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 20px;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }

    .footer-section h3 {
        font-size: 18px;
        margin-bottom: 10px;
        color: #26796c;
    }

    .footer-section ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .footer-section ul li {
        margin: 5px 0;
    }

    .footer-section ul li a {
        color: #333;
        text-decoration: none;
        font-size: 14px;
    }

    .footer-section ul li a:hover {
        text-decoration: underline;
    }

    .social-icons {
        display: flex;
        gap: 10px;
        margin-top: 10px;
    }

    .social-icons a {
        font-size: 20px;
        color: #4a4a4a;
        text-decoration: none;
    }

    .payment-methods .payment-icons {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 10px;
    }

    .payment-methods .payment-icons img {
        width: 40px;
        height: 30px;
        object-fit: contain;
    }

    .partners .partner-logos {
        display: flex;
        gap: 10px;
        margin-top: 10px;
    }

    .partners .partner-logos img {
        height: 30px;
    }

    @media (max-width: 768px) {
        .footer-content {
            grid-template-columns: 1fr;
        }

        .footer-section {
            text-align: center;
        }
    }
</style>
