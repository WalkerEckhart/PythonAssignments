# 1. TASK: print "Hello World"
print('Hello, World!')
# 2. print "Hello Noelle!" with the name in a variable
name = "Walker"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
number = 26
print("Hello", number)	# with a comma
print("Hello " + str(number))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
my_string = "I love to eat {} and {}"
fave_food1 = "sushi"
fave_food2 = "pizza"
print(my_string.format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string
