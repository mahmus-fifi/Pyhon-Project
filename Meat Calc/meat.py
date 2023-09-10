# Calculates the cost of meat per killograms 
# Get the user input 
greetings = "Welcome"
# greet user
print("********************************")
print(greetings)
# ask user to input weight of meat to buy 
prompt_1 = "Please enter weight in killograms:" # note, you need to convert the input to a decimal number 
# get input 
customer_input = float(input(prompt_1)) # casting the input type to integers 
# set weight per money unit 
naira_per_kg = 4000
# calculate total cost which is 
# naira per kg multiplied by weight 
total_cost = naira_per_kg * customer_input
#print the cost 
print(f'you entered:{customer_input}kg, your total cost is: N{total_cost}')
print("*******************************")

