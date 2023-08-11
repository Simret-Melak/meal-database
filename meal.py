import requests

class Meals:
    def __init__(self,meals_json):
        self.name = meals_json["strMeal"]
        self.category = meals_json["strCategory"]
        self.area = meals_json["strArea"]
        self.instructions = meals_json["strInstructions"]
        self.ingredients = []
        ingredient = "  "
        i = 1
        while ingredient!= "null" and ingredient!="" and i<=20:
            self.ingredients.append(meals_json["strIngredient"+str(i)])
            ingredient = meals_json["strIngredient"+str(i)]
            i+=1
        self.measures = []
        measure = "  "
        m = 1
        while measure!= "null" and measure!="" and m<=20:
            self.measures.append(meals_json["strMeasure"+str(m)])
            measure = meals_json["strIngredient"+str(m)]
            m+=1
        self.image = meals_json["strMealThumb"]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def main():
    name = input("Enter the meal name :")
    response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=")
    meals_json = response.json()

    meals_objects = []
    for meal_json in meals_json:
        meals_objects.append(Meals(meal_json))
    print(meals_objects)

if __name__== "__main__":
    main()