// hamburger = document.querySelector(".hamburger");
// hamburger.onclick = function () {
//     navBar = document.querySelector(".div-nav");
//     navBar.classList.toggle("active");
// }

document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.querySelector(".hamburger");
    if (hamburger) {
        hamburger.onclick = function () {
            const navBar = document.querySelector(".div-nav");
            if (navBar) {
                navBar.classList.toggle("active");
            }
        }
    }
});