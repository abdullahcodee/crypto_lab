// app/auth/static/js/sign_up.js

$(document).ready(function() {
    // Function to handle form submission
    $('#signUpForm').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: '/sign-up',
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
