$(document).ready(function () {
    // Open mobile menu
    $('#menu-icon').on('click', function () {
        $('#mobile-menu').addClass('active');
        $('.overlay').addClass('active');
        $('.close').addClass('active');
    });

    // Close mobile menu
    $('.close, .overlay').on('click', function () {
        $('#mobile-menu').removeClass('active');
        $('.overlay').removeClass('active');
        $('.close').removeClass('active');
    });

    // Close menu on ESC key
    $(document).on('keydown', function(e) {
        if (e.key === "Escape") {
            $('#mobile-menu').removeClass('active');
            $('.overlay').removeClass('active');
            $('.close').removeClass('active');
        }
    });
});