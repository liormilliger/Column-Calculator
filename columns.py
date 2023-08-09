from csv import reader
import csv
import os
sum_var=0.0
temp_value=''
was_broken=False


############################## Logic Function #####################################
def counter_func():
    with open(file_var, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header_row = next(csv_reader, None)
        num_columns = len(header_row)
        for row in csv_reader:
            global column_var
            while column_var > num_columns:
                column_var = int(input("You have entered an invalid value, try again: "))
            temp_value=(row[column_var])
            if temp_value.isnumeric():
                global sum_var
                sum_var+=float(temp_value)
            elif len(temp_value) >= 2 and temp_value[1] == '.':
                temp_value = float(temp_value)
                sum_var += temp_value
            else:
                if continue_var == ("y"):
                    print(f"Invalid value {temp_value}, proceeding to next values...")
                if continue_var == ("n"):
                    print("Invalid value, Terminating")
                    global was_broken
                    was_broken=True
                    break
##########################Intro#################################
print("Welcome to COLUMN SUM APP!\nBefore we begin we need some info -")
############################## Filename Input Prompt #####################################
file_var = input("Please enter a csv file name from current directory: ")
while not os.path.exists(file_var):
    file_var = input("The file you have entered does not exist, please enter again: ")

############################## Stopper Input Prompt #####################################
continue_var = input("In case of an invalid value, would you like to go on with the calculation? (y/n): ")
while continue_var != ("y") and continue_var != ("n"):
    continue_var = input("Please enter a valid option (y/n):")

############################## Column Input Prompt #####################################
#### fix issue on a non numeric input !!! ###
column_var = int(input("Please choose a column number to sum: "))
while not isinstance(int(column_var), int) and column_var > 0:
    column_var = (input("You have entered an invalid value, try again: "))


counter_func()

if was_broken == False: 
    formatted_value = "{:.2f}".format(sum_var)
    print(f"The total sum of the columns is: {formatted_value}")
