
/* ==================================
   JobConnect - Frontend JavaScript
================================== */

// Automatically close flash messages
document.addEventListener("DOMContentLoaded", function () {

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {

        setTimeout(function () {

            if (typeof bootstrap !== "undefined") {
                const alertInstance =
                    bootstrap.Alert.getOrCreateInstance(alert);

                alertInstance.close();
            }

        }, 5000);

    });

});


// Confirm before deleting a user
function confirmDelete() {
    return confirm(
        "Are you sure you want to delete this user?"
    );
}


// Confirm before changing application status
function confirmStatusUpdate() {
    return confirm(
        "Do you want to update this application status?"
    );
}


// Job search form validation
document.addEventListener("DOMContentLoaded", function () {

    const searchForms = document.querySelectorAll(
        'form[action*="/jobs"]'
    );

    searchForms.forEach(function (form) {

        form.addEventListener("submit", function (event) {

            const searchInput =
                form.querySelector('input[name="search"]');

            const locationInput =
                form.querySelector('input[name="location"]');

            const searchValue = searchInput
                ? searchInput.value.trim()
                : "";

            const locationValue = locationInput
                ? locationInput.value.trim()
                : "";

            if (!searchValue && !locationValue) {
                // Empty search is allowed to show all jobs.
                return;
            }

        });

    });

});


// Display current year dynamically
document.addEventListener("DOMContentLoaded", function () {

    const yearElement = document.getElementById("current-year");

    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }

});
