let sidebarOpen = true;

function sidebarToggle() {
    if (sidebarOpen == true) {
        document.getElementById("sidebar").style.left = "-400px";
        sidebarOpen = false;
    } else if (sidebarOpen == false) {
        document.getElementById("sidebar").style.left = "0px";
        sidebarOpen = true;
    }
}