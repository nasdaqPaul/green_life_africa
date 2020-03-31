$(document).ready(function () {
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    });

    $('.parallax').parallax();

    $('.materialboxed').materialbox();

    $('.sidenav').sidenav();

    $('.slider').slider({
        indicators: false
    });

    $('.collapsible').collapsible();
});