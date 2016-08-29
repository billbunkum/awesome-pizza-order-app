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

def display_invalid_option(menu_selection):
	if menu_selection.isdigit():
		print("\nI don't want anything but 0-4, foo. ".format(menu_selection))
	else:
		print("\nI want all the digits, foo. Try again. ".format(menu_selection))


def is_valid_pizza(pizza_selection, pizzas): #question on pizzas & PIZZAS
		return pizza_selection.isdigit() and int(pizza_selection)-1 < len(pizzas)

def add_to_order():
	"""
	prompts for adding pizza to the order
	"""

	while True:
		print("\n")
		for index, pizza in enumerate(PIZZAS):
			print("{}: {}".format(index+1, pizza["name"]))
		print("0: Go Back")

		pizza_selection = input("\nWhich pizza, foo? ")

		if pizza_selection == "0":
			break
		elif is_valid_pizza(pizza_selection, PIZZAS):
			my_pizzas.append(PIZZAS[int(pizza_selection) - 1])
		else:
			display_invalid_option(pizza_selection)

def main():
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
			pass
		elif menu_selection == "3":
			pass
		elif menu_selection == "4":
			pass
		else:
			display_invalid_option(menu_selection)

if __name__ == "__main__":
	main()