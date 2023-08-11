from meals_collection import mealCollection

def example_data():
    test_list = []
    test_list.append({"strMeal":"pancakes","strCategory":"Dessert","strArea":"American",
                      "strInstructions":"cook","strIngredient1":"egg","strIngredient2":"flour",
                      "strIngredient3":"sugar","strIngredient4":"null","strMeasure1":"1 tea spoon",
                      "strMeasure2":"1/2 cup","strMeasure3":"null","strMeasure4":"null","strMealThumb":"/www.http"})
    test_list.append({"strMeal":"pasta","strCategory":"main meal","strArea":"Italian",
                      "strInstructions":"boil","strIngredient1":"pasta","strIngredient2":"tomato",
                      "strIngredient3":"onions","strIngredient4":"","strMeasure1":"2 tea spoon",
                      "strMeasure2":"1/2 cup","strMeasure3":"null","strMeasure4":"null","strMealThumb":"/http"})
    test_list.append({"strMeal":"Apple pie","strCategory":"fruit","strArea":"American",
                      "strInstructions":"eat","strIngredient1":"apple","strIngredient2":"tomato",
                      "strIngredient3":"sugar","strIngredient4":"","strMeasure1":"2 tea spoon",
                      "strMeasure2":"1/2 cup","strMeasure3":"null","strMeasure4":"null","strMealThumb":"/http"})
    return test_list

def test_creating_meal_collection():
    my_meal_collection = mealCollection(example_data())
    print(my_meal_collection)

def test_display_all_meals_sorted():
    my_meal_collection = mealCollection(example_data())
    assert my_meal_collection.meal_list[0].name=="pancakes"
    my_meal_collection.display_all_meals_sorted()
    assert my_meal_collection.meal_list[0].name == "Apple pie"
    assert len(my_meal_collection.meal_list) ==3

def test_info_about_meal():
    my_meal_collection = mealCollection(example_data())
    assert my_meal_collection.info_about_meal("Apple pie").area=="American"
    assert my_meal_collection.info_about_meal("pie")== None

def test_display_meals_with_ingredient():
    my_meal_collection = mealCollection(example_data())
    assert my_meal_collection.display_meals_with_ingredient("egg")==["pancakes"]
    assert my_meal_collection.display_meals_with_ingredient("tomato") == ["pasta","Apple pie"]
    assert my_meal_collection.display_meals_with_ingredient("salt") == []

def test_display_meals_with_category():
    my_meal_collection = mealCollection(example_data())
    assert my_meal_collection.display_meals_with_category("Dessert")==["pancakes"]
    assert my_meal_collection.display_meals_with_category("Des") == []

def test_display_meals_with_area():
    my_meal_collection = mealCollection(example_data())
    assert my_meal_collection.display_meals_with_area("Italian")==["pasta"]
    assert my_meal_collection.display_meals_with_area("Des") == []