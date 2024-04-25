// static/home.js

// Function to handle form submission
function handleSubmit(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get form data
    const formData = new FormData(event.target);
    const text = formData.get('text');
    const method = formData.get('method');
    const action = formData.get('action');
    let key, shift;

    // Get key or shift value based on the selected method
    if (method === 'caesar' || method === 'affine' || method === 'vigenere') {
        key = formData.get('key');
    }
    if (method === 'caesar') {
        shift = formData.get('shift');
    }

    // Construct the payload
    const payload = {
        text: text,
        method: method,
        action: action,
        key: key,
        shift: shift
    };

    // Send AJAX request to the server
    fetch('/process-cipher', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.text())
    .then(result => {
        // Display the result on the page
        document.getElementById('result').innerHTML = result;
    })
    .catch(error => console.error('Error:', error));
}

// Add event listener to the form submission
document.getElementById('cipherForm').addEventListener('submit', handleSubmit);
