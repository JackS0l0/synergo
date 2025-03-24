// DarkMode
document.addEventListener("DOMContentLoaded", function () {
    let desktopSwitch = document.getElementById("filter-desktop");
    let mobileSwitch = document.getElementById("filter-mobile");

    // Yadda saxlanmış rejimi yoxlayırıq
    let darkMode = localStorage.getItem("dark-mode") === "enabled";

    // Switch-ləri və body class-ı uyğun vəziyyətə gətiririk
    desktopSwitch.checked = darkMode;
    mobileSwitch.checked = darkMode;
    document.body.classList.toggle("dark-mode", darkMode);

    function syncSwitches(source, target) {
        target.checked = source.checked;
        document.body.classList.toggle("dark-mode", source.checked);

        // Dark mode rejimini yadda saxlayırıq
        localStorage.setItem("dark-mode", source.checked ? "enabled" : "disabled");
    }

    desktopSwitch.addEventListener("change", function () {
        syncSwitches(desktopSwitch, mobileSwitch);
    });

    mobileSwitch.addEventListener("change", function () {
        syncSwitches(mobileSwitch, desktopSwitch);
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
// whyMeBlockMob
$('.whyMeBlockMob').slick({
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