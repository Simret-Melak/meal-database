import requests
from meal import Meals

class mealCollection:
    def __init__(self,meals_json_list):
        self.meal_list= []
        for meal_json in meals_json_list:
            new_meal = Meals(meal_json)
            self.meal_list.append(new_meal)

    def __str__(self):
        return str(self.meal_list)

    def display_all_meals_sorted(self):
        all_meals = []
        self.meal_list.sort(key=lambda meal: meal.name)
        for meal in self.meal_list:
            all_meals.append(meal.name)
        return all_meals
    def info_about_meal(self,name):
        check = False
        for meal in self.meal_list:
            if meal.name==name:
                check = True
                return meal
        if check == False:
            return None

    def display_meals_with_ingredient(self,ingredient):
        meal_with_ingredient_list = []
        for meal in self.meal_list:
            for ing in meal.ingredients:
                if ing == ingredient:
                    meal_with_ingredient_list.append(meal.name)
        return meal_with_ingredient_list

    def display_meals_with_category(self,meal_categories):
        meal_with_category = []
        for meal in self.meal_list:
                if meal.category == meal_categories:
                    meal_with_category.append(meal.name)

        return meal_with_category

    def display_meals_with_area(self,meal_area):
        meal_with_area = []
        for meal in self.meal_list:
            if meal.area == meal_area:
                meal_with_area.append(meal.name)

        return meal_with_area

def main():

    response1 = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=")
    all_meals_json = response1.json()
    all_meals_list = []
    for meal in all_meals_json["meals"]:
        all_meals_list.append(Meals(meal))

    all_meals = mealCollection(all_meals_json["meals"])
    print(all_meals.display_meals_with_ingredient("Onion"))


    print(all_meals.display_meals_with_category(("Dessert")))
    print(all_meals.display_meals_with_area(("Turkish")))




if __name__ == "__main__":
    main()