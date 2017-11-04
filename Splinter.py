# Importing Browser from the splinter below
from splinter import Browser
# Using an array to store the 6 dining locations available on the website
a = ['Busey-Evans', 'FAR', 'Ikenberry', 'ISR', 'LAR', 'PAR']
# Creating an object b
b = Browser()
url = "http://housing.illinois.edu/Dining/Menus/Dining-Halls"
# The object opens Firefox to the given url
b.visit(url)
# A button is created which is positioned at the drop-down menu for various locations
button = b.find_by_name('pagebody_0$ddlLocations')
button.click()
# Changing the options in the drop down menu using the array elements
b.find_option_by_text(a[3]).first.click()


buttonEnter = b.find_by_name('pagebody_0$btnSubmit')
buttonEnter.click()

import urllib
import json

urllib.urlopen()

