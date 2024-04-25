// static/blog.js

// Function to fetch blog posts from the server and display them dynamically
function fetchAndDisplayBlogPosts() {
    // Fetch blog posts from the server using AJAX or fetch API
    // Example:
    fetch('/api/blog-posts')
        .then(response => response.json())
        .then(data => {
            // Display blog posts dynamically
            const blogContainer = document.querySelector('.blog-container');
            data.forEach(post => {
                const postElement = document.createElement('div');
                postElement.classList.add('blog-post');
                postElement.innerHTML = `
                    <h3>${post.title}</h3>
                    <p>${post.content}</p>
                `;
                blogContainer.appendChild(postElement);
            });
        })
        .catch(error => console.error('Error fetching blog posts:', error));
}

// Call the function when the page is loaded
window.addEventListener('load', fetchAndDisplayBlogPosts);
