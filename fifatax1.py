running = True

# Start the loop
while running:
    # get the first number from the user
    num1 = float(input("Enter the first number: "))

    # get the second number from the user
    num2 = float(input("Enter the second number: "))

    # calculate the difference between the two numbers
    diff = num2 - num1
    tax = num2 * 0.05
    net_profit = diff - tax

    # print the result
    print("The sum of the two numbers is:", diff)
    print("Tax is: ", tax)
    print("Net profit is: ", net_profit)

    # Ask the user if they want to continue
    response = input("Enter 'y' to continue or 'n' to stop: ")

    # If the user enters 'n', set running to False to end the loop
    if response.lower() == 'n':
        running = False

input('Press ENTER to exit')
