// DarkMode
document.addEventListener("DOMContentLoaded", function () {
    const toggleSwitch = document.getElementById("filter");
    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
        toggleSwitch.checked = true;
    }
    toggleSwitch.addEventListener("change", function () {
        if (this.checked) {
            document.body.classList.add("dark-mode");
            localStorage.setItem("darkMode", "enabled"); // Seçimi yadda saxla
        } else {
            document.body.classList.remove("dark-mode");
            localStorage.setItem("darkMode", "disabled"); // Seçimi yadda saxla
        }
    });
});
// headerSlider
$('.headerSlider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    infinite: true,
    dots: false,
    arrows: false,
    speed:5000,
    pauseOnHover: false,
});
// btnToTop
let mybutton = document.getElementById("myBtn");
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}