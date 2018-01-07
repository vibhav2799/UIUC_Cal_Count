# Importing Browser from the splinter below
from splinter import Browser
import re

#1. Breads, 2. Desserts 3. Entrees 4. Vegetables 5. Starches 6. Sauces 7. Toppings 8. Fruits 9. Cereal 10. Others
#"1. Busey-Evans, 2. FAR, 3. Ikenberry, 4. ISR, 5. LAR, 6. PAR"

# Using an array to store the 6 dining locations available on the website

a = ['Busey-Evans', 'FAR', 'Ikenberry', 'ISR', 'LAR', 'PAR']
print ('Enter Location: 1. Busey-Evans 2. FAR 3. Ikenberry 4. ISR 5. LAR 6. PAR')
loc = input("Select an option: ")

# Creating an object b
b = Browser()
url = "http://housing.illinois.edu/Dining/Menus/Dining-Halls"
# The object opens Firefox to the given url
b.visit(url)
# A button is created which is positioned at the drop-down menu for various locations
button = b.find_by_name('pagebody_0$ddlLocations')
button.click()
# Changing the options in the drop down menu using the array elements
b.find_option_by_text(a[int(loc) - 1]).first.click()
buttonEnter = b.find_by_name('pagebody_0$btnSubmit')
buttonEnter.click()
div = b.find_by_id("MyHousingForm")
arr = ["Breads", "Desserts", "Entrees", "Vegetables", "Starches", "Sauces", "Toppings", "Fruits", "Cereals",
       "Others",
       "Soups"]

print ('Enter Type: ')
print('1. Breads, 2. Desserts 3. Entrees 4. Vegetables 5. Starches 6. Sauces 7. Toppings 8. Fruits 9. Cereal 10. Others')
dish_type = input("Select an option: ")

item = re.findall(arr[int(dish_type) - 1] + '.+', div.text)
print(item)
