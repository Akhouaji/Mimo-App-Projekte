italian_food= ["Pasta Bolognese", "Pepperooni pizza", "Margherita pizza", "Lasagna"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]

def find_meal(name, menu):
  if name in menu:
    return name
  else:
    None

def select_meal(name, food_type):
  if food_type == "Italian":
    find_meal(name, italian_food)
    return find_meal(name, italian_food)
  
  elif food_type == "Indian":
    return find_meal(name, indian_food)
  
  else:
    None

def display_available_meals(food_type):

  if food_type == "Italian":
    print("Available Italian Meals: ")
    for meal in italian_food:
      print(meal)
  
  elif food_type == "Indian":
    print("Available Indian Meals: ")
    for meal in indian_food:
      print(meal)

  else:
    print("Invalid food type")
  

def create_summary(name, amount, food_type):
  order = select_meal(name, food_type)
  if order:
    return f"You have ordered {amount} of {name} ."
  else:
    return "Meal not found"

print("Welcome to the Food Order System!")
type_input = input("What kind of Food do you want? ")

display_available_meals(type_input)

name_input = input("Enter the name of the meal you want to order: ")
amount_input = int(input("Choose the amount: "))
result = create_summary(name_input, amount_input, type_input)
print(result)