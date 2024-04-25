// app/static/js/admin.js

// Function to handle toggling of navbar collapse
function toggleNavbar() {
    var navbar = document.getElementById('navbarNav');
    if (navbar.classList.contains('show')) {
        navbar.classList.remove('show');
    } else {
        navbar.classList.add('show');
    }
}

// Add event listener to navbar toggler button
document.getElementById('navbar-toggler').addEventListener('click', toggleNavbar);
