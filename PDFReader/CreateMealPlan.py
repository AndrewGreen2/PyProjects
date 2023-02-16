import pandas as pd
import os

def readWriteRecipeValues():
    file_path = r"C:\Users\andre\Documents\PyProjects\PDFReader\RecipeCSVs"   
    file_list = os.listdir(file_path)
    df_concat = pd.concat([pd.read_csv("PDFReader/RecipeCSVs/" + f) for f in file_list], ignore_index=True) 
    df_concat.to_csv("PDFReader/Combined Recipes.csv", index=False)
    recipes = pd.read_csv('PDFReader/Combined Recipes.csv')
    return(recipes)

def getRequirements():
    # while True:1
    #     try:
    #         proteinGoal = int(input("Enter Protein Goal (g): "))
    #         break
    #     except:
    #         print("That's not a valid option!")
    # while True:
    #     try:
    #         fatGoal = int(input("Enter Fat Goal (g): "))
    #         break
    #     except:
    #         print("That's not a valid option!")
    # while True:
    #     try:
    #         carbGoal = int(input("Enter Carb Goal (g): "))
    #         break
    #     except:
    #         print("That's not a valid option!")
      # while True:
    #     try:
    #         noOfMeals = int(input("How many meals do you need? "))
    #         break
    #     except:
    #         print("That's not a valid option!")
    proteinGoal = 219
    carbGoal = 190
    fatGoal = 60
    calGoal = (proteinGoal * 4) + (carbGoal * 4) + (fatGoal * 9)
    noOfMeals = 3
    print('Your calorie goal is approx: '+ str(calGoal))
    return(calGoal, proteinGoal, carbGoal, fatGoal)


def createMealPlan(recipes, calGoal, proteinGoal, carbGoal, fatGoal):
    # print(recipes)
    # print(recipes.sample(frac = 1))
    recipes = recipes.sample(frac = 1)
    meals = []
    for index, row in recipes.iterrows():
        currentCals=0
        for meal in meals:
            currentCals += meal[0]
        targetCals = calGoal - currentCals
        if row['cals'] <= targetCals:
            meals.append([row['cals'], row['pgNo']]) 

    print(meals)
    print('Calories = ' + str(calGoal - currentCals))

    
def main():        
    calGoal, proteinGoal, carbGoal, fatGoal = getRequirements()
    createMealPlan(readWriteRecipeValues(), calGoal, proteinGoal, carbGoal, fatGoal)

if __name__ == "__main__":
    main()
