import time
from enum import Enum

import keyboard
import pyautogui
import random

import main
from recipes import initRecipeBook, initHoldingStationRecipeBook, initCustomoOrderRecipes
from util import initEasyOCR, triggerUponKeypress, isColorPresentInImage, pressButton


class HoldingStationStatus(Enum):
    EMPTY = 0
    READY = 1

# Logic: Open the first empty HoldingStation. If recipe requirements have not been checked. check it and update
# the food needed to be cooked in isRecipeNeeded. Cook the needed recipe in order until all Holding Stations contain food
#If no food are needed, but there are still empty Holding Station, loop over and continue cooking.

class HoldingStationHandler:

    def __init__(self):
        self.amountOfHoldingStations = 6
        self.orderStatuses = [HoldingStationStatus.EMPTY] * 6
        self.isRecipeNeeded = []

    def updateHoldingStationStatus(self):
        holdingStationColor = (35, 35, 35)
        holdingStationPositions = [
            (355,60),
            (480,60),
            (600,60),
            (725,60),
            (850,60),
            (965,60),
        ]

        #Check if holding station is empty based on color. If color of the holding station is gray, it is empty
        for i in range(len(holdingStationPositions)):
            if pyautogui.pixel(holdingStationPositions[i][0], holdingStationPositions[i][1]) == holdingStationColor:
                self.orderStatuses[i] = HoldingStationStatus.EMPTY
            else:
                self.orderStatuses[i] = HoldingStationStatus.READY

    def checkNeededHoldingStationRecipe(self):
        recipeNeededRegions = [
            (800, 390, 75, 75),
            (800, 460, 75, 75),
            (800, 530, 75, 75),
            (800, 600, 75, 75),
        ]
        isRecipeNeeded = []
        for i in range(len(recipeNeededRegions)):
            screenshotName = f'recipeNeeded{i}.png'
            pyautogui.screenshot(screenshotName, region=recipeNeededRegions[i])
            recipePresentColorIndicator = (255, 160, 64)
            recipePresentButFulfilledColorIndicator = (128,128,128)

            isMoreServingNeeded = isColorPresentInImage(screenshotName, recipePresentColorIndicator)
            isServingFulfilled = isColorPresentInImage(screenshotName, recipePresentButFulfilledColorIndicator)

            #If either isMoreServingNeeded or isServingFulfilled is True, then the recipe is present for the day and is not empty. Therefore we add to isRecipeNeeded
            if isMoreServingNeeded or isServingFulfilled:
                isRecipeNeeded.append(isMoreServingNeeded)

        print("isRecipeNeeded", isRecipeNeeded)
        return isRecipeNeeded

    def cookNeededRecipe(self, ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes, indexToCook):
        indexToChar = {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'e',
            5: 'f',
            6: 'g',
            7: 'h',
        }

        if self.isRecipeNeeded[indexToCook]:
            pressButton(indexToChar[indexToCook])
        else:
            #If the recipe at indexToCook is not needed, cook random recipe that is needed
            #Bug: self.isRecipeNeeded can contains more recipes than currently have. Therefore there is a chance that it can randomly pick the index that is out of bound
            choices = [i for i in range(len(self.isRecipeNeeded)) if self.isRecipeNeeded[i]]
            pressButton(indexToChar[random.choice(choices)])

        main.cook(ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes)
        self.orderStatuses[indexToCook] = HoldingStationStatus.READY

    #Current problem, when in stop, and the holding station does not contain enough food, then the code will break.
    def cookHoldingStation(self, ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes):
        self.updateHoldingStationStatus()

        holdingStationButtons = {
            0: 'F1',
            1: 'F2',
            2: 'F3',
            3: 'F4',
            4: 'F5',
            5: 'F6',
        }

        hasCheckedRecipeNeeded = False
        for i in range(len(self.orderStatuses)):
            if self.orderStatuses[i] == HoldingStationStatus.EMPTY:
                pressButton(holdingStationButtons[i])
                time.sleep(0.2)
                #Checking recipes needed to cook once is enough, avoid checking more than one to save time
                if not hasCheckedRecipeNeeded:
                    self.isRecipeNeeded = self.checkNeededHoldingStationRecipe()
                    hasCheckedRecipeNeeded = True
                self.cookNeededRecipe(ocrReader, recipeBook, holdingStationRecipeBook,  customOrderRecipes, i % len(self.isRecipeNeeded))

def test():
    print("Waiting for keypress...")
    triggerKey = ';'
    while True:
        if keyboard.is_pressed(triggerKey):
            print("triggered")
            time.sleep(0.2)
            pressButton('F1')
            time.sleep(0.2)
            pressButton('a')
            time.sleep(0.2)
            pressButton('c')
            pressButton('l')
            pressButton('s')
            pressButton('w')
            pressButton('m')
            pressButton('x')
            pressButton('enter')
            pressButton('F2')
            time.sleep(0.2)
            pressButton('b')

if __name__ == '__main__':
    recipeBook = initRecipeBook()
    holdingStationRecipeBook = initHoldingStationRecipeBook()
    ocrReader = initEasyOCR()
    customOrderRecipes = initCustomoOrderRecipes()
    #
    holdingStationHandler = HoldingStationHandler()
    #
    triggerUponKeypress(
        ";", holdingStationHandler.cookHoldingStation,
        ocrReader=ocrReader,
        recipeBook=recipeBook,
        holdingStationRecipeBook=holdingStationRecipeBook,
        customOrderRecipes=customOrderRecipes)

    # test()

