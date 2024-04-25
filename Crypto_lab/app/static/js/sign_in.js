// app/auth/static/js/sign_in.js

$(document).ready(function() {
    // Function to handle form submission
    $('#signInForm').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: '/sign-in',
            data: formData,
            success: function(response) {
                // Handle success response
                console.log(response);
            },
            error: function(xhr, status, error) {
                // Handle error response
                console.error(xhr.responseText);
            }
        });
    });
});
