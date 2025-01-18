#calculator with different operations
print('__General_Calculator__')

#importing a library for later use.
import os

#declaring the variable operation
operation = ''

#defining a function for later use
def Arithmetic_operation(operation):
    
    # if the operation chosen is Addition
    if operation == '+':
        
        #asking the two numbers to do the operation
        num1 = float(input('\t\t First number:_ '))
        num2 = float(input('\t\t Second number:_ '))
        
        #doing the operation and showing it
        print('\n\t\t\t Answer = ',num1+num2,'\n')
        
    # if the operation chosen is Subtraction
    elif operation == '-':
        
        #asking the two numbers to do the equation
        num1 = float(input('\t\t First number:_ '))
        num2 = float(input('\t\t Second number:_ '))
        
        #doing the operation and showing it
        print('\n\t\t\t Answer = ',num1 - num2,'\n')
        
    # if the operation chosen is Multiplication
    elif operation == '*':
        
        #asking the two numbers to do the equation
        num1 = float(input('\t\t First number:_ '))
        num2 = float(input('\t\t Second number:_ '))
        
        #doing the operation and showing it
        print('\n\t\t\t Answer = ',num1 * num2,'\n')

    # if the operation chosen is Exponentiation
    elif operation == '**':
        
        #asking the two numbers to do the equation
        num1 = float(input('\t\t First number:_ '))
        num2 = float(input('\t\t Second number:_ '))
        
        #doing the operation and showing it
        print('\n\t\t\t Answer = ',num1 ** num2,'\n')
        
    # if the operation chosen is Division
    elif operation == '/':
        
        #asking the two numbers to do the equation
        num1 = float(input('\t\t First number:_ '))
        num2 = int(input('\t\t Second number:_ '))
        
        #doing the operation and showing it
        print('\n\t\t\t Answer = ',num1 / num2,'\n')
    
    # if the operation is root
    elif operation == 'root':
        
        #asking the two numbers to do the equation
        num1 = float(input('\t\t Root of:_ '))
        num2 = 1/(float(input('\t\t How much Root:_ ')))
        
        #doing the operation and showing it
        print('\n\t\t\t Answer = ',num1 ** num2,'\n')
    
    #if the operation is BMI
    elif 'bmi' in operation:

        #asking the heigh and weight of the person
        height = float(input('\t\t Height (in meter):_ '))
        weight = float(input('\t\t Weight (in kilogram):_ '))

        BMI = weight/(height**2)
        
        #printing the BMI
        print('\n\t\t\t BMI = ',BMI,'\n')

#defining other function for other operations
def Other_operation(operation):
    
    #taking multiple inputs from the user and sprliting them
    input_string = input('\n\t\t Enter the numbers separated by comma[,]:_ ')
    user_list = input_string.split(',')

    # converting each item to float
    for i in range(len(user_list)):
        user_list[i] = float(user_list[i])
            
    #creating a sorted list
    sorted_list = sorted(user_list)
    
    #if the operation is Max
    if 'max' in operation:
        
        # Calculating the max value from list elements
        print("\n\t\t\t Max =", max(user_list),'\n')

    #if the operation is Min
    if 'min' in operation:
        
        # Calculating the min value from list elements
        print("\n\t\t\t Min =", min(user_list),'\n')
    
    #if the operation is Sum
    if 'sum' in operation:
        
        # Calculating the sum of the elements
        print("\n\t\t\t Sum =", sum(user_list),'\n')

    #if the operation is sorted
    if 'sort' in operation:
        
        #printing the sorted list
        print('\n\t\t\t',sorted_list,'\n')
    
    #if the operation is Median
    if 'central' in operation:

        #displaying the length of data
        print("\n\t\t\t Length = " + str(len(user_list)))

        # Calculating the Mean of the elements
        Mean = sum(user_list)/len(user_list)
        #showing the result
        print("\t\t\t Mean =", Mean )
        
        # Calculating the median of the elements
        
        #if the length of the list is even
        if len(user_list)%2 == 0: 
            Median = (sorted_list[len(sorted_list)//2] + sorted_list[(len(sorted_list)//2)-1])/ 2
        #if the length of the list is odd
        else:
            Median = int(sorted_list[(len(sorted_list)//2)])
        #showing the result
        print("\t\t\t Median =", Median)

        #calculating mode
        #first we create variables one that will store the frequency and the other the mode
        freq = []
        Mode = []

        #we create empty values based on the length of the data inputted
        for number1 in range(len(user_list)):
            freq.append(0)
            
            #we will count the number of occerence and store it to the freq variable
            for number2 in range(len(user_list)):
                if user_list[number1] == user_list[number2]:
                    freq[number1] += 1
                    
        #by using the zip function we assign the values to their number of occerence
        pairs = list(zip(user_list,freq))
                
        #we save the max frequency value using the max function and a custom function
        Max = max(pairs, key=lambda x : x[1])

        #if the highest frequency is not equal to 1
        if Max[1] != 1:
            #we use for loop to check if there are any other equal modes
            for i in range(len(pairs)):
                if pairs[i][1] == Max[1]:
                    Mode.append(pairs[i][0])
            Mode = list(set(Mode))
        else:
            Mode = None

        #we finally print the modes
        print(f"\t\t\t Mode = {Mode} ")
        print()

    #if the operation is range
    if 'range' in operation:
        
        #calculating range
        print("\n\t\t\t Range =", max(user_list)-min(user_list))
    
    #if the operation is dispersion
    if 'dispersion' in operation:
        
        #calculating range
        print("\n\t\t\t Range =", max(user_list)-min(user_list))

        #calculating variance
        variance = []
        for element in user_list:
            var = (element - sum(user_list)/int(len(user_list)))**2
            variance.append(var)
        variance = sum(variance)/int(len(variance))
        
        #printing the variance
        print("\t\t\t Variance =",round(variance,2))
        
        #standard deviation calculation
        standard_deviation = variance**(1/2)
        
        #printing standard deviation
        print(f"\t\t\t Standard Deviation = {round(standard_deviation,2)}\n")

#while loop so that the program runs until stopped
while True:
    
    # showing the operations
    print('\n\nOprations: [ + , - , * , / , ** , Root , BMI , Other ], [Stop] to stop or [Clear] to clear','\n')
    
    #asking input from the user for the operation
    operation = input('\t Choose an operation:_').lower()
    print()

    #if Clear is choosen
    if 'clear' in operation:

        os.system('clear')

    #if Stop is choosen
    if 'stop' in operation:
        
        #stopping the while loop
        break
        
    #calling the function from before for arithmethic operations
    Arithmetic_operation(operation)

    #if the user chooses other
    if 'other' in operation:
        
        #asking other input
        operation = input('\t Other operations: [Max , Min , Sum , Range , Sort] \n\t\t\t[Central] for central tendency and [Dispersion] for measure of dispersion:_').lower()
        
        #calling other operations funcion to do the rest
        Other_operation(operation)