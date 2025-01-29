# Zybooks stumpers

# 22.10 LAB*: Program: Cooking measurement converter
   

# https://learn.zybooks.com/zybook/WGUC859v4/chapter/22/section/10

###########

# FIXME (1): Finish reading other items into variables, then output the three ingredients

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))

water = float(input('Enter amount of water (in cups):\n'))

agave = float(input('Enter amount of agave nectar (in cups):\n'))

servings = float(input('How many servings does this make?\n\n'))

# Sample data:
# 2 lemon
# 16 water
# 2.5 agave
# 6 servings make

# should be: Lemonade ingredients - yields 6.00 servings
print(f"Lemonade ingredients - yields {servings:.2f} servings")

# should be: 2.00 cup(s) lemon juice
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")

# should be: 16.00 cup(s) water
print(f"{water:.2f} cup(s) water")

# should be: 2.50 cup(s) agave nectar
print(f"{agave:.2f} cup(s) agave nectar\n")



# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients


# test data 48
howmanservings = float(input("How many servings would you like to make?\n\n"))

#calc lemon juice from input, HOW WOULD YOU GO ABOUT FIGURING OUT THE EQUATION 
# IF 48 servings is 16 cups how much is 1 serving, well divide...
lemon2 = howmanservings / 3

# Calc water... dont freaking know
# 48 input 
# 128 output
# 2.66??

# Calc agave... dont freaking know
# 48 / 20
# agave2 = 2.4 ? 0.4166666666666667 ?
agave2 = 0.4166666666666667 * howmanservings # this doesnt really solve it

#should be Lemonade ingredients - yields 48.00 servings
print(f"Lemonade ingredients - yields {howmanservings:.2f} servings")

# should be 16.00 cup(s) lemon juice
print(f"{lemon2:.2f} cup(s) lemon juice")

# should be 128.00 cup(s) water
#8.00 cup(s) water

# should be 20.00 cup(s) agave nectar
print(f"{agave2:.2f} cup(s) agave nectar")




# FIXME (3): Convert and output the ingredients from (2) to gallons
   
