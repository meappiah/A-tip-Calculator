
print("Welcome to the tip Calculator! ") #Welcome message
Bill= float(input("What was the total bill?$ "))#Input prompt for total bill 
Tip= int(input("What tip will you like to give? 10, 12, or 15? "))#input prompt for tip
people= int(input("How many people will like to split the bill ? ")) #input prompt for the number of people sharing the tip
tip_as_a_percentage = Tip/100 #calculating percentage for the tip
total_tip_amount = Bill * tip_as_a_percentage #Calculating the total amount for the tip
total_bill =Bill + total_tip_amount #Calculating the total bill plus the tip
Bill_per_person =total_bill/people #Calculating Bill per person
Final_amount =round(Bill_per_person, 2) #Rounding the final bill per person to 2 decimal places
print(f"Each person should pay: ${Final_amount}") #printing the final bill for each person

