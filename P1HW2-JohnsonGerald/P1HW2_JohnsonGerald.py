
#Finding out the Number of Pizzas I need to order for my group of Students.
#February 23, 2022
#CTI-110 P1HW2-Pizza Order
#Ricardo Rivera
#
##########################Pseudo-Code################################
# Display "Enter number of students to order pizza for."
# Input students
# Set slices = students * 3
# Set pizzas = students / 2
# Display "\n----Pizza Order--------"
# Display "Number of Students: ", students
# Display "Pizza Slices needed: ", slices
# Display "Pizzas needed: ", pizzas
# Display "-------------------------"
#####################################################################

#Enter Number of Students.
students = int(input("Enter number of students to order pizza for."))

#Calculate Number of Pizzas and Slices.
slices = students * 3
pizzas = students / 2

#Display Results
print("\n----Pizza Order--------")
print("Number of Students: ", students)
print("Pizza Slices needed: ", slices)
print("Pizzas needed: ", pizzas)
print("-----------------------")
