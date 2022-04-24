const createFooter = () => {
    let footer = document.querySelector('footer');

    footer.innerHTML= ` <div class="footer-content">
    <img src="public/img/light-logo.png" class="logo" alt="">
    <div class= "footer-ul-container">
        <ul class="category">
            <li class="category-title">Mens</li>
            <li><a href="http://#" class = "footer-link">T-Shirts</a></li>
            <li><a href="http://#" class = "footer-link">Sweatshirts</a></li>
            <li><a href="http://#" class = "footer-link">Shirts</a></li>
            <li><a href="http://#" class = "footer-link">Jeans</a></li>
            <li><a href="http://#" class = "footer-link">Trousers</a></li>
            <li><a href="http://#" class = "footer-link">Shoes</a></li>
            <li><a href="http://#" class = "footer-link">Casuals</a></li>
            <li><a href="http://#" class = "footer-link">Formals</a></li>
            <li><a href="http://#" class = "footer-link">Sports</a></li>
            <li><a href="http://#" class = "footer-link">Watches</a></li>
            </ul>
         <ul class="category">
                <li class="category-title">Womens</li>
                <li><a href="http://#" class = "footer-link">T-Shirts</a></li>
                <li><a href="http://#" class = "footer-link">Sweatshirts</a></li>
                <li><a href="http://#" class = "footer-link">Shirts</a></li>
                <li><a href="http://#" class = "footer-link">Jeans</a></li>
                <li><a href="http://#" class = "footer-link">Trousers</a></li>
                <li><a href="http://#" class = "footer-link">Shoes</a></li>
                <li><a href="http://#" class = "footer-link">Casuals</a></li>
                <li><a href="http://#" class = "footer-link">Formals</a></li>
                <li><a href="http://#" class = "footer-link">Sports</a></li>
                <li><a href="http://#" class = "footer-link">Watches</a></li>
                </ul>
    </div>
    
</div>
<p class="footer-title"> About Company</p>
    <p class="info">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce porttitor non libero ac tempus. Pellentesque tincidunt eros diam, vel tincidunt orci tincidunt non. Proin a consequat est, quis tincidunt eros. Pellentesque ac auctor sem. Vivamus mi urna, convallis vitae bibendum ut, tempor sit amet magna. Nunc sed luctus purus. In mollis sollicitudin ullamcorper. Integer pulvinar elit nec est bibendum varius.
    </p>
    <p class="info"> support emails - dynamic@clothing.com,
        customersupport@clothing.com
    </p>
    <p class="info"> telephone - 00 1234567890, 00 9841234567</p>
   <div class="footer-social-container">
       <div>
           <a href ="#" class="social-link">terms and Conditions</a>
           <a href ="#" class="social-link">privacy page</a>
       </div>
       <div>
        <a href ="#" class="social-link">instagram</a>
        <a href ="#" class="social-link">facebook</a>
        <a href ="#" class="social-link">twitter</a>
    </div>
   </div> 
   <p class="footer-credit"> Clothing, Best fashion Collection of All Time</p>`;
}

createFooter();