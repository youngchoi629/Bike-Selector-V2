# *************************************
#
# Youngshin Choi
#
# Project name: Road Bike Selector
#
# PROJ DESC: The name of my projects is "Road bike selelctor".
#            The purpose of this prgram is to provide a recommendation of a series of road bikes
#            based on the input of the user, which is genre of road bike and price.
#            Another purpose is to recommend a frame size based on the user's height,
#            and also recommend a gear ratio for the user's riding terrain.
# *************************************

from re import L
import string
import time

pass_on = False

# *************************************
# Function: animation
# Description: A function that receives a string and displays the string letter by letter,
#              creating an animation as if someone is typing.
# Input: The string that the selector is saying to the user
# Output: Showing the string letter by letter as an animation
# *************************************
def animation(str):
    for i in range(len(str)):
        print(str[i], end = "")
        time.sleep(0.05)

# *************************************
# Reading the txt files, storing them into lists,
# and closing the files
# *************************************

#Lists where the information from the txt files will be stored in
giant_all = []
giant_aero = []
giant_endu = []

splzd_all = []
splzd_aero = []
splzd_endu = []

trek_all = []
trek_aero = []
trek_endu = []

canyon_all = []
canyon_aero = []
canyon_endu = []

cannon_all = []
cannon_aero = []
cannon_endu = []

#Opening and reading txt files
f_g_1 = open("giant_all.txt", "r")
f_g_2 = open("giant_aero.txt", "r")
f_g_3 = open("giant_endu.txt", "r")

f_s_1 = open("splzd_all.txt", "r")
f_s_2 = open("splzd_aero.txt", "r")
f_s_3 = open("splzd_endu.txt", "r")

f_t_1 = open("trek_all.txt", "r")
f_t_2 = open("trek_aero.txt", "r")
f_t_3 = open("trek_endu.txt", "r")

f_cnyn_1 = open("canyon_all.txt", "r")
f_cnyn_2 = open("canyon_aero.txt", "r")
f_cnyn_3 = open("canyon_endu.txt", "r")

f_cann_1 = open("cannon_all.txt", "r")
f_cann_2 = open("cannon_all.txt", "r")
f_cann_3 = open("cannon_endu.txt", "r")


#Saving read contents into list
giant_all = list(f_g_1)
giant_aero = list(f_g_2)
giant_endu = list(f_g_3)

splzd_all = list(f_s_1)
splzd_aero = list(f_s_2)
splzd_endu = list(f_s_3)

trek_all = list(f_t_1)
trek_aero = list(f_t_2)
trek_endu = list(f_t_3)

canyon_all = list(f_cnyn_1)
canyon_aero = list(f_cnyn_2)
canyon_endu = list(f_cnyn_3)

cannon_all = list(f_cann_1)
cannon_aero = list(f_cann_2)
cannon_endu = list(f_cann_3)

#close files
f_g_1.close()
f_g_2.close()
f_g_3.close()
f_s_1.close()
f_s_2.close()
f_s_3.close()
f_t_1.close()
f_t_2.close()
f_t_3.close()
f_cnyn_1.close()
f_cnyn_2.close()
f_cnyn_3.close()
# *************************************
# Function: edit_lst
# Description: A function to edit the list to a format of: [Name of bicycle, price]
# Input: The list that needs to be edited to the format based on the user's selection
# Output: The edited list in the format
# *************************************
def edit_lst(lst):
    new_lst = [x[:-1] for x in lst]
    return new_lst


# *************************************
# Function: prices
# Description: A function for sorting out the bicycles that fit in the price range
# Input: Lists of bicycles that are in the genre the user selected, the minimum and maximum price the user entered
# Output: Lists that are in the price range the user entered
# *************************************
def prices(giant, splzd, trek, canyon, cannon, min, max):
    giant_prices = []
    splzd_prices = []
    trek_prices = []
    canyon_prices = []
    cannon_prices = []
    n = 1
    while n <= len(giant):
        if int(giant[n]) >= min and int(giant[n]) <= max:
            giant_prices.append(giant[n-1])
            giant_prices.append("\t$")
            giant_prices.append(giant[n])
            giant_prices.append("\n")
        n += 3
    n = 1
    while n <= len(splzd):
        if int(splzd[n]) >= min and int(splzd[n]) <= max:
            splzd_prices.append(splzd[n-1])
            splzd_prices.append("\t$")
            splzd_prices.append(splzd[n])
            splzd_prices.append("\n")
        n += 3
    n = 1
    while n <= len(trek):
        if int(trek[n]) >= min and int(trek[n]) <= max:
            trek_prices.append(trek[n-1])
            trek_prices.append("\t$")
            trek_prices.append(trek[n]) 
            trek_prices.append("\n")
        n += 3
    n = 1
    while n <= len(canyon):
        if int(canyon[n]) >= min and int(canyon[n]) <= max:
            canyon_prices.append(canyon[n-1])
            canyon_prices.append("\t$")
            canyon_prices.append(canyon[n]) 
            canyon_prices.append("\n")
        n += 3
    n = 1
    while n <= len(cannon):
        if int(cannon[n]) >= min and int(cannon[n]) <= max:
            cannon_prices.append(cannon[n-1])
            cannon_prices.append("\t$")
            cannon_prices.append(cannon[n]) 
            cannon_prices.append("\n")
        n += 3
    return giant_prices, splzd_prices, trek_prices, canyon_prices, cannon_prices

# *************************************
# Function: sizes
# Description: A function to recommend a frame size based on the user's height
# Input: The user's height
# Output: The recommended frame size
# *************************************
def sizes(height):
    print("\n")
    if height >= 150 and height <= 165:
        animation("Your suggested size is an XS to an S.")
    elif height > 165 and height <= 175:
        animation("Your suggested size is an S to a M.")
    elif height > 175 and height <= 185:
        animation("Your suggested size is an M to a L.")
    elif height > 185 and height <= 195:
        animation ("Your suggested size is an L to an XL.")
    elif height > 195:
        animation ("Your suggested size is an XL.")
    else:
        animation("Sorry, I could not find a size that would fit your height.")

# *************************************
# Function: gear
# Description: A funcrion for recommending the gear ratio for the user based on their riding terrain.
# Input: Type of terrain
# Output: The recommended gear ratio
# *************************************
def gear(terrain):
    print("\n")
    if terrain == "mountainous":
        animation("I see you are a climber.")
        print("\n")
        time.sleep(0.3)
        animation("I would recommend a 50-34 chainset.")
        print("")
        time.sleep(0.3)
        animation("And a 11-32 or a 11-34 cassette.")

    elif terrain == "flat":
        animation("Ah, nothing is as safistfying as crusing on flat roads.")
        print("\n")
        time.sleep(0.3)
        animation("I would recommend a 52-36 or a 53-39 chainset.")
        print("")
        time.sleep(0.3)
        animation("And a 11-28 or if you have very strong legs, even a 11-25 cassette.")

    elif terrain == "hilly":
        animation("Mixed hilly terrain? That's the best one!")
        print("\n")
        time.sleep(0.3)
        animation("I would recommend a 50-34 or a 52-36 chainset.")
        print("")
        time.sleep(0.3)
        animation("Combine that with a 11-28 or 11-30 cassette, and you should be good!")

# The Main program
# The starting screen
print("\n")
animation("====================================")
print("\n\n")
print(" __o            __o            __o")
print("-\<,           -\<,           -\<,")
print("O/ O...........O/ O...........O/ O")
print("      THE ROAD BIKE SELECTOR")
time.sleep(1)
print("\n")
animation("Greetings! Welcome to THE ROAD BIKE SELECTOR.")
time.sleep(1)
print("")
animation("Here, I will help find you the perfect road bike to suit your needs.")
time.sleep(1)
print("")
animation("My data is from five reputable bike brands.")
time.sleep(1)

# Briefly explains the different road bike types
# Asks the user for their desired road bike type
while pass_on != True:
    print("\n\n")
    animation("First, let's find out what kind of bike you would want.")
    print("")
    animation("An all-rounder is the jack of all trades, typically combined with light weight and some aero features.")
    print("")
    animation("If you want to ride like a rocketship on flats, an aero bike will be your best pick.")
    print("")
    animation("If you are want to ride long distances comfortably, go for an endurance bike.")
    print("")
    print("\n")
    animation("Please enter your choice (All-rounder, Aero, Endurance): ")
    bike_type = input()
    bike_type = bike_type.lower()
    # Constant loop until the user types in a valid response
    if bike_type == 'all-rounder' or bike_type == 'allrounder' or bike_type == 'aero' or bike_type == 'endurance':
        pass_on = True
    else:
        animation("Hmm.... I don't recognize that. Please enter a valid response.")

# Action when user selects All-rounder
if bike_type == 'all-rounder' or 'allrounder':
    giant_all = edit_lst(giant_all)
    splzd_all = edit_lst(splzd_all)
    trek_all = edit_lst(trek_all)
    canyon_all = edit_lst(canyon_all)
    cannon_all = edit_lst(cannon_all)
    giant = giant_all
    splzd = splzd_all
    trek = trek_all
    canyon = canyon_all
    cannon = cannon_all

# Action when user selects aero
if bike_type == 'aero':
    giant_aero = edit_lst(giant_aero)
    splzd_aero = edit_lst(splzd_aero)
    trek_aero = edit_lst(trek_aero)
    canyon_aero = edit_lst(canyon_aero)
    cannon_aero = edit_lst(cannon_aero)
    giant = giant_aero
    splzd = splzd_aero
    trek = trek_aero
    canyon = canyon_aero
    cannon = cannon_aero

# Action when user selects endurance
if bike_type == 'endurance':
    giant_endu = edit_lst(giant_endu)
    splzd_endu = edit_lst(splzd_endu)
    trek_endu = edit_lst(trek_endu)
    canyon_endu = edit_lst(canyon_endu)
    cannon_endu = edit_lst(cannon_endu)
    giant = giant_endu
    splzd = splzd_endu
    trek = trek_endu
    canyon = canyon_endu
    cannon = cannon_endu

time.sleep(0.5)
print("\n")
animation("Ahh, Great choice!")

# Asks the price range of the bicycle
time.sleep(0.3)
print("\n\n")
animation("The next important thing when you are buying a bike is probably how much you are willing to spend.")
time.sleep(1)
print("")
animation("You know, after all, money's always the biggest concern ;)")
time.sleep(0.5)
print("")
animation("Please enter the range of the price (USD).")
time.sleep(0.5)
print("\n")
# User enters minimum and maximum price
animation("Minimum price: ")
price_range_min = int(input())
animation("Maximum price: ")
price_range_max = int(input())

# Asks for valid prices when the minimum price is larger than the maximum price
while price_range_min >= price_range_max:
    animation("Please enter a valid min and max price (USD).\n")
    time.sleep(0.5)
    print("\n")
    animation("Minimum price: ")
    price_range_min = int(input())
    animation("Maximum price: ")
    price_range_max = int(input())

giant_prices = []
splzd_prices = []
trek_prices = []
canyon_prices = []
cannon_prices = []
# Calls function "prices" and returns the bikes that fit in the price range
giant_prices, splzd_prices, trek_prices, canyon_prices, cannon_prices = prices(giant, splzd, trek, canyon, cannon, price_range_min, price_range_max)
print("\n")
# Prints out the results
animation("Getting your results..........")
time.sleep(1.5)
print("\n")
total = len(giant_prices) + len(splzd_prices) + len(trek_prices) + len(canyon_prices) + len(cannon_prices)
animation("I found %d results in total. Here are the bikes: " %total)
print("\n")
print("<Giant>")
for g in range(len(giant_prices)):
    print(giant_prices[g], end = "")
print("\n")
print("<Specialized>")
for s in range(len(splzd_prices)):
    print(splzd_prices[s], end = "")
print("\n")
print("<Trek>")
for t in range(len(trek_prices)):
    print(trek_prices[t], end = "")
print("\n")
print("<Canyon>")
for cnyn in range(len(canyon_prices)):
    print(canyon_prices[cnyn], end = "")
print("\n")
print("<Cannondale>")
for cann in range(len(cannon_prices)):
    print(cannon_prices[cann], end = "")
time.sleep(5)

# Asks the height of the user
print("\n\n")
animation("Now that you have chosen your preferred type of road bike and price range,")
print("")
time.sleep(0.3)
animation("please tell me your height.")
print("")
time.sleep(0.2)
animation("This is to determine your frame size.")
print("")
animation("Enter height (in cms):")
height = int(input())
# Calls the function "sizes"
sizes(height)

# Asks the terrain the user is riding
print("\n\n")
time.sleep(1)
animation("Now you have chosen your desired road bike type and size,")
print("")
time.sleep(0.3)
animation("Please tell me the kind of terrain are you going to ride your bike.")
print("")
time.sleep(0.3)
animation("There are gear ratios that are best suited for each terrain.")
pass_on = False
# Constant loop until user types in valid response
while pass_on != True:
    print("")
    animation("Which word best describes your terrain? (Mountainous, Hilly, Flat): ")
    terrain = str(input())
    terrain = terrain.lower()
    if terrain == "mountainous" or terrain == "hilly" or terrain == "flat":
        pass_on = True
    else:
        print("\n")
        animation("Sorry, but I didn't quite understand that. Please type in a valid response.")
gear(terrain)

time.sleep(0.6)
print("\n\n")
animation("Last but not the least........")
print("")
animation("You can learn more about the bikes and find more information, by visiting the manufacterers' websites.")
time.sleep(0.5)
print("")

pass_on = False
# Asks if the user wants to visit the websites
while pass_on != True:
    animation("If you want to visit the website, please press Y. If not, please press N.")
    visit_site = str(input(""))
    visit_site = visit_site.lower()
    # Constant loop until user types in valid response
    if visit_site == "y" or visit_site == "n":
        pass_on = True
    else:
        print("\n")
        animation("I didn't quite get that. Please enter a valid response.")
        print("")

# Displays link when user types in y, doesn't if user types in n
if visit_site == "y":
    print("\n")
    animation("Very well! Try visiting these links:")
    time.sleep(1)
    print("\n")
    print("https://www.giant-bicycles.com/us/bikes/road-bikes/performance-and-racing")
    print("https://www.specialized.com/us/en/shop/bikes/road-bikes/performance-road-bikes/c/roadperformance")
    print("https://www.trekbikes.com/us/en_US/bikes/road-bikes/performance-road-bikes/c/B260/")
    print("https://www.canyon.com/en-us/road-bikes/")
    print("https://www.cannondale.com/en-eu/bikes/road?activeFilters=subcategory~Race")

# The end screen
print("\n\n")
animation("Thank you very much for using THE ROAD BIKE SELECTOR.")
print("")
time.sleep(0.3)
animation("Well then, ride safe, and I hope to see you again!")
print("")
time.sleep(0.3)
animation("==========================================")
print("\n\n")
animation("Shutting down.............................")
print("\n")