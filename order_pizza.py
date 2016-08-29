PIZZAS = (
	{ 
		"name": "cheese pizza", 
		"cost": 5.00
	},
	{
		"name": "meat pizza", 
		"cost": 8.00
	},
)

my_pizzas = []

def display_invalid_option(menu_selection):
	if menu_selection.isdigit():
		print("\nI don't want anything out of range, foo. ".format(menu_selection))
	else:
		print("\nI want all the digits, foo. Try again. ".format(menu_selection))


def is_valid_pizza(pizza_selection, pizzas): #question on VARIABLES - pizzas & PIZZAS
		return pizza_selection.isdigit() and int(pizza_selection)-1 < len(pizzas)

def display_pizzas(pizzas):
	if len(pizzas) > 0:
		for index, pizza in enumerate(pizzas):
			print("{}: {} - cost: ${:,.2f}".format(index+1, pizza["name"], pizza["cost"]))
	else:
		print("WHOA!!?\nNo pizzas added, yet.")

def display_total_cost(pizzas): #question on LIST COMPREHENSIONS
	total_cost = sum([pizza["cost"] for pizza in pizzas])
	print("----------")
	print("total cost: ${:,.2f}".format(total_cost))

def display_order(pizzas):
	display_pizzas(pizzas)
	display_total_cost(pizzas)
	print("\n")

def order_pizza(pizzas):
	if len(my_pizzas) > 0:
		print("Thanx, foo.")
		return True
	else:
		print("Add a pizza, foo.")
		return False

def add_to_order():
	"""
	prompts for adding pizza to the order
	"""
	while True:
		print("\n")
		display_pizzas(PIZZAS)
		print("0: Go Back")

		pizza_selection = input("\nWhich pizza, foo? ")

		if pizza_selection == "0":
			break
		elif is_valid_pizza(pizza_selection, PIZZAS):
			my_pizzas.append(PIZZAS[int(pizza_selection)-1])
		else:
			display_invalid_option(pizza_selection)

def remove_from_order():
	"""
	remove a pizza from my_pizzas based on user's input
	"""
	while True:
		print("\n")
		display_pizzas(my_pizzas)
		print("0: Go Back")

		pizza_selection = input("\nWhich pizza do ya wanna remove, foo? ")

		if pizza_selection == "0":
			break
		elif is_valid_pizza(pizza_selection, my_pizzas):
			del (my_pizzas[int(pizza_selection)-1])
		else:
			display_invalid_option(pizza_selection)


def main():
	global my_pizzas
	MENU_ITEMS = (
		"1: add pizza to order",
		"2: remove pizza from order",
		"3: display order",
		"4: order pizza",
		"0: exit",
		)

	while True:
		for menu_items in MENU_ITEMS:
			print(menu_items)

		menu_selection = input("\nPlease select an option from above: ")

		if menu_selection == "0":
			break
		elif menu_selection == "1":
			add_to_order()
		elif menu_selection == "2":
			remove_from_order()
		elif menu_selection == "3":
			display_order(my_pizzas)
			print("\n")
		elif menu_selection == "4":
			display_order(my_pizzas)
			if order_pizza(my_pizzas):
				my_pizzas = []
		else:
			display_invalid_option(menu_selection)

if __name__ == "__main__": #question on what __name__ actually is doing
	main()