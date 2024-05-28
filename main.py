import threading
import time

import pyautogui

import HoldingStationHandler
import SpecialOrderHandler
from recipes import initRecipeBook, initHoldingStationRecipeBook, initCustomoOrderRecipes, initCookingProcedureRecipe
from util import pressButton, removeNonCharactersExceptWhitespaceAndNumbers, remove_extra_whitespaces, \
    triggerUponKeypress, multipleTriggerUponKeypress, initEasyOCR, pressAutoServe, checkCache, loadOCRCache, \
    generateImageHash, appendCache, saveImageOCRCacheToFile


def determineButtonPressOrderForCustomOrder(recipeDescription, customRecipeToCook):
    previousIngredientGroup = 1
    buttonsToPress = []

    for ingredient in recipeDescription:
        if ingredient in customRecipeToCook.ingredientsPart1:
            buttonsToPress.append(customRecipeToCook.ingredientsPart1[ingredient])
        elif ingredient in customRecipeToCook.ingredientsPart2:
            currentIngredientGroup = 2
            if previousIngredientGroup != currentIngredientGroup:
                previousIngredientGroup = currentIngredientGroup
                buttonsToPress.append("space")
            buttonsToPress.append(customRecipeToCook.ingredientsPart2[ingredient])
        elif ingredient in customRecipeToCook.ingredientsPart3:
            currentIngredientGroup = 3
            if previousIngredientGroup != currentIngredientGroup:
                amountOfSpacebarPresses = currentIngredientGroup - previousIngredientGroup
                previousIngredientGroup = currentIngredientGroup
                for i in range(amountOfSpacebarPresses):
                    buttonsToPress.append("space")
            buttonsToPress.append(customRecipeToCook.ingredientsPart3[ingredient])
        else:
            print("Ingredient not found: ", ingredient)
            # raise Exception("Ingredient: " + ingredient + " not found")
    return buttonsToPress

def cookCustomOrder(recipeName, customOrderRecipes, ocrReader):
    customRecipeToCook = customOrderRecipes[recipeName]
    recipeDescription = readRecipeDescription(ocrReader)

    recipeDescription = recipeDescription.split(" ")

    # Sanitize recipe description
    for i in range(len(recipeDescription)):
        recipeDescription[i] = removeNonCharactersExceptWhitespaceAndNumbers(recipeDescription[i]).strip()
        recipeDescription[i] = remove_extra_whitespaces(recipeDescription[i])

    print("Ingredients to cook:", recipeDescription)

    buttonsToPress = determineButtonPressOrderForCustomOrder(recipeDescription, customRecipeToCook)
    print("Buttons to press: ", buttonsToPress)
    for button in buttonsToPress:
        pressButton(button, isDebug=True)
    pressButton('enter', isDebug=True)


def handleCustomOrder(recipeName, customOrderRecipes, ocrReader):
    if recipeName in customOrderRecipes:
        cookCustomOrder(recipeName, customOrderRecipes, ocrReader)
        return True

    return False


def cookRecipe(recipeBook, recipeName, customOrderRecipes, ocrReader):
    # If it is custom order, cook custom order and return. (i.e we already cooked)
    if handleCustomOrder(recipeName, customOrderRecipes, ocrReader):
        return

    print("Cooking recipe: ", recipeName)
    buttonsToPress = recipeBook[recipeName]
    print("Buttons to press for the recipe: ", buttonsToPress)
    for button in buttonsToPress:
        pressButton(button, isDebug=True)

    # Press enter to start cooking
    pressButton('enter', isDebug=True)


def cook(ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes, ocrCache=None, cookingProcedureRecipe=None):
    recipeName, recipeBookToUse = readRecipe(ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes)

    #if the "cook" button is pressed and there is no "cooking phase" (i.e pressing on ready order) then nothing should happen.
    if recipeName == '':
        return

    recipeName = removeNonCharactersExceptWhitespaceAndNumbers(recipeName).strip()
    recipeName = remove_extra_whitespaces(recipeName)

    cookRecipe(recipeBookToUse, recipeName, customOrderRecipes, ocrReader)

    #Return recipe name of the cooked recipe
    return recipeName

def getRecipeNameFromScreenshot(ocrReader, ocrCache=None):
    recipeRegionX, recipeRegionY, width, height = 600, 827, 700, 55
    screenshotName = "test.png"
    pyautogui.screenshot(screenshotName, region=(recipeRegionX, recipeRegionY, width, height))

    recipeName = checkCache(ocrCache, screenshotName)
    if recipeName:
        print("Found recipe name in cache: ", recipeName)
        return [recipeName]
    else:
        recipeName = ocrReader.readtext(screenshotName, detail=0)


        return recipeName


def readHoldingStationRecipe(ocrReader, ocrCache=None):
    # recipeDescription = ' '.join(handleRecipeDescription(ocrReader))

    recipeDescription = readRecipeDescription(ocrReader, ocrCache)

    # cookRecipe(recipeBook, recipeDescription)
    print(recipeDescription)
    return recipeDescription


def readRecipeDescription(ocrReader, ocrCache=None):
    if ocrCache is None:
        ocrCache = loadOCRCache()

    recipeRegionX, recipeRegionY, width, height = 440, 870, 1050, 110
    screenshotName = "recipeDescription.png"
    pyautogui.screenshot(screenshotName, region=(recipeRegionX, recipeRegionY, width, height))

    recipeDescription = checkCache(ocrCache, screenshotName)
    if recipeDescription is not None:
        print("Found recipe name in cache: ", recipeDescription)
        return recipeDescription
    else:
        recipeDescription = ocrReader.readtext(screenshotName, detail=0)

        recipeDescription = ' '.join(recipeDescription)
        print("Reading Recipe Description:", recipeDescription)
        recipeDescription = removeNonCharactersExceptWhitespaceAndNumbers(recipeDescription).strip()
        recipeDescription = remove_extra_whitespaces(recipeDescription)

        appendCache(ocrCache, screenshotName, recipeDescription)
        saveImageOCRCacheToFile(ocrCache)
        return recipeDescription

def readRecipe(ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes, ocrCache=None):
    if ocrCache is None:
        ocrCache = loadOCRCache()

    recipeName = getRecipeNameFromScreenshot(ocrReader, ocrCache)

    # if recipeName is empty, that means user probably misspressed
    if len(recipeName) == 0:
        print("Recipe Name is empty")
        return "", recipeBook

    if len(recipeName) > 1:
        print("More than 1 recipe detected, these are the recipes: ", recipeName)
        recipeName = ' '.join(recipeName)
        print("Recipe Name: ", recipeName)
        return recipeName, recipeBook

    recipeName = removeNonCharactersExceptWhitespaceAndNumbers(recipeName[0]).strip()
    recipeName = remove_extra_whitespaces(recipeName)
    print("Recipe Name: ", recipeName)



    if recipeName in customOrderRecipes:
        return recipeName, customOrderRecipes

    if recipeName not in recipeBook:
        print("Recipe Name not in recipeBook, recipeName: ", recipeName)
        recipeDescription = readHoldingStationRecipe(ocrReader, ocrCache)
        return recipeDescription, holdingStationRecipeBook

    appendCache(ocrCache, "test.png", recipeName)
    saveImageOCRCacheToFile(ocrCache)

    return recipeName, recipeBook


def runBot():
    recipeBook = initRecipeBook()
    holdingStationRecipeBook = initHoldingStationRecipeBook()
    customOrderRecipes = initCustomoOrderRecipes()
    cookingProcedureRecipe = initCookingProcedureRecipe()
    ocrCache = loadOCRCache()

    ocrReader = initEasyOCR()

    # Start auto serve
    autoServeThread = threading.Thread(target=pressAutoServe)
    autoServeThread.start()

    triggerFunctionMap = {
        ';': cook,
        ",": runCookingBot,
    }

    multipleTriggerUponKeypress(triggerFunctionMap, ocrReader=ocrReader,
                                recipeBook=recipeBook,
                                holdingStationRecipeBook=holdingStationRecipeBook,
                                customOrderRecipes=customOrderRecipes,
                                cookingProcedureRecipe=cookingProcedureRecipe,
                                ocrCache=ocrCache)

def runCookingBot(ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes, cookingProcedureRecipe, ocrCache=None):
    holdingStationHandler = HoldingStationHandler.HoldingStationHandler()
    specialOrderHandler = SpecialOrderHandler.SpecialOrderHandler()

    while True:
        #Run HS
        print("Holding Station cooking")
        holdingStationHandler.cookHoldingStation(ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes)
        time.sleep(1)
        #Run SO
        print("Special Order cooking")
        specialOrderHandler.cookSpecialOrder(ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes, cookingProcedureRecipe)



def test():
    ocrReader = initEasyOCR()
    screenshotName = "test.jpg"

    start = time.perf_counter()
    for i in range(10):
        recipeDescription = ocrReader.readtext(screenshotName, detail=0)

    end = time.perf_counter()
    print(end - start)

if __name__ == '__main__':
    runBot()


    # test()
    # print(torch.cuda.is_available())

    # triggerUponKeypress(';', handleRecipeDescription, ocrReader=initEasyOCR())

    # cookHoldingStationRecipe(initEasyOCR(), initHoldingStationRecipeBook())
    # triggerUponKeypress(';', cookHoldingStationRecipe, ocrReader=initEasyOCR())

# def notifySpecialOrderHandler(specialOrderHandler):

