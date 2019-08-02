#A Bad Cookbook
 
This is a project to made using flask and mongoDB to allow people to look up and share recipes. 
 
##UX
I used a basic mockup to guide how i built this project. 

![wireframe of homepage](static\images\mockup.png)


I wanted to users to be able to easily search for recipes so I added a search function at the top 
of the homepage with options to search by name, cuisine or without certain allergens. 


I also wanted users to be able to find new recipes easily. I added a section on the homepage that contains the most recent recipes added to the database. 

I wanted users to be able to add their own recipes easily and originally planned on having user add all the information on one page as seen in the basic wireframe below. This was changed to several pages each asking for a seperate part of the recipe making it simpler and cleaner looking. This also had the advantage of letting users enter part of a recipe, then editing the recipe later to add more information.

![wireframe of add recipies](static\images\mockup2.png)



##Features

Search Bar - The search bar on the homepage allows users to search for recipes by name or allergen and a dropdown menu allows users to search by cuisine. 

Add recipe - going through the add recipe wizard allows users to add their own recipes one stage at a time. Starting with a name description and cuisine, then ingredients, then the method and finally any allergy advice. 

Edit recipes - by selecting a recipe the user is given the option to edit the individual aspects of the recipe. 

Features Left to Implement

Login form and users - allow users to log in and only edit recipes they have added.

##Technologies Used


[JQuery](https://jquery.com/) - The project uses JQuery to simplify DOM manipulation.

[Bootstrap](https://getbootstrap.com/) - To easily get the foundations of the design in place.

[Flask](https://www.fullstackpython.com/flask.html) - To interact with mongoDB and to handle routing on the site.

[MongoDB](https://www.mongodb.com/) - The Database used to store the recipes.


##Testing

All links on the page have been tested and work. 

All forms hove been tested to add recipies. all forms work and are easy to follow. When a name that is already being used is entered the correct error is displayed. when nothing is entered the correct error is also displayed. 

All forms have been tested to edit the recipie and all work correctly. 

a css validator was used and found no errors (https://validator.w3.org/)

a bug was found in the routing for edit methourd. the routing was updated. 

a bug was found in the javascript for the search bars on the homepage, show and hide were the wrong way round. 

A bug was found when editing the recipie name, when the name was updated it removed the rest of the recipie. this was fixed by using $set so it only updated that part of the recipie.



##Deployment
 
Website is deployed through Heroku pages https://recipes-data-project.herokuapp.com/

##how to deploy locally 

the following must be installed 

pip
python 3
Git

Save the project locally or use the git clone command to clone this project. 
install all the reqirements using "pip -r requirements.txt"

set up a mongoDB account and a databace named recipes (if you do not want the databace named recipies you will need to update line 16 in recipies.py "recipes = mongo.db.recipes")

update line 11 of recipes.py "app.config["MONGO_URI"] = 'your mongodb Connection String goes here'" or you can update the enviroment variables in your IDE.


Credits

Content
images taken from 
https://www.digitalartsonline.co.uk/features/illustration/how-draw-food-20-tips-from-leading-illustrators/

https://moaniecat.tumblr.com/
