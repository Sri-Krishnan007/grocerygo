document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded and parsed.");
    setTimeout(function() {
        var popup = document.getElementById("popupMessage");
        console.log("Displaying popup message.");
        if (popup) {
            popup.style.display = "block";
        } else {
            console.error("Popup message element not found!");
        }
    }, 10000); // Display popup after 10 seconds
});
