#Author: Charlie Ta
#Project: Lab 2

# Main function
def main():
    # your code will go here

    # constant variables

    NONE_CODE = 0
    HAMBURGER_CODE = 1
    HOTDOG_CODE = 2
    GRILLEDCHICKEN_CODE = 3

    FRENCHFRIES_CODE = 1
    TATERTOTS_CODE = 2
    POTATOWEDGES_CODE = 3

    SODA_CODE = 1
    MILK_CODE = 2
    WATER_CODE = 3

    CHEESECAKE_CODE = 1
    CAKE_CODE = 2
    ICECREAM_CODE = 3

    NONE_PRICE = 0
    HAMBURGER_PRICE = 5.50
    HOTDOG_PRICE = 3.00
    GRILLEDCHICKEN_PRICE = 4.00

    FRENCHFRIES_PRICE = 1.25
    TATERTOTS_PRICE = 1.00
    POTATOWEDGES_PRICE = 1.35

    SODA_PRICE = 0.50
    MILK_PRICE = 1.00
    WATER_PRICE = 0.25

    CHEESECAKE_PRICE = 3.50
    CAKE_PRICE = 2.50
    ICECREAM_PRICE = 1.50


    total_price = 0.00



    # Welcome the user to the restaurant
    print("WELCOME TO KWIK-E MART!!!")

    #Prompt for the main dish
    print("What would you like for your main dish? ")
    print("Enter %d for none" % NONE_CODE)
    print("Enter %d for a hamburger" % HAMBURGER_CODE)
    print("Enter %d for a hot dog" % HOTDOG_CODE)
    print("Enter %d for a grilled chicken" % GRILLEDCHICKEN_CODE)
    main_dish_choice = int(input(""))



    #Prompt for the side dish
    print("What would you like for your side dish?")
    print("Enter %d for none" % NONE_CODE)
    print("Enter %d for french fries" % FRENCHFRIES_CODE)
    print("Enter %d for tater tots" % TATERTOTS_CODE)
    print("Enter %d for potato wedges" % POTATOWEDGES_CODE)
    side_dish_choice = int(input(""))

    #Prompt for the drink
    print("What would you like for your drink?")
    print("Enter %d for none" % NONE_CODE)
    print("Enter %d for soda" % SODA_CODE)
    print("Enter %d for milk" % MILK_CODE)
    print("Enter %d for water" % WATER_CODE)
    drink_choice = int(input(""))

    #Prompt for the dessert
    print("What would you like for your dessert?")
    print("Enter %d for none" % NONE_CODE)
    print("Enter %d for cheesecake" % CHEESECAKE_CODE)
    print("Enter %d for cake" % CAKE_CODE)
    print("Enter %d for ice cream" % ICECREAM_CODE)
    dessert_choice = int(input(""))

    #calculation section


    #Output section
    if main_dish_choice == NONE_CODE:
        print("You didn't choose anything for your main dish.")
    elif main_dish_choice == HAMBURGER_CODE:
        print("You chose hamburger as your main dish.")
    elif main_dish_choice == HOTDOG_CODE:
        print("You chose hot dog as your main dish.")
    elif main_dish_choice == GRILLEDCHICKEN_CODE:
        print("You chose grilled chicken sandwich as your main dish.")

    if side_dish_choice == NONE_CODE:
        print("You didn't choose anything for your side dish.")
    elif side_dish_choice == FRENCHFRIES_CODE:
        print("You chose french fries as your side dish.")
    elif side_dish_choice == TATERTOTS_CODE:
        print("You chose tater tots as your side dish.")
    elif side_dish_choice == POTATOWEDGES_CODE:
        print("You chose potato wedges as your side dish.")

    if drink_choice == NONE_CODE:
        print("You didn't choose anything for your drink.")
    elif drink_choice == SODA_CODE:
        print("You chose soda as your drink.")
    elif drink_choice == MILK_CODE:
        print("You chose milk as your drink.")
    elif drink_choice == WATER_CODE:
        print("You chose water as your drink.")

    if dessert_choice == NONE_CODE:
        print("You didn't choose anything for your dessert.")
    elif dessert_choice == CHEESECAKE_CODE:
        print("You chose cheesecake as your dessert.")
    elif dessert_choice == CAKE_CODE:
        print("You chose cake as your dessert.")
    elif dessert_choice == ICECREAM_CODE:
        print("You chose ice cream as your dessert.")

    #Calculation Section
    if main_dish_choice == NONE_CODE:
        total_price += NONE_PRICE
    elif main_dish_choice == HAMBURGER_CODE:
        total_price += HAMBURGER_PRICE
    elif main_dish_choice == HOTDOG_CODE:
        total_price += HOTDOG_PRICE
    elif main_dish_choice == GRILLEDCHICKEN_CODE:
        total_price += GRILLEDCHICKEN_PRICE

    if side_dish_choice == NONE_CODE:
        total_price += NONE_PRICE
    elif side_dish_choice == FRENCHFRIES_CODE:
        total_price += FRENCHFRIES_PRICE
    elif side_dish_choice == TATERTOTS_CODE:
        total_price += TATERTOTS_PRICE
    elif side_dish_choice == POTATOWEDGES_CODE:
        total_price += POTATOWEDGES_PRICE

    if drink_choice == NONE_CODE:
        total_price += NONE_PRICE
    elif drink_choice == SODA_CODE:
        total_price += SODA_PRICE
    elif drink_choice == MILK_CODE:
        total_price += MILK_PRICE
    elif drink_choice == WATER_CODE:
        total_price += WATER_PRICE

    if dessert_choice == NONE_CODE:
        total_price += NONE_PRICE
    elif dessert_choice == CHEESECAKE_CODE:
        total_price += CHEESECAKE_PRICE
    elif dessert_choice == CAKE_CODE:
        total_price += CAKE_PRICE
    elif dessert_choice == ICECREAM_CODE:
        total_price += ICECREAM_PRICE

    print("Your total is $%.2f" % total_price)

    print("Thank you, come again!")


# Boilerplate used to run the main function
if __name__ == "__main__":
    main()