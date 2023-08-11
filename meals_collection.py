import requests
from Meals import Meals

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
    def info_about_meal(self,name_to_find):
        self.meal_list.sort(key=lambda meal: meal.name)
        l = 0
        u = len(self.meal_list) - 1
        while (l <= u):
            mid = (l + u) // 2
            if (self.meal_list[mid].name > name_to_find ):
                u = mid - 1
            elif (self.meal_list[mid].name < name_to_find):
                l = mid + 1
            else:
                return self.meal_list[mid]
        return None

    def display_meals_with_ingredient(self,ingredient):
        meal_with_ingredient_list = []
        for meal in self.meal_list:
            for ing in meal.ingredients:
                if ing == ingredient:
                    meal_with_ingredient_list.append(meal.name)
        return meal_with_ingredient_list
    def display_all_ingredients(self):
        all_ingredients = []
        for meal in self.meal_list:
            for ing in meal.ingredients:
                all_ingredients.append(ing)
        return all_ingredients
    def display_meals_with_category(self,category):
        meal_with_category_list = []
        for meal in self.meal_list:
            if meal.category == category:
                meal_with_category_list.append(meal.name)
        return meal_with_category_list

    def display_all_category(self):
        all_category =[]
        for meal in self.meal_list:
            all_category.append(meal.category)
        return all_category

    def display_meals_with_area(self,area_to_find):
        meal_with_area_list = []
        for meal in self.meal_list:
            if meal.area == area_to_find:
                meal_with_area_list.append(meal.name)
        return meal_with_area_list

    def display_all_area(self):
        all_areas=[]
        for meal in self.meal_list:
            all_areas.append(meal.area)
        return all_areas
def main():

    response1 = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=")
    all_meals_json = response1.json()
    all_meals_list = []
    for meal in all_meals_json["meals"]:
        all_meals_list.append(Meals(meal))

    all_meals = mealCollection(all_meals_json["meals"])
    print(all_meals.display_meals_with_ingredient("Onion"))


if __name__== "__main__":
    main()
