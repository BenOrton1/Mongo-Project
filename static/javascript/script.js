$(document).ready(function () {
    $(".allergen-form").hide();
    $(".cuisine_form").hide();

    console.log('this');
    $("#search-Allergens").click(function () {
        $(".allergen-form").show(1000, "linear");
        $(".name-form").hide(1000, "linear"); 
        $(".cuisine_form").hide(1000, "linear");
    });

    $("#search-name").click(function () {
        $(".cuisine_form").hide(1000, "linear");
        $(".allergen-form").hide(1000, "linear");
        $(".name-form").show(1000);
    });

    $("#search-cuisine").click(function () {
        $(".cuisine_form").show(1000, "linear");
        $(".allergen-form").hide(1000, "linear");
        $(".name-form").hide(1000, "linear");
    });

    $(".update-name").hide();
    console.log('this');
    $(".update-name-button").click(function () {
        $(".update-name").show(1000, "linear");
        $(".name").hide(1000, "linear");
    });
});