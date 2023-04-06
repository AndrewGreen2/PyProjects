import pandas as pd
import os
import random

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
    proteinGoal = 65
    carbGoal = 65
    fatGoal = 29
    #calGoal = (proteinGoal * 4) + (carbGoal * 4) + (fatGoal * 9)
    calGoal = 726
    noOfMeals = 1
    print(f'Your calorie goal is approx:  {str(calGoal)} \n')
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
    return(meals)

def openMeals(meals):
    totalCals = 0
    totalPro = 0
    totalCarb = 0
    totalFat = 0
    pdfDict = {
        "BTB": "BTB-Cookbook",
        "ELCC": "Elite Low Calorie CookBook",
        "ABCB":"The AnabolicMD Cookbook"
    }

    for i, meal in enumerate(meals):
        totalCals += meal['cals']
        totalPro += meal['pro']
        totalCarb += meal['carbs']
        totalFat += meal['fats']
        print(f'Meal {i+1} : {pdfDict[meal["pdf"]]} Page: {meal["pgNo"]}')
    print(f'\n-------Totals-------\nCalories:  {totalCals} \nProtein:  {totalPro} \nCarbs:  {totalCarb} \nFats: {totalFat}\n')




def main():  
    #readWriteRecipeValues()      
    calGoal, proteinGoal, carbGoal, fatGoal, noOfMeals = getRequirements()
    mealPlan = createMealPlan(readWriteRecipeValues(), calGoal, proteinGoal, carbGoal, fatGoal, noOfMeals)
    openMeals(mealPlan)
    

if __name__ == "__main__":
    main()
