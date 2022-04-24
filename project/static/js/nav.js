const createNav =() => {
    let nav = document.querySelector('.navbar');

    nav.innerHTML =`

    <div class="nav">
    <img src="{%static 'img/dark-logo.png'%}" class="brand-logo" alt="">
    <div class="nav-items">
        <div class= "search">
            <input type="text" class= "search-box" placeholder="Search Brand, Product">
            <button class="search-btn">Search</button>
        </div>
          <a href="#"><img src= "{%static 'img/user.png'%}" alt=""></a>
          <a href="#"><img src="{%static 'img/cart.png'%}" alt=""></a>
    </div>
</div>
<ul class ="links-container">
    <li class="link-item"><a href="{%url 'index' %}" class="link">Home</a></li>
    <li class="link-item"><a href="#" class="link">Women</a></li>
    <li class="link-item"><a href="#" class="link">Men</a></li>
    <li class="link-item"><a href="#" class="link">Kids</a></li>
    <li class="link-item"><a href="#" class="link">Accessories</a></li>
</ul>
    `

}

createNav();