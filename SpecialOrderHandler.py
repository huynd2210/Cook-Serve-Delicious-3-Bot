import threading
import time
from enum import Enum

import keyboard
import pyautogui
import main

from recipes import initRecipeBook, initHoldingStationRecipeBook, initCustomoOrderRecipes, initCookingProcedureRecipe
from util import pressButton, isColorSameWithinThreshold, triggerUponKeypress, pressAutoServe


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class SpecialOrderStatus(Enum):
    EMPTY = 0
    PENDING = 1
    COOKING = 2
    READY = 3
    # Urgent means the food is done cooking, and additional prepping is needed
    URGENT = 4


class SpecialOrderHandler:
    def __init__(self):
        self.orderStatuses = [SpecialOrderStatus.EMPTY] * 8

    def resetOrderStatuses(self):
        for i in range(len(self.orderStatuses)):
            self.orderStatuses[i] = SpecialOrderStatus.EMPTY

    def setCookingTimer(self, index, waitTime, stateTransitionFunction):
        delayedInvokeLambda = lambda func: (lambda *args, **kwargs: (time.sleep(waitTime), func(*args, **kwargs)))
        thread = threading.Thread(target=delayedInvokeLambda(stateTransitionFunction), args=(index,))
        print("Set cooking timer for index: ", index, " to ", waitTime, " seconds")
        thread.start()

    def setOrderStatusToEmpty(self, index):
        self.orderStatuses[index] = SpecialOrderStatus.EMPTY

    def setOrderStatusToUrgent(self, index):
        self.orderStatuses[index] = SpecialOrderStatus.URGENT

    def setOrderStatusToReady(self, index):
        self.orderStatuses[index] = SpecialOrderStatus.READY

    def setOrderStatusTransition(self, index, recipeNameJustCooked, cookingProcedureRecipe):
        cookingTime, additionalPreppingNeeded = self.getCookingProcedureOfRecipe(recipeNameJustCooked,
                                                                                 cookingProcedureRecipe)
        defaultDelay = 0.1
        if cookingTime == 0:
            # Set timer to 0.5 seconds to wait for auto serve to kick in
            print("Cooking time is 0, setting to 0.5 seconds")
            # setToEmpty = lambda index: SpecialOrderStatus.EMPTY

            self.setCookingTimer(index, defaultDelay, self.setOrderStatusToEmpty)

        elif additionalPreppingNeeded:
            self.setCookingTimer(index, cookingTime, self.setOrderStatusToUrgent)
        else:
            self.setCookingTimer(index, cookingTime + defaultDelay, self.setOrderStatusToEmpty)

    def getCookingProcedureOfRecipe(self, recipeName, cookingProcedureRecipe):
        return cookingProcedureRecipe[recipeName] if recipeName in cookingProcedureRecipe else (0, False)

    # Check if there is a special order
    def checkSpecialOrder(self):
        slotCoordinates = [
            (196, 158),
            (199, 225),
            (198, 281),
            (230, 339),
            (227, 400),
            (222, 460),
            (201, 513),
            (198, 573),
        ]

        slotColors = [
            (58, 59, 59),
            (49, 50, 51),
            (70, 72, 71),
            (107, 109, 109),
            (103, 106, 106),
            (95, 96, 96),
            (85, 85, 85),
            (77, 77, 78),
        ]

        # Current issue is that this would only work for one single loop.
        # The reason being once an order is cooked/being cooked, the status changed to READY. When it is served. and if immediately a new order comes
        # Then since the status is still READY, and there is an order pending, there is no way to switch to PENDING, as it require an order to first be empty.
        # Which is not possible since by the time we check, there is already an order there. Which is impossible to distinguish a new order or the previous order is
        # still being cooked.

        # Solution: We need to know the information of the order that we are currently cooking. And compare that to the cooking time of the said order.
        # If the alloted time has passed since we prepared the order. Then either the order is ready to be served/served, or it requires attention which
        # depends on the order.

        for i in range(len(slotCoordinates)):
            if self.orderStatuses[i] == SpecialOrderStatus.EMPTY:
                if not isColorSameWithinThreshold(slotColors[i],
                                                  pyautogui.pixel(slotCoordinates[i][0], slotCoordinates[i][1]),
                                                  threshold=40):
                    self.orderStatuses[i] = SpecialOrderStatus.PENDING
            # else:
            #     if isColorSameWithinThreshold(slotColors[i],
            #                                       pyautogui.pixel(slotCoordinates[i][0], slotCoordinates[i][1]),
            #                                       threshold=40):
            #         self.orderStatuses[i] = SpecialOrderStatus.EMPTY

        print(self.orderStatuses)
        return self.orderStatuses

    def isArriving(self, ocrReader):
        recipeRegionX, recipeRegionY, width, height = 1610, 0, 300, 60
        screenshotName = "distance.png"
        pyautogui.screenshot(screenshotName, region=(recipeRegionX, recipeRegionY, width, height))
        currentDistance = ocrReader.readtext(screenshotName, detail=0)

        currentDistance = ' '.join(currentDistance)
        print("Current distance: ", currentDistance)
        if "arriving" in currentDistance.lower():
            return True
        return False

    def cookSpecialOrder(self, ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes,
                         cookingProcedureRecipe):
        lastCheckTime = 0
        secondsBeforePollingIsArrived = 3
        # while True:
        currentTime = time.time()

        #Check if we are arriving at the destination through polling
        if currentTime - lastCheckTime >= secondsBeforePollingIsArrived:
            # If the truck is arriving at destination, we stop cooking special orders to avoid potential errors
            # if self.isArriving(ocrReader):
            #     self.resetOrderStatuses()
            #     print("We are arriving at the destination, stopping cooking special orders")
            #     break
            lastCheckTime = currentTime
        currentOrderStatus = self.checkSpecialOrder()
        for i in range(len(currentOrderStatus)):
            currentOrderStatus = self.checkSpecialOrder()
            if currentOrderStatus[i] == SpecialOrderStatus.PENDING:
                pressButton(str(i + 1))
                recipeJustCooked = main.cook(ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes)
                currentOrderStatus[i] = SpecialOrderStatus.COOKING
                self.setOrderStatusTransition(i, recipeJustCooked, cookingProcedureRecipe)
        print(f"{bcolors.WARNING}End Loop{bcolors.ENDC}")
        # Wait 1 sec before checking again
        time.sleep(1)



    def cookSpecialOrderWrapper(self, ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes,
                                cookingProcedureRecipe):
        print("Special Order Cooker ready")
        triggerUponKeypress(',', self.cookSpecialOrder, ocrReader=ocrReader,
                            recipeBook=recipeBook,
                            holdingStationRecipeBook=holdingStationRecipeBook,
                            customOrderRecipes=customOrderRecipes,
                            cookingProcedureRecipe=cookingProcedureRecipe)

    def runCheckSpecialOrder(self):
        # while True:
        #     checkSpecialOrder()
        #     time.sleep(0.5)
        self.checkSpecialOrder()


if __name__ == '__main__':
    # triggerUponKeypress(';', runCheckSpecialOrder())
    # runCheckSpecialOrder()
    #
    # specialOrderHandler = SpecialOrderHandler()
    # specialOrderHandler.orderStatuses[0] = SpecialOrderStatus.COOKING
    # print(specialOrderHandler.orderStatuses)
    # # specialOrderHandler.setOrderStatusTransition(0, 'a', {})
    # # setToEmpty = lambda orderStatus: SpecialOrderStatus.EMPTY
    #
    # specialOrderHandler.setCookingTimer(0, 1, specialOrderHandler.setOrderStatusToEmpty)
    # # specialOrderHandler.orderStatuses[0] = setToEmpty(specialOrderHandler.orderStatuses[0])
    #
    # print(specialOrderHandler.orderStatuses)
    # time.sleep(2)
    # print(specialOrderHandler.orderStatuses)

    specialOrderHandler = SpecialOrderHandler()

    ocrReader = main.initEasyOCR()
    recipeBook = initRecipeBook()
    holdingStationRecipeBook = initHoldingStationRecipeBook()
    customOrderRecipes = initCustomoOrderRecipes()
    cookingProcedureRecipe = initCookingProcedureRecipe()

    autoServeThread = threading.Thread(target=pressAutoServe)
    autoServeThread.start()

    print("Waiting for keypress...")
    triggerKey = ';'
    while True:
        if keyboard.is_pressed(triggerKey):
            specialOrderHandler.cookSpecialOrder(ocrReader, recipeBook, holdingStationRecipeBook, customOrderRecipes,
                                                 cookingProcedureRecipe)
            time.sleep(0.2)
