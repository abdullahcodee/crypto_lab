// common.js

// Function to handle form submission
function handleFormSubmission(formId, endpoint) {
    $(formId).submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: endpoint,
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
}

// Function to toggle visibility of form fields based on selected method
function toggleFieldsVisibility(methodId, keyFieldId, shiftFieldId) {
    $(methodId).change(function() {
        var selectedMethod = $(this).val();
        if (selectedMethod === 'caesar') {
            $(keyFieldId).hide();
            $(shiftFieldId).show();
        } else {
            $(keyFieldId).show();
            $(shiftFieldId).hide();
        }
    });
}
