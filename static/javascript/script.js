$(document).ready(function () {
    $(".allergen-form").hide();
    console.log('this');
    $("#search-Allergens").click(function () {
        $(".allergen-form").show(1000, "linear");
        $(".name-form").hide(1000, "linear");
    });

    $("#search-name").click(function () {
        $(".allergen-form").hide(1000, "linear");
        $(".name-form").show(1000);
    });


    $(".update-name").hide();
    console.log('this');
    $(".update-name-button").click(function () {
        $(".update-name").show(1000, "linear");
        $(".name").hide(1000, "linear");
    });
});