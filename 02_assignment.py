'''
Assignment #2
1. Add / modify code ONLY between the marked areas (i.e. "Place code below")
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 01_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
7. Make sure your work is committed to your master branch
'''
import math
import unittest
import numpy as np
import requests as r

def exercise01():
    # Create a list called animals containing the following animals: cat, dog, crouching tiger, hidden dragon, manta ray

    # ------ Place code below here \/ \/ \/ ------
    
    animals = ["cat", "dog", "crouching tiger", "hidden dragon", "manta ray"]    

    # ------ Place code above here /\ /\ /\ ------

    return animals


def exercise02():
    # Repeat exercise 1 and loop through and print each item in the animal list by iterating through an index number and using range(). Set the variable len_animals to the length of the animal list.

    # ------ Place code below here \/ \/ \/ ------
    

    animals = exercise01()

    #length of the animal list
    len_animals = len(animals)

    for i in range(1, len_animals):
        print(i,animals[i])


    #method 2
    #for count, animal in enumerate(animals,1):
    #     print (count,animal)


    # ------ Place code above here /\ /\ /\ ------

    return animals, len_animals


def exercise03():
    # Reorganize the countdown list below in descending order and return the value of the 5th element in the countdown list
    countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
    the_fifth_element = -999

    # ------ Place code below here \/ \/ \/ ------
    
    #convert countdown to numpy array
    countdown = np.array(countdown)

    ##sorts the array in place
    countdown[::-1].sort()
    
    #return the value of the 5th element
    the_fifth_element = countdown[4]
    print(countdown)

    # ------ Place code above here /\ /\ /\ ------

    return countdown, the_fifth_element


def exercise04(more_temperatures, iot_sensor_points, a, b, c, d, e):
    # This exercise function receives a list of temperatures and a dictionary of temperature data where the key is an arbitrary sequential number and the value is the temperature and a,b,c,d and e are each a single temperature reading
    # To Do:
    # 1. Add all of the items in more_temperatures to the temperatures list
    # 2. Add all of the temperature values in iot_sensor_points to the temperatures list
    # 3. Add a,b,c,d and e to the temperature list
    # 4. Organize the temperatures in descending order
    # 5. The samples list will contain every 5th reading from the final temperatures list i.e in list [1,2,3,4,5,6,7,8,9,10] samples would be [5,10]
    # 6. Do a shallow copy of samples into copy_of_samples
    # 7. Organize samples in ascending order

    temperatures = list(np.random.randint(-25, 25, size=10))
    samples = []
    copy_of_samples = []

    # ------ Place code below here \/ \/ \/ ------
    
    temperatures += list(more_temperatures)
    
    for key,value in iot_sensor_points.items():
        temperatures.append(value)

    temperatures += [a,b,c,d,e]

    ##sort temperatures in descending order
    temperatures=sorted(temperatures,reverse=True)
     
    #list containing every 5th reading from the temperatures
    samples = temperatures[4::5]
     
    #shallow copy of samples
    copy_of_samples = samples.copy()

    ##sort samples in ascending order
    samples.sort()


    # ------ Place code above here /\ /\ /\ ------

    return samples, temperatures, more_temperatures, iot_sensor_points, a, b, c, d, e, copy_of_samples


def exercise05(n):
    # This function will find n factorial using recursion (calling itself) and return the solution. For example exercise05(5) will return 120. No Python functions are to be used.

    # ------ Place code below here \/ \/ \/ ------

    def factorial(n):
         if n < 0 or type(n) != int:
             print("Entry must be a non-negative integer")
         elif n == 1 or n == 0:
             return 1
         else:
              return n * factorial(n-1)
    
    return factorial(n)
    # ------ Place code above here /\ /\ /\ ------


def exercise06(n):
     # This function will receive an arbitrary list of numbers of arbitrary size and find the average of those numbers. The size of the list may vary. Find the method that requires the  least amount of code. Return back the length, sum of list and average of list

    # ------ Place code below here \/ \/ \/ ------

    numbers = np.array(n)
    length_n = np.size(numbers)
    sum_n = np.sum(numbers)
    average_n = np.average(numbers)

    # ------ Place code above here /\ /\ /\ ------
    return length_n, sum_n, average_n


def exercise07(n):
    # This function looks for duplicates in list n. If there is a duplicate False is returned. If there are no duplicates True is returned.

    # ------ Place code below here \/ \/ \/ ------

    list(n)

    #validate n
    if type(n)!=list:
       print("n must be a list!")

    if n == list(set(n)):
         # no dublicates are found 
         return True
    else:
         #dublicates are found 
         return False

    # ------ Place code above here /\ /\ /\ ------

# Exercise 8
# Create a function called display_menu that receives an argument called menu. The function should do the following:
# 1. Verify that menu is in fact a tuple. If it isnt, return back -1.
# 2. Determine the number of elements in menu
# 3. Loops through menu & enumerate through to the a menu to the screen. The test case will describe what the menu items are. The enumeration should be generate by code and not hardcoded.
# 4. Using input(), asks the user to select a menu item by entering a number and hitting Enter 
# 5. Validates if the number entered is a valid menu option and asks user to retry if number is not valid or is not a number / int
# 6. An exit menu option should be added at the end of the displayed list of menu options allowing the user to exit selecting a menu causing the display_menu() function to return back the number of the last menu option chosen prior to exit and also return the length of menu
# 7. If a valid menu option is chosen, call a function named similarly to the menu option that prints the menu option chosen i.e. def buy_burger() prints('Burger bought!')
# 8. The menu options should repeatedly be displayed after each selection (and appropriate delegate function is called) until user selects exist

# ------ Place code below here \/ \/ \/ ------

def display_menu(menu):
    
    my_menu=menu
    
    #verify that menu is a tuple
    if type(my_menu)!= tuple:
        return -1
    
    #convert to list
    my_menu=list(my_menu)
    
    #add exit option
    my_menu.append("Exit")
    
    #create list that stores user choices 
    user_choices=[]
    
    #lambda function
    my_func=lambda x: print(x)

    
    def select_menu():
        #display menu onm the screen
        for count, menu_items in enumerate(My_menu,1):
             print (count,menu_items)
        
        #user input     
        user_choice = input("Select a menu item 1 to " + str(len(my_menu)) + "   ")
        print("You've selected " + str(my_func(menu[user_choice]))


        #validate user entry
        if user_choice.isdigit() == False or user_choice<1 or user_choice>len(user_choices):
                print("Your selection is invalid. The entery should be a digit 1 to " + str(len(my_menu)) + "Please try again...")
                return select_menu()

        #return 0 if user choose 'Exit' as the first selection        
        elif int(user_choice)==len(my_menu) and len(user_choices)==0:
                print("Goodbuy!")
                return 0,len(my_menu)

        #return previous selection and menu length when user exits         
        elif int(user_choice)==len(my_menu) and len(user_choices)!=0:
                print("Exiting... You previous selection was " + str(user_choices[-1]))
                print(len(my_menu),int(user_choices[-1]))
                return int(user_choices[-1]),len(my_menu)

        #user makes a selection other than 'exit'        
        else:
            user_choices.append(user_choice)
            #recursive call
            return select_menu()
                  
    return select_menu()




# ------ Place code above here /\ /\ /\ ------

def exercise09():
    # Compile a list of 10 random URLs of dog pics

    dogs = []
    url = 'https://random.dog/woof.json'
    dog_media = r.get(url=url)
    print(str(dog_media.content))
    
    # ------ Place code below here \/ \/ \/ ------
    
    dogs=url,url,url,url,url,url,url,url,url,url

    # ------ Place code above here /\ /\ /\ ------

    return dogs

def exercise10(sentence):

    # Exercise10 receives an arbitrary string. Return the sentence backwards with the cases inverted and spaces an underscore _, i.e. HelLo returns OlLEh
    reversed = ''

    # ------ Place code below here \/ \/ \/ ------
    
    #validate sentance
    if  type(sentence)!=str:
        print("The entered sentace is not a string.")

    else:
        #return the sentence backwards
        reversed = sentence[::-1]

        #invert cases
        reversed=reversed.swapcase()
    
        #replace spaces with underscores
        reversed=reversed.replace(' ','_')

    # ------ Place code above here /\ /\ /\ ------
    return reversed


class TestAssignment2(unittest.TestCase):
    def test_exercise01(self):
        print('Testing exercise 1')
        a = exercise01()
        self.assertEqual(len(a), 5)
        self.assertTrue('cat' in a)
        self.assertTrue('dog' in a)
        self.assertTrue('manta ray' in a)
    
    def test_exercise02(self):
        print('Testing exercise 2')
        a, l = exercise02()
        self.assertEqual(len(a), 5)
        self.assertEqual(l, 5)
        self.assertTrue('cat' in a)
        self.assertTrue('dog' in a)
        self.assertTrue('manta ray' in a)

    def test_exercise03(self):
        print('Testing exercise 3')
        c, tfe = exercise03()
        self.assertEqual(c[0], 10)
        self.assertEqual(c[11], -5)
        self.assertEqual(len(c), 12)
        self.assertEqual(tfe, 6)

    def test_exercise04(self):
        print('Testing exercise 4')
        more_temperatures = np.random.randint(300, 400, size=25)
        iot_sensor_points = {1: 801, 2: 644, 3: 991, 4: 721,
                             5: 752, 6: 871, 7: 991, 8: 1023, 9: 804, 10: 882}
        samples, temperatures, more_temperatures, iot_sensor_points, a, b, c, d, e, copy_of_samples = exercise04(more_temperatures, iot_sensor_points,
                                                                                                                 8000, 8500, 9000, 9500, 9999)

        self.assertEqual(len(temperatures), 50)
        self.assertEqual(len(samples), 10)
        self.assertEqual(temperatures[0], 9999)
        self.assertEqual(temperatures[11], 801)
        self.assertEqual(samples[9], 8000)
        self.assertEqual(copy_of_samples[0], 8000)
        self.assertEqual(a, 8000)
        self.assertEqual(b, 8500)
        self.assertEqual(c, 9000)
        self.assertEqual(d, 9500)
        self.assertEqual(e, 9999)

    def test_exercise05(self):
        print('Testing exercise 5')
        self.assertEqual(exercise05(5), 120)
        self.assertEqual(exercise05(10), 3628800)

    def test_exercise06(self):
        print('Testing exercise 6')
        length_n, sum_n, average_n = exercise06([1, 2, 3, 4, 5])
        self.assertEqual(average_n, 3)
        self.assertEqual(length_n, 5)
        length_n, sum_n, average_n = exercise06([1, 2, 120])
        self.assertEqual(average_n, 41)
        self.assertEqual(length_n, 3)

    def test_exercise07(self):
        print('Testing exercise 7')
        self.assertTrue(exercise07([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False)
        self.assertTrue(exercise07([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True)
        self.assertTrue(exercise07([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == False)
        self.assertTrue(exercise07([1, 2.00002, 2.00001, 4, 5, 6, 7, 8, 9, 10]) == True)

    def test_exercise08(self):
        print('Testing exercise 8')
        menu = ['Buy Bitcoin','Buy Ethereum','Sell Bitcoin','Sell Ethereum']
        r, l = display_menu(menu)
        self.assertEqual(r,-1)
        self.assertEqual(l,4)
        menu = ('Buy Bitcoin','Buy Ethereum','Sell Bitcoin','Sell Ethereum')
        r, l = display_menu(menu)
        self.assertTrue(r > 0)
        self.assertEqual(l,4)
    
    def test_exercise09(self):
        print('Testing exercise 9')
        dogs = exercise09()
        for d in dogs:
            print(d)
            self.assertTrue('https://random.dog/' in d)
            

    def test_exercise10(self):
        print('Testing exercise 10')
        self.assertEqual(exercise10('HellO'),'oLLEh')
        self.assertEqual(exercise10('ThIs Is MaD'),'dAm_Si_SiHt')




if __name__ == '__main__':
    unittest.main()
