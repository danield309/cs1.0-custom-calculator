print("This program will help you calculate your car's mpg.")
miles_driven = input("Enter miles driven: ") #prompts user to input miles driven
miles_driven = float(miles_driven)  #converts input into a float
gallons_used = input("Enter gallons used: ") #prompts user to input gallons used
gallons_used = float(gallons_used) #converts input into a float
mpg = miles_driven / gallons_used #the variable mpg is assigned the qoutient of miles & gallons entered
print("Estimated miles per galon: " + str(mpg) + "mpg") #returns your mpg
