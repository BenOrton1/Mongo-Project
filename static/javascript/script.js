$(document).ready(function () {
    $(".allergen-form").hide();
    console.log('this');
    $("#search-Allergens").click(function () {
        $(".allergen-form").hide("slow");
        $(".name-form").show("slow");
    });

    $("#search-name").click(function () {
        $(".allergen-form").show("slow");
        $(".name-form").hide("slow");
    });
});