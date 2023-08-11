from flask import Flask,render_template, request
from meals_collection import mealCollection
import requests

response1 = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=")
all_meals_json = response1.json()
all_meals = mealCollection(all_meals_json["meals"])

app = Flask(__name__)
@app.route('/')
def home():
    meal_list = str(all_meals.display_all_meals_sorted())
    return HOME_HTML.format(meal_list)


@app.route('/meal', methods = ['POST'])
def meal():
    name = request.form['meal']
    meal_info = all_meals.info_about_meal(name)
    return MEAL_HTML.format(str(meal_info.name),str(meal_info.ingredients),str(meal_info.area),
           str(meal_info.category),str(meal_info.instructions),str(meal_info.measures),meal_info.image)


HOME_HTML = """
 <html><body>
     <h2>Welcome to the Meal Database</h2>
     <h3>Here are the list of meals we have</h3>
     <h4>{0}</h4>
     <form action="/meal" method = "post">
     <label>Enter the meal you want to see :</label>
     <input type="text" id="meal" name="meal"> </br>
     <input type="submit" value="Submit"></br>
     <a href='/searchbyingredient'>Search by Ingredient</a></br>
     <a href='/searchbycategory'>Search by Category</a></br>
     <a href='/searchbyarea'>Search by Area</a>
 </body></html>"""

MEAL_HTML = """
 <html><body>
     <h2>{0}</h2>
     <img src={6} alt="Mars Image" width=400 height=400>
     <h3>Ingredients</h3>
     <h4>{1}</h4>
     <h3>Area</h3>
     <h4>{2}</h4>
     <h3>Category</h3>
     <h4>{3}</h4>
     <h3>Instructions</h3>
     <h4>{4}</h4>
     <h3>Measures</h3>
     <h4>{5}</h4>     
 </body></html>"""


@app.route('/searchbyingredient')
def search_by_ingredient():
    ingredient_list = str(all_meals.display_all_ingredients())
    return ING_HTML.format(ingredient_list)


@app.route('/mealswithingredient',methods =['POST'])
def meals_with_ingredient():
    name = request.form['mealswithingredient']
    user_ingredient = str(all_meals.display_meals_with_ingredient(name))
    return MEALS_WITH_INGREDIENT_HTML.format(user_ingredient)

ING_HTML= """
<html><body>
    <h2>Ingredients</h2></br>
    <h3>{0}</h3>
    <form action="/mealswithingredient" method = "post"></br></br>
    <label>Enter the ingredient you want to look for in a meal :</label>
    <input type="text" id="ingredient" name="mealswithingredient"> 
  <input type="submit" value="Submit">
</form>
"""
MEALS_WITH_INGREDIENT_HTML = """
 <html><body>
     <h2>THE LIST OF MEALS</h2>
     <h3>{0},</h3>
 </body></html>"""

@app.route('/searchbycategory')
def search_by_category():
    category_list = str(all_meals.display_all_category())
    return CAT_HTML.format(category_list)


@app.route('/mealswithcategory',methods =['POST'])
def meals_with_category():
    name = request.form['mealswithcategory']
    user_category = str(all_meals.display_meals_with_category(name))
    return MEALS_WITH_CATEGORY_HTML.format(user_category)

CAT_HTML= """
<html><body>
    <h2>Categories</h2></br>
    <h3>{0}</h3>
    <form action="/mealswithcategory" method = "post"></br></br>
    <label>Enter the category of the meal you want to look for :</label>
    <input type="text" id="ingredient" name="mealswithcategory"> 
  <input type="submit" value="Submit">
</form>
"""
MEALS_WITH_CATEGORY_HTML = """
 <html><body>
     <h2>THE LIST OF MEALS</h2>
     <h3>{0},</h3>
 </body></html>"""

@app.route('/searchbyarea')
def search_by_area():
    area_list = str(all_meals.display_all_area())
    return AREA_HTML.format(area_list)


@app.route('/mealswitharea',methods =['POST'])
def meals_with_area():
    name = request.form['mealswitharea']
    user_area = str(all_meals.display_meals_with_area(name))
    return MEALS_WITH_AREA_HTML.format(user_area)

AREA_HTML= """
<html><body>
    <h2>Areas</h2>
    <h3>{0}</h3></br>
    <form action="/mealswitharea" method = "post"></br></br>
    <label>Enter the area of a meal :</label>
    <input type="text" id="ingredient" name="mealswitharea"> 
  <input type="submit" value="Submit">
</form>
"""
MEALS_WITH_AREA_HTML = """
 <html><body>
     <h2>THE LIST OF MEALS</h2>
     <h3>{0},</h3>
 </body></html>"""


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", port=5001, debug=True)
