$(document).ready(function() {
    console.log('this');
    $("#search-Allergens").click(function(){
        const allergen = `<form class="search jumbotron-search col-xs-12 col-md-8" action="{{url_for('search_recipe')}}" method="POST"
        id="search_recipe">
        <input name="allergy" id="allergy" class="form-control form-control-lg" type="text"
            placeholder="search for recipes that without this allergen required">
        <button type="submit" class="btn btn-primary">search</button>
        <div class="row">
            <a class="white-text jumbotron-text" href="#recent_recipes">See New Recipes</a>
        </div>
    </form>`;
        $(".change-search").html(allergen);
    });

    $("#search-name").click(function(){
        const recepieName = `<form class="search jumbotron-search col-xs-12 col-md-8" action="{{url_for('search_recipe_name')}}"
        method="POST" id="search_recipe_names">
        <input name="search_recipe_name" id="search_recipe_name" class="form-control form-control-lg"
            type="text" placeholder="search recipe name" required>
        <button type="submit" class="btn btn-primary">search</button>
        <div class="row">
            <a class="white-text jumbotron-text" href="#recent_recipes">See New Recipes</a>
        </div>
    </form>`;
        $(".change-search").html(recepieName);
    });
});

