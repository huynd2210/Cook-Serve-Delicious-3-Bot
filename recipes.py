class CustomOrderRecipe:
    def __init__(self, ingredientsPart1, ingredientsPart2=None, ingredientsPart3=None):
        if ingredientsPart3 is None:
            ingredientsPart3 = []
        if ingredientsPart2 is None:
            ingredientsPart2 = []
        self.ingredientsPart1 = ingredientsPart1
        self.ingredientsPart2 = ingredientsPart2
        self.ingredientsPart3 = ingredientsPart3


def initCookingProcedureRecipe():
    # Procedure contains cooking time and whether the recipe need additional prepping
    cookingProcedureRecipe = {
        "Salisbury": (5, True),
        "Bananas Foster": (10.5, False),
    }

    return cookingProcedureRecipe


def initCustomoOrderRecipes():
    # Ice Cream Sundae
    iceCreamSundaeIngredientPart1 = {
        "Vanilla": 'v',
        "Chocolate": 'c',
        "Cookie Dou": 'd',
        "Butter P": 'b',
        "Mint Choc": 'm',
        "Rocky Road": 'r',
        "Praline P": 'p',
        "RSherbert": 's',
    }

    iceCreamSundaeIngredientPart2 = {
        "Choc Syr": 'c',
        "Straw Syr": 's',
        'Nuts': 'n',
        "Gummies": 'g',
        "Bananas": 'b',
        "Hard Candy": 'h',
        "Sprinkles": 'p',
    }

    iceCreamSundaeIngredientPart3 = {
        "Strawberries": 's',
        "Cookie Bits": 'c',
        'Whip': 'w',
    }

    phoToppingIngredientPart1 = {
        "Chives": 'c',
        "Radish": 'r',
        "Onion Shoot": 'n',
        "Cilantro": 'l',
        "Jalapeno": 'j',
        "Basil": 'b',
        "Lime": 'i',
        # ignore extra information like these?
        # 'Basil and Lime are always added to all recipes': '',
        # 'Basil and Lime are alwavs added to all recipes': '',
    }

    banhMiIngredientPart1 = {
        "Chicken": 'k',
        "Tofu Slices": 't',
        "Ground Meat": 'm',
        "Pork Tender": 'p'
    }

    banhMiIngredientPart2 = {
        "WOnions": 'n',
        "Quail Eggs": 'e',
        "Cilantro": 'l',
        'Bread': 'b',
        "Carrots": 'a',
        "Cucumbers": 'u',
        "Radishes": 'r',
        'Jalapenos': 'j',
    }

    miniSubIngredientPart1 = {
        "Ham": 'h',
        "Turkey": 'u',
        "Tuna": 't',
        "Bacon": 'b',
        "Capicola": 'c',
        "Roast Beef": 'r',
        "Meatballs": 'm',
        "Salami": 's',
    }

    miniSubIngredientPart2 = {
        "Cheese": 'c',
        "Tomato": 't',
        "Swiss": 's',
        "WOnions": 'n',
        "Provolone": 'v',
        "Pickles": 'p',
        "Lettuce": 'l',
        "Jalapenos": 'j',
    }

    miniSubIngredientPart3 = {
        "Olives": 'v',
        "BPepper": 'b',
        "GPepper": 'g',
        "Cucumber": 'u',
        "POnions": 'n',
        "White Bread": 'w',
        "Wheat Bread": 'h',
        "Rosemary Bread": 'r',
    }

    customOrderRecipes = {
        "Custom Ice Cream Order": CustomOrderRecipe(iceCreamSundaeIngredientPart1, iceCreamSundaeIngredientPart2,
                                                    iceCreamSundaeIngredientPart3),
        "Custom Pho Toppings": CustomOrderRecipe(phoToppingIngredientPart1),
        "Custom Banh Mi Order": CustomOrderRecipe(banhMiIngredientPart1, banhMiIngredientPart2),
        "Custom Mini Sub Order": CustomOrderRecipe(miniSubIngredientPart1, miniSubIngredientPart2,
                                                   miniSubIngredientPart3),
    }

    return customOrderRecipes


# This includes only the recipes that doesn't have a dedicated name, and use only "Holding station Prep"
def initHoldingStationRecipeBook():
    recipeBook = {
        "Strips 4 After placing the ingredients Dunk Cook": ["s", 's', 's', 's', 'd'],
        "Falafel 4 After placing the ingredients Dunk Cook": ["f", 'f', 'f', 'f', 'd'],
        "French Fr 4 After placing the ingredients Dunk Cook": ["f", 'f', 'f', 'f', 'd'],
        "Huauzontle 4 After placing the ingredients Dunk Cook": ["h", 'h', 'h', 'h', 'd'],
        "Turkey Leg 4": ['t', 't', 't', 't'],
        "Espresso": ['e'],
        "Ice Water Espresso": ['i', 'e'],

        #Yaki Tomorokoshi
        "Corn 4": ['r', 'r', 'r', 'r'],
        "Corn Soy Sau Butter": ['r', 's', 'u'],

        #Bunny Chow
        "Beef Potatoes GPepper DOnion Tomato Sau Broth Leaf Turmeric Chili Pow Bay": ['b', 'p', 'g', 'n', 't', 'space', 'b', 'l', 't', 'h'],
        'Cut Bunny Chow Top': ['c', 'b'],
        
        # Ham Slices
        "Ham Seasoning": ['h', 's'],

        # Garden Salad
        "Lettuce Carrots Tomatoes Croutons Cucumbers": ["l", "a", "t", "r", "u"],

        # Brisket
        "Brisket Inject BBQ Seasoning": ['b', 'i', 's'],

        # Bibingka
        "Banana Leaf Batter": ['l', 'b'],

        # Deluxe Nachos
        "Chicken Shrimp Beef Ground Meat": ['k', 'h', 'b', 'm'],

        # Prime Ribs
        "Prime Rib Sauce Seasoning": ['p', 'a', 's'],

        # Steak
        "New York Strip": ['n'],
        "TBone": ['t'],
        "Porterhouse": ['p'],

        # Stuffed Artichokes
        "Water Artichokes Stuffing Lid": ['w', 'a', 's', 'l'],

        # Banh Mi
        "Ground Meat Pork Tender Chicken": ['m', 'p', 'k'],

    }

    return recipeBook


def initRecipeBook():
    # Recipe Book consists of recipe name and buttons to press
    recipeBook = {
        "Ayam Goreng": ["a", "a", "a", "a", "d"],
        "Blancmange": ["c", "l", "s", "w", "m", "x"],
        "Buta Kimchi": ["k", "n", "p"],
        "Brownies Prep": ["b"],
        "Classic Crab Legs": ["c", "l"],
        "Japchae": ["d", "r", "s"],
        "Jerk Chicken": ["k", "g", "m"],
        "Marshmallow Squares": ["w", "c", "m"],
        "Bananas Foster": ["u", "s", "b", "r"],

        "Duck Confit": ["d", "p", "f"],

        "Baklava": ['p', 'n', 'p', 'n', 'p'],

        "Chicken Kiev": ['k', 'p', 'l', 'l', 'r', 'h', 'c', 'f'],

        #Okroshka
        "01 Pork Train": ['r', 'u', 'e', 'o', 'p', 'space', 'y', 'b'],
        "02 Beef Train": ['r', 'b', 'u', 'e', 'o', 'space', 'y', 'b'],
        "03 Chicken Train": ['r', 'k', 'u', 'e', 'o', 'space', 'y', 'b'],
        "04 Ham Train": ['r', 'h', 'u', 'e', 'o', 'space', 'y', 'b'],
        "05 Meat Train": ['r', 'b', 'k', 'u', 'e', 'o', 'space', 'y', 'b'],

        #Meatloaf
        "O1 Classic Meatloaf": ['m', 'a'],
        "02 Bacon Wrapped Meatloaf": ['m', 'a', 'b'],

        #Steamed Momos
        "O1 Mincemeat Momos": ['d', 'f', 'space', 'm', 'w'],
        "02 Beef Momos": ['d', 'f', 'space', 'b', 'w'],
        "03 Potato Momos": ['d', 'f', 'space', 'p', 'w'],
        "04 Vegetable Momos": ['d', 'f', 'space', 'v', 'w'],

        #Chow Mein
        "01 Beef Chow Mein": ['o', 'w', 'p', 'c', 'b', 'a', 'm', 'space', 'o', 'b'],
        "02 Chicken Chow Mein": ['o', 'w', 'p', 'c', 'b', 'a', 'm', 'space', 'o', 'k'],
        "03 Shrimp Chow Mein": ['o', 'w', 'p', 'c', 'b', 'a', 'm', 'space', 'o', 'h'],
        "04 Pork Chow Mein": ['o', 'w', 'p', 'c', 'b', 'a', 'm', 'space', 'o', 'p'],
        "05 Veggie Chow Mein": ['o', 'w', 'p', 'c', 'b', 'a', 'm', 'r'],

        #Egg Drop Soup
        "EggDrop Soup": ['e', 'c', 'm'],

        #Khachapuri
        "Khachapuri": ['d', 's', 'c'],

        #Grilled Cheese Sandwich
        "Grilled Cheese Sandwich": ['s', 'n', 'd', 'w', 'c', 'h'],

        #Soup
        "O1 Broccoli Deluxe Soup": ['r', 'c', 'e', 'space', 'r'],
        "02 Classic Lentil": ['b', 'c', 'a', 'l'],
        "03 Tortilla Soup": ['t', 'n', 'space', 't'],
        "04 Potato and Chicken": ['b', 'c', 'e', 'space', 'o', 'k', 'p'],
        "05 Veggie Soup": ['b', 'c', 'a', 'e', 'space', 'm', 'p'],
        "06 Chicken Noodle Classic": ['b', 'n', 'space', 'o', 'k'],

        "Pancit": ['n', 'e', 'c', 'o', 'h', 'k'],

        #Haemul Panjeon
        "O1 Squid Special": ['b', 'c', 'u', 'q', 'j', 's'],
        "02 Shrimp Special": ['b', 'c', 'u', 'j', 's', 'h'],
        "03 Gourmet Special": ['b', 'c', 'u', 'q', 'j', 's', 'h'],

        #Pupusas
        "01 Chicken Pupusas": ['d', 'l', 'k', 'f'],
        "02 Cheese Pupusas": ['d', 'l', 'c', 'f'],
        "03 Pork Pupusas": ['d', 'l', 'p', 'f'],
        "04 Bean Pupusas": ['d', 'l', 'b', 'f'],

        #Seaboil
        "O1 Rare Boil": ['b', 'c', 'w', 'o', 'p', 'u', 'h'],
        "02 Delicious Boil": ['r', 'c', 'w', 'o', 'p', 'u', 'h'],

        # Chicken Breast
        "O1 Chicken Breast": ['k', 't', 't', 't', 't', 't', 't', 's'],
        "02 Breaded Chicken Breast": ['k', 't', 't', 't', 't', 't', 't', 'b'],

        # Lasagna
        "O1 The Classic Lasagna": ['p', 's', 'c', 'r', 'p', 's', 'c', 'r', 'p', 's', 'c'],
        "02 Meaty Rome Lasagna": ['p', 's', 'm', 'c', 'r', 'p', 's', 'c', 'r', 'p', 's', 'c'],
        "03 Veggie Lasagna": ['p', 's', 'v', 'c', 'r', 'p', 's', 'c', 'r', 'p', 's', 'c'],
        "04 Spinach Lasagna": ['p', 's', 'n', 'c', 'r', 'p', 's', 'c', 'r', 'p', 's', 'c'],

        # Chili
        "O1 Texas Chili Bowl": ['o', 'm', 'b', 'g', 'n'],
        "02 Chunky Fire Chili": ['o', 'm', 'g', 'r'],
        "03 Sunshine Road": ['o', 'm', 'g', 'r', 'n'],
        "04 Rock n Roll Bowl": ['o', 'm', 'b', 'r', 't'],

        "Bibingka": ['c', 'o'],

        #Huauzontle
        "01 Green": ['h', 'g'],
        "02 Red Hot": ['h', 's'],
        "03 Red Mild": ['h', 't'],
        "04 Cheesy": ['h', 'q'],

        #Medovik
        "Medovik": ['m', 'e', 'd', 'o', 'v', 'i', 'k', 's'],

        #Sashimi
        "O1 Mediterranean": ['s', 'm', 't', 'l', 'u', 'o', 'space', 't', 'c'],
        "02 Floating Islands of Japan": ['s', 'l', 'u', 'q', 'space', 'b', 'h', 't', 'g'],
        "03 Remember California": ['m', 't', 'l', 'w', 'space', 'h', 't', 'c', 'g'],
        "04 Reef Paradise": ['s', 'm', 'l', 'u', 'q', 'w', 'space', 'h', 'c'],
        "05 Classic Fishnet": ['t', 'l', 'o', 'w', 'space', 'b', 'h', 't', 'c'],
        "07 Atlantic Special": ['m', 'u', 'o', 'q', 'w', 'space', 'h', 't', 'c'],
        "06 The Ocean Blue": ['m', 't', 'l', 'q', 'w', 'space', 'b', 'h', 'g'],
        "08 Pacific Coast": ['s', 'm', 't', 'q', 'space', 'b', 't', 'c', 'g'],

        # Sizzling Fajitas
        "O1 Beef Fajita Sizzler": ['o', 'n', 'g', 'r', 'y', 'b'],
        "02 Chicken Fajita Sizzler": ['o', 'n', 'g', 'r', 'y', 'k'],
        "03 Shrimp Sizzler": ['o', 'n', 'g', 'r', 'y', 'h'],
        "04 Deluxe Fajita Sizzler": ['o', 'n', 'g', 'r', 'y', 'b', 'k'],
        # Cookies
        "01 Chocolate Chip Batch": ["c"],
        "02 Dark Chocolate Batch": ["d"],
        "03 Candy Cookie Batch": ["a"],

        "04 Peanut Butter Batch": ["p"],
        "05 Oatmeal Batch": ["o"],
        "06 Sugar Batch": ["s"],

        "Delicious Curry": ["w", "r", "s", "l", "g", "h", "n", "k"],

        "LauLau": ['l', 'l', 'm', 'w'],

        # Corn Pie Chip
        "O1 Corn Chip Classic": ['h', 'c', 'j'],
        "02 Oklahoma Pie": ['h', 'c', 'j', 'n'],
        "03 Freedom Pie": ['c', 'j', 'n'],

        # Sushi
        "O1 California Roll": ['r', 'e', 'v', 's', 'space', 'y', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
                               'c', 'c'],
        "02 Spider Roll": ['r', 'e', 'v', 'space', 'y', 'c', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
                           'c'],
        "03 Ocean Roll": ['r', 'u', 'a', 'c', 'space', 'w', 't', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
                          'c', 'c'],
        "04 Firecracker Roll": ['r', 'e', 'h', 'space', 'w', 'a', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
                                'c', 'c'],
        "05 Drum Roll": ['r', 'a', 'h', 'space', 'a', 't', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
                         'c'],
        "06 Osaka Roll": ['r', 'u', 'h', 'space', 'y', 'e', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
                          'c'],
        "07 Salty Roll": ['r', 'a', 'c', 'h', 'space', 'y', 'a', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
                          'c', 'c'],
        "08 Gated Roll": ['r', 'e', 'u', 'c', 'space', 'w', 'e', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
                          'c', 'c'],
        "09 Slaughter Roll": ['r', 's', 'c', 'space', 'w', 'e', 't', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c',
                              'c', 'c', 'c'],
        "IO Splatter Roll": ['r', 'e', 'a', 'space', 'y', 'w', 'a', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c',
                             'c', 'c', 'c'],
        "11 Champ Roll": ['r', 'e', 's', 'c', 'space', 'c', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
                          'c'],
        "12 Jammy Roll": ['r', 's', 'space', 'y', 'a', 'c', 'space', 'r', 'r', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
                          'c'],

        # Borscht
        "03 Plains": ['c', 'a', 'b', 'g', 'p', 't'],
        "02 Hills": ['c', 'a', 'b', 'e', 't'],
        'O1 Mountains': ['c', 'b', 'l', 'g', 't'],

        "Onigiri": ['r', 'i', 's', 'h', 'n'],

        # Pad Thai
        "Pad Thai": ['n', 'h', 'b', 'r'],
        "O1 Pad Thai": ['p', 'c', 'i', 'l'],
        "02 Pad Thai wlo Cilantro": ['p', 'c', 'i'],

        # Spaghetti
        "Spaghetti and Meatballs Prep": ['s', 'm'],
        "Spaghetti and Meatballs": ['s', 'm', 'r'],

        # Stews
        'O1 Swamp Stew': ['o', 'b', 'e', 'a'],
        "02 Rusty Bolts": ['o', 'b', 'p', 'n'],
        '03 Savannah Glaze': ['o', 'b', 'p', 'e'],
        '04 Alabama Glass': ['o', 'b', 'e', 'a', 'n'],

        # Muffins
        'O1 Blueberry Muffins': ['p', 'l'],
        '02 Bran Muffins': ['p', 'b'],
        '03 Chocolate Muffins': ['p', 'c'],
        '04 Cranberry Muffins': ['p', 'r'],
        '05 Banana Muffins': ['p', 'a'],

        # Solyanka
        'O1 Hamlanka': ['t', 'b', 'p', 'g', 'h', 'n', 'c'],
        '02 Sausaganka': ['t', 'b', 'p', 'g', 'u', 'n', 'c'],
        '03 Veggieanka': ['t', 'b', 'p', 'g', 'n', 'c'],

        'Satay': ['k', 'o', 'p'],

        # Filet Mignon
        'Bacon Wrapped Mignon Rare': ['o', 'b'],
        'Bacon Wrapped Mignon Well Done': ['o', 'b'],
        'Bacon Wrapped Mignon Medium Well': ['o', 'b'],
        'Bacon Wrapped Mignon Medium Rare': ['o', 'b'],
        'Bacon Wrapped Mignon Medium': ['o', 'b'],
        'Bacon Wrapped Mignon Blue Rare': ['o', 'b'],
        'Filet Mignon Rare': ['o', 'f'],
        'Filet Mignon Well Done': ['o', 'f'],
        'Filet Mignon Medium Well': ['o', 'f'],
        'Filet Mignon Medium Rare': ['o', 'f'],
        'Filet Mignon Medium': ['o', 'f'],
        'Filet Mignon Blue Rare': ['o', 'f'],
        'O1 Classic Filet Mignon': ['s', 'c'],
        '02 Foie Gras Filet Mignon': ['s', 'f'],
        '03 Truffle Filet Mignon': ['s', 't'],

        'Veal Marsala': ['v', 'b', 'p', 'f', 'f', 'f', 'r'],
        'Pigs Blood Cakes': ['b', 'p', 'c'],
        'Kachumbari': ['t', 'g', 'p', 'n', 'v'],

        'Hanami Dango': ['g', 'w', 'p'],

        "Moussaka": ['b', 'm', 'p', 'e', 'c'],

        # Salisbury Steak
        "Salisbury Steak Prep": ['u', 's'],
        "O1 Classic Salisbury": ['s', 'g'],
        "02 Mushroom Salisbury": ['s', 'm'],
        "03 Onion Salisbury": ['s', 'o'],

        "Biscuits and Gravy": ['b', 'g'],

        "Cinnamon Roll Prep": ['c'],

        # Oatmeal
        "Oatmeal Prep": ['o'],

        "03 Almond Oatmeal": ['i', 'l'],
        "02 Cranberry Oatmeal": ['i', 'r'],
        "01 Cinnamon Oatmeal": ['i'],

        # Kheer
        "O1 Almond Kheer": ['p', 'i', 'f', 'l'],
        '02 Cranberry Kheer': ['p', 'f', 'r'],
        '03 Rich Kheer': ['p', 'i', 'f', 'r', 'l'],

        # Omelette
        "O1 Classic Omelette": ['e', 'c', 'b', 't', 'm', 'space', 's'],
        "02 Hammy Sunrise": ['e', 'h', 'c', 'b'],
        "03 The Pepper and the Egg": ['e', 'c', 'space', 'g', 'r', 'y', 's'],
        "04 The OozeCheesy Squeezy": ['e', 'z', 'c', 'n', 'space', 'u'],
        "05 Deluxe Omelette": ['e', 'z', 'c', 'b', 't', 'n', 'space', 'u', 's'],
        "06 Ultra Veggie Stacker": ['e', 'z', 't', 'm', 'n', 'space', 'g', 'r', 's'],

        # Tiramisu
        "Classic Tiramisu": ['l', 'c', 'm', 'p', 'l', 'c', 'm', 'p'],

        # Tres Leches
        "01 Vanilla Tres Leches": ['v'],
        "02 Chocolate Tres Leches": ['c'],

        # Food Truck Rice
        "O1 White Rice": ['w', 'r', 's', 'l'],
        "02 Forbidden Rice": ['w', 'f', 's', 'l'],
        "03 Brown Rice": ['w', 'b', 's', 'l'],
        "04 Wild Rice": ['w', 'i', 's', 'l'],

        # Food Truck Beans
        "O1 Black Beans": ['b', 's'],
        "02 Pinto Beans": ['p', 's'],
        "03 Tuscan Beans": ['t', 's'],

        # Ceviche
        "02 Mexican Mix": ['v', 'i', 'g', 'h', 't', 'm'],
        "O1 Spanish Mix": ['c', 'i', 'n', 'h', 't', 'm'],

        "Delicious Menudo": ['p', 'g', 'n', 'u', 'c', 'b', 'l'],

        # Ratatouille
        "Classic Ratatouille": ['r', 'u', 'a', 'i', 't', 'l', 'o', 'e', 'space', 'r', 'i', 'a', 'u', 't', 'o', 'space',
                                'r', 'u', 'a', 'i', 't', 'l', 'o', 'e', 'r', 'i', 'a', 'u', 't', 'o', 'r'],

        # Rote Gruetze
        "Blueberry Rote Gruetze": ['l', 'd'],
        "Strawberry Rote Gruetze": ['s', 'd'],
        "Raspberry Rote Gruetze": ['r', 'd'],
        "Red Currant Rote Gruetze": ['c', 'd'],
        "Blackberry Rote Gruetze": ['b', 'd'],

        # Frozen Banana
        "Frozen Banana Prep": ['b', 'n', 'd'],

        "Poutine Basket": ['g', 'c'],

        # Palak Paneer
        "01 South Way": ['s', 'p', 'g', 'c', 'n', 'd'],
        "02 West way": ['s', 'p', 'c', 'n', 't', 'u'],
        "03 East way": ['s', 'p', 'g', 'c', 't', 'h', 'u'],
        "04 North way": ['s', 'p', 'c', 'n', 't', 'h', 'u'],

        # Boba Tea
        "O1 Mango Tea": ['b', 'i', 'space', 'a', 'space', 's'],
        "02 Strawberry Tea": ['b', 'i', 'space', 's', 'space', 's'],
        "03 Matcha Tea": ['b', 'i', 'space', 'm', 'space', 's'],
        "04 Blueberry Tea": ['b', 'i', 'space', 'l', 'space', 's'],
        "05 Thai Milk": ['b', 'i', 'space', 'h', 'space', 's'],
        "06 Taro": ['b', 'i', 'space', 't', 'space', 's'],
        "07 Coconut": ['b', 'i', 'space', 'o', 'space', 's'],
        "09 Almond Milk": ['b', 'i', 'space', 'space', 'l', 's'],
        "08 Pearl": ['b', 'i', 'space', 'p', 'space', 's'],
        "IO Fruit Tea": ['b', 'i', 'space', 'space', 'f', 's'],
        "11 Milk Tea": ['b', 'i', 'space', 'space', 'm', 's'],
        "12 Mocha": ['b', 'i', 'space', 'space', 'o', 's'],
        "13 Jasmine": ['b', 'i', 'space', 'space', 'j', 's'],
        "14 Honeydew": ['b', 'i', 'space', 'space', 'h', 's'],

        # Desert Shooter
        "O1 Double Mocha Cheesecake": ['m', 'm', 'c'],
        "02 Tiramisu Creme": ['t', 't', 'b'],
        "03 Banapple": ['a', 'b', 'b'],
        "04 Dark Creamy Goodness": ['m', 'm', 'b'],
        "05 Chocolate Lime Key": ['m', 'm', 'k'],
        "06 The Chicago Sampler": ['c', 'b', 'k'],
        "07 Mexican Paradise": ['m', 'a', 't'],
        "08 The San Francisco Sampler": ['t', 'b', 'k'],
        "09 Dark Mess": ['m', 'm', 'm'],
        "IO Triple Shot": ['b', 'b', 'b'],

        "Classic Tourtiere": ['m', 'n', 'e', 'p', 'a', 'c'],

        "Tandoori Chicken": ['k', 'r', 's', 'u', 'y', 'g', 'm'],

        "Mapo Tofu": ['r', 'm', 't', 'c', 'p'],

        "Pho Prep": ['n', 'b', 'p'],

        "Htapothi sti Skhara": ['o', 'h', 'u'],

        # Sausage Slices
        "O1 Classic Sausage": ['u'],
        "02 Black Pudding": ['b'],

        # Ramen"
        # "02 Kakuni Spa": ['r', 'o', 'k'],
        # "04 Salty Coast": ['r', 'o', 'c', 'm'],
        # "05 Spicy Bowl": ['r', 'o', 'p', 'k']
        # "08 Hot Afternoon": []

        # Deluxe Nachos
        "01 Classic Nachos": ['q', 'b', 'space', 'm', 'u'],
        "02 South of the Border": ['q', 't', 'space', 'k', 's'],
        "03 Beefarita": ['q', 'r', 'a', 'space', 'b', 's'],
        "04 Mexican Tornado": ['q', 'v', 'n', 't', 'space', 'k', 'b'],
        "05 Cheesy Hurricane": ['q', 'r', 'n', 't', 'space', 'h', 's', 'u'],
        "06 Cheddar Chips": ['q'],
        "07 Beantown": ['q', 'b', 'a', 'space', 'k'],
        "08 Meatalicious": ['q', 'space', 'k', 'h', 'b', 'm'],
        "09 Meatalicious Supreme": ['q', 'r', 'v', 'n', 't', 'space', 'k', 'h', 'b', 'm'],
        'IO Extreme Fajitas': ['q', 'v', 'space', 'k', 'b', 's', 'u'],
        "11 Infinite Nachos": ['q', 'b', 'r', 'v', 'a', 'n', 't', 'space', 'k', 'h', 'b', 'm', 's'],
        "12 Queso me Mucho": ['q', 'space', 'k', 'b'],

        # Pizza
        'O1 Classic Pepperoni': ['h', 'r', 'c', 'space', 'r'],
        '02 Meat Lovers': ['s', 'r', 'c', 'space', 'p', 'u', 'g', 'b'],
        "03 Veggie Tomato": ['t', 'r', 'c', 'space', 'space', 'm', 'v', 's', 'g', 'r'],
        '04 Ham and Pineapple': ['h', 'r', 'c', 'space', 'h', 'i'],
        "05 Supreme": ['h', 'r', 'c', 'space', 'g', 'space', 'm', 'n', 'v', 'g', 't'],
        "06 Beefy Tomato": ['h', 'r', 'c', 'space', 'u', 'g', 'r', 'space', 'r', 't'],
        "07Pesto Pepperoni": ['h', 'e', 'c', 'space', 'p'],
        "08 Pesto and Anchovies": ['h', 'e', 'c', 'space', 'a', 'space', 'm', 'n', 'g'],
        "09 Green Gardens": ["t", 'e', 'c', 'space', 'r', 'space', 'v', 's', 'g'],
        "IOMeatesto": ['s', 'e', 'c', 'space', 'p', 'u', 'b', 'space', 'g', 'r'],
        "11 New Jersey Classic": ['s', 'e', 'c', 'space', 'r', 'a', 'b', 'space', 'n', 'i'],
        "12 Light and Crisp": ['t', 'e', 'c', 'space', 'k', 'space', 'm'],
        "13 White Desert": ['h', 'a', 'c', 'space', 'p', 'b'],
        "14 Italian Tour": ['s', 'a', 'c', 'space', 'g', 'r', 'k', 'space', 'v', 'g', 'r'],
        "15 Creamy Pie": ['s', 'a', 'c', 'space', 'r'],
        "16 Meaty Alfredo": ['h', 'a', 'c', 'space', 'p', 'g', 'k', 'b'],
        "17 Mega Queso": ['s', 'q', 'c', 'space', 'u', 'r', 'space', 'n', 's', 't'],
        "18 Meaty Queso": ['h', 'q', 'c', 'space', 'p', 'g', 'k', 'b'],
        "19 DeLight Queso": ['t', 'q', 'c', 'space', 'space', 'm', 'v', 's', 'r'],
        "20Ham and Cheese": ['h', 'q', 'c', 'space', 'h', 'r'],

    }

    print("Recipe Book initialized: ", recipeBook)
    return recipeBook
