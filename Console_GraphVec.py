from GraphVec import *
#A function that starts a programs that runs on the console.
def start(clear = False, count_clr = 3, date = False, title = 'Vector Visualization'):
    
    #Initiating variables for later use.
    vectors_list = []
    vectors_dict = {}
    count = count_clr

    #An options variable that will be printed everytime the while loop loops.
    options = '''\nOptions:
    1: Create vectors
    2: View vectors
    3: Operations
    4: Draw vectors
    5: Clear
    6: Exit'''

    #A welcome message to introduce the project to the user.
    print('Welcome to GraphVec')
    print('This project can help you do many things with vectors.')

    #A while loop so that the project runs until stopped.
    while True:
        #Displaying the options and asking input from the user.
        print(options)
        choice = input('\nChoose an option (1-6): ')

        if clear:
            count -= 1
            if count == 0:
                display.clear_output()
                count = count_clr

        if choice == '1':
            print('\nCreate vectors: \n\t1: From points \n\t2: From magnitude and direction')
            choice2 = input('\nChoose an option (1-2): ')
            choice3 = input('\nHow many vectors would you like to create')

            try:
                choice3 = int(choice3)
            except:
                print('Please enter a valid number')
                continue

            if choice2 == '1':

                for i in range(choice3):
                    try:
                        choice4 = input('\nDo you like to name your vector? (y/n)').lower()
                    
                        if choice4 == 'y':
                            
                            name = input('Enter the name for your vector: ')
                            x1, y1 = map(float, input('Enter starting point |x1, y1|: ').split(','))
                            x2, y2 = map(float, input('Enter ending point |x2, y2|: ').split(','))
                            v = Vector((x1, y1), (x2, y2))
                            vectors_dict[name] = v
                            print(f'\nVector created as:_ Vector {name}')
                    
                        elif choice4 == 'n':
                            
                            x1, y1 = map(float, input('Enter starting point |x1, y1|: ').split(','))
                            x2, y2 = map(float, input('Enter ending point |x2, y2|: ').split(','))
                            v = Vector((x1, y1), (x2, y2))
                            vectors_list.append(v)
                            print(f'\nVector created as: Vector {vectors_list.index(v)}')
                        
                        else:
                            print('Please enter a valid answer.')
                    except:
                        break
                        
            elif choice2 == '2':

                for i in range(choice3):
                    try:
                        choice5 = input('\nDo you like to name your vector? (y/n)').lower()
                    
                        if choice5 == 'y':
                            
                            name = input('Enter the name for your vector: ')
                            magnitude = float(input('Enter the magnitude: '))
                            direction = float(input('Enter the direction (in degrees): '))
                            m = Mvector(mag = magnitude, dir = direction)
                            v = m.to_vector()
                            vectors_dict[name] = v
                            print(f'\nVector created as:_ Vector {name}')
                    
                        elif choice5 == 'n':
                            
                            magnitude = float(input('Enter the magnitude: '))
                            direction = float(input('Enter the direction (in degrees): '))
                            m = Mvector(mag = magnitude, dir = direction)
                            v = m.to_vector()
                            vectors_list.append(v)
                            print(f'\nVector created as: Vector {vectors_list.index(v)}')
                        
                        else:
                            print('Please enter a valid answer.')
                    except:
                        break

        elif choice == '2':
            print('\n____________Vectors:_____________')
            if not vectors_list and not vectors_dict:
                print('You have no vectors.')

            else:
                for i,vector in enumerate(vectors_list):
                    print(f'\nVector {i}: {vector}')
    
                for vector in vectors_dict:
                    print(f'\nVector {vector}: {vectors_dict[vector]}')

        elif choice == '3':
            print('\nOperations: \n\t1: Add \n\t2: Subtract \n\t3: Scalar Multiplication \n\t4: Scalar Division')
            choice5 = input('\nChoose an option (1-4): ')
            result_vector = Vector()
            
            if not vectors_list and not vectors_dict:
                print("You don't have any vectors.")
                continue
        
            if vectors_list: #Performing the operations for vectors with just indexes if there are some.
                O_list = input('Enter the indexes of the vectors separated by commas (only int): ').split(',')#Taking input for integer indexes.
                
                try: #For handling errors.
                    for i in O_list: #For loop for performing the operations on multiple vectors.
                        index = int(i.strip()) #Removing spaces from the string and turning it into an integer.
                        
                        if choice5 in ['1', '2']:
                            #For Addition and Subtraction, we initialize the resulting vector.
                            if index == 0: #Initiating the result vector.
                                result_vector = vectors_list[index]
                            elif choice5 == '1':
                                result_vector += vectors_list[index] #Addition
                            elif choice5 == '2':
                                result_vector -= vectors_list[index]  #subtraction
                                
                        elif choice5 in ['3', '4']:
                            #For scalar multiplication and division, we initiatte the scalar value and find the resulting vector.
                            scalar = float(input("Enter a scalar value: ")) #Taking the scalar value.
                            
                            if choice5 == '3':
                                result_vector += vectors_list[index] * scalar  # Scalar Multiplication
                            elif choice5 == '4':
                                result_vector += vectors_list[index] / scalar  # Scalar Division
                                
                except (ValueError, IndexError): #Error message incase an error occured.
                    print('\nInvalid input. Please ensure you are using valid indices.')
                    continue
        
            if vectors_dict: #Performing the operations for vectors with names if there are some..
                O_dict = input('Enter the names of the vectors separated by commas: ').split(',') #Taking input of many names.
                
                for name in O_dict: #For handling errors.
                    name = name.strip() #Removing whitespaces from the name.
                    
                    if choice5 in ['1', '2']:
                        if name in vectors_dict:
                            if choice5 == '1':
                                result_vector += vectors_dict[name]  # Addition
                            elif choice5 == '2':
                                result_vector -= vectors_dict[name]  # Subtraction
                        else:
                            print(f"Vector '{name}' not found in named vectors.")
                            
                    elif choice5 in ['3', '4']:
                        #For scalar multiplication and division, we initiatte the scalar value.
                        scalar = float(input("Enter a scalar value: "))
                        
                        if name in vectors_dict: #Checking if the vector needed is located in our list.
                            if choice5 == '3':
                                result_vector += vectors_dict[name] * scalar # Scalar Multiplication
                                print('Vector added')
                            elif choice5 == '4':
                                result_vector += vectors_dict[name] / scalar  # Scalar Division
                                
                        else:
                            print(f"Vector '{name}' not found in named vectors.")

            vectors_list.append(result_vector) #Adding the result_vector to the vectors_list.
            print(f"\nResulting Vector after operation added as: Vector {vectors_list.index(result_vector)}") #Print message showing that the operation is complete.

        elif choice == '4':
            GraphVector(V_list = vectors_list, V_dict = vectors_dict, title = title, date = date)#The function that displays the vectors.

        elif choice == '5':
            display.clear_output()#IPython function that clears the console, may nt work with other interpretors.
                
        elif choice == '6':
            print('\nThank you for using GraphVec.')
            break
            
        else:
            print('Invalid option. Please try again.')

if __name__ == '__main__':
  start(date = True)
