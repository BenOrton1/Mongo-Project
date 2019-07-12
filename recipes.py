import os
import json
from flask import Flask, render_template, redirect, request, jsonify, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config['SECRET_KEY'] = 'tempPasswordChangeLater' 

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] =os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

"""access mongo db"""
recipes = mongo.db.recipes


"""homepage"""
@app.route('/')
@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    return render_template('recipes.html', 
                            recipe_find = recipes.find().sort('$natural', -1).limit(5))
                            
"""add ingredients to recepie"""
                            
@app.route('/add_ingredient/<this_recipe_name>', methods=['POST'])
def add_ingredient(this_recipe_name):
        recipes.find_one_and_update(
        {'recipe_name': this_recipe_name},
        {'$push':{'ingredient':request.form.get('ingredient').lower(),
        'weight':request.form.get('weight').lower()
        }})
        return render_template('add_ingredient.html',
        this_recipe = recipes.find_one({'recipe_name': this_recipe_name}))

@app.route('/add_method_page/<this_recipe_name>', methods=['GET','POST'])
def add_method_page(this_recipe_name):
    return render_template('method.html',
    this_recipe = recipes.find_one({'recipe_name':this_recipe_name}))
        
@app.route('/add_method/<this_recipe_name>', methods=['GET','POST'])
def add_method(this_recipe_name):
    recipes.find_one_and_update(
        {'recipe_name': this_recipe_name},
        {'$push':{'method':request.form.get('method')
        }})
    return render_template('method.html',
    this_recipe = recipes.find_one({'recipe_name':this_recipe_name}))
    
@app.route('/add_recipes')
def add_recipes():
    return render_template('add_recipes.html',
    this_recipe=recipes.find())
    

@app.route('/allergy/<this_recipe_name>', methods=['GET','POST'])
def allergy(this_recipe_name):
    recipes.find_one_and_update(
        {'recipe_name': this_recipe_name},
        {'$push':{'allergen':request.form.get('allergen')
        }})
    return render_template('allergy.html',
    this_recipe = recipes.find_one({'recipe_name':this_recipe_name}))

""" Delete recepie or cancel hald way though adding a new recepie"""
@app.route('/cancel/<recipe_id>', methods=['GET','POST'])
def cancel(recipe_id):
    recipes.remove({"_id": ObjectId(recipe_id)})
    return render_template('recipes.html', 
                            recipe_find = recipes.find())
"""edit"""                     
@app.route('/edit/<recipe_id>')
def edit(recipe_id):
    the_recipe = recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit.html', 
    this_recipe=the_recipe)

@app.route('/edit_ingredients/<recipe_id>')
def edit_ingredients(recipe_id):
    return render_template('edit_ingredients.html',
    this_recipe=recipes.find_one({"_id": ObjectId(recipe_id)})) 

""" Add a new recepie"""   
@app.route('/insertrecipe', methods=['GET','POST'])
def insertrecipes():
    name=request.form['recipe_name']
    if recipes.find_one({'recipe_name': name}):
        return render_template('add_recipes_already.html',
        this_recipe=recipes.find())
    else:
        recipes.insert_one(request.form.to_dict())
        return render_template('add_ingredient.html', 
        this_recipe_name = name,
        this_recipe = recipes.find_one({'recipe_name': name})
    )

@app.route('/one_recipe/<recipe_id>')
def one_recipe(recipe_id):
    the_recipe = recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('one_recipe.html', 
    this_recipe=the_recipe)

    
@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/search_recipe_name', methods=['GET','POST'])
def search_recipe_name():
    searched_name = request.form.get('search_recipe_name').lower()
    return render_template('searched_recipe.html', 
                    this_recipe = recipes.find({'recipe_name':{'$in': [searched_name]}}))


"""currnt work on search function"""
@app.route('/search_recipe', methods=['GET','POST'])
def search_recipe():
    searched_allergy = request.form.get('allergy')
    return render_template('searched_recipe.html', this_recipe=recipes.find({'allergen':{ '$nin':[searched_allergy]}}))
"""
searched_ingredient = request.form.get('ingreedient')
    searchedrecipe = recipes.find({'ingreedient':{'$in': [searched_ingredient]}})
    return render_template('searched_recipe.html', this_recipe=searchedrecipe)

elif searched_ingredient:
    
    searchedrecipe = recipes.find({'allergen':{ '$nin':[searched_allergy]}})
    elif searched_allergy:
        searchedrecipe = recipes.find({'allergen':{ '$nin':[searched_allergy]}})
"""


@app.route('/update_recipe/<recipe_id>', methods=['GET', 'POST'])
def update_recipe(recipe_id):
    recipes.update( {'_id': ObjectId(recipe_id)},
    {"$set":
        {
        'recipe_name':request.form.get('recipe_name')
        }
    }
    )
    return redirect(url_for('get_recipes'))

@app.route('/update_ingredience/<this_recipe_name>', methods=['GET', 'POST'])
def update_ingredience(this_recipe_name):
    recipes.update(
    {'recipe_name': this_recipe_name},
    {'ingredient':request.form.get('ingredient').lower(),
    'weight':request.form.get('weight').lower()
    })
    return render_template(url_for('edit_ingredients_update.html'),
                this_recipe = recipes.find_one({'recipe_name': this_recipe_name}))

@app.route('/update_ingredience_push/<this_recipe_name>', methods=['GET', 'POST'])
def update_ingredience_push(this_recipe_name):
    recipes.find_one_and_update(
    {'recipe_name': this_recipe_name},
    {'$push':{'ingredient':request.form.get('ingredient').lower(),
    'weight':request.form.get('weight').lower()
    }})
    return render_template(url_for('edit_ingredients_update.html'))

@app.errorhandler(404) 
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500) 
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)