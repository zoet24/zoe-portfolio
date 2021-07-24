let sidebarOpen = true;

function sidebarToggle() {
    if (sidebarOpen == true) {
        document.getElementById("sidebar").style.left = "-400px";
        document.getElementById("sidebar-toggle-arrow").style.transform = "rotate(180deg)";
        sidebarOpen = false;
    } else if (sidebarOpen == false) {
        document.getElementById("sidebar").style.left = "0px";
        document.getElementById("sidebar-toggle-arrow").style.transform = "rotate(0deg)";
        sidebarOpen = true;
    }
}