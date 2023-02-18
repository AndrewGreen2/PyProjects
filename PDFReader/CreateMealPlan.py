import pandas as pd
import os
import random
from PyPDF2 import PdfReader

def readWriteRecipeValues():
    file_path = r"C:\Users\andre\Documents\PyProjects\PDFReader\RecipeCSVs"   
    file_list = os.listdir(file_path)
    df_concat = pd.concat([pd.read_csv("PDFReader/RecipeCSVs/" + f) for f in file_list], ignore_index=True) 
    df_concat.to_csv("PDFReader/Combined Recipes.csv", index=False)
    recipes = pd.read_csv('PDFReader/Combined Recipes.csv')
    recipes = recipes.sort_values(by=['cals'], ignore_index=True)
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
    proteinGoal = 110
    carbGoal = 134
    fatGoal = 52
    calGoal = (proteinGoal * 4) + (carbGoal * 4) + (fatGoal * 9)
    noOfMeals = 3
    #print('Your calorie goal is approx: '+ str(calGoal))
    return(calGoal, proteinGoal, carbGoal, fatGoal, noOfMeals)

def listAcceptableRecipes(recipes, mealCalorieGoal, listStart, listEnd):
    mealOptions = []
    lowCals = mealCalorieGoal - 50
    highCals = mealCalorieGoal + 50    
    
    #Binary search base case
    if listEnd >= listStart:
        mid = (listStart + listEnd) // 2

    # If middle recipe calories are within acceptable range, add recipes within tolerance to mealOptions list
    if int(recipes.iloc[[mid]]['cals']) in range(lowCals, highCals):
            i = mid
            while int(recipes.loc[i]['cals']) in range(lowCals, highCals):
                mealOptions.append(recipes.loc[i])
                i -= 1            
            i = mid
            while int(recipes.loc[i]['cals']) in range(lowCals, highCals):
                mealOptions.append(recipes.loc[i])
                i += 1

    # If middle recipe calories are higher than upper acceptable range, repeat search within lower part of list
    elif int(recipes.iloc[[mid]]['cals']) > highCals:
        return(listAcceptableRecipes(recipes, mealCalorieGoal, listStart, mid - 1))
    # If middle recipe calories are lower than the lower acceptable range, repeat search within upper part of list
    else:
        return(listAcceptableRecipes(recipes, mealCalorieGoal, mid + 1, listEnd))
    return(mealOptions)



def createMealPlan(recipes, calGoal, proteinGoal, carbGoal, fatGoal, noOfMeals):
    meals = []
    while len(meals) != noOfMeals:
        mealCalorieGoal = int(calGoal/noOfMeals)
        meals.append(random.choice(listAcceptableRecipes(recipes, mealCalorieGoal, 0 , len(recipes))))
    print(meals)
        
def main():  
    #readWriteRecipeValues()      
    calGoal, proteinGoal, carbGoal, fatGoal, noOfMeals = getRequirements()
    createMealPlan(readWriteRecipeValues(), calGoal, proteinGoal, carbGoal, fatGoal, noOfMeals)
    

if __name__ == "__main__":
    main()
