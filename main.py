'''
* csv allows us to read in and work with csv files
* time allows us to work with time-related functions
* statistics allows us to use statistical functions to work with data
'''
import csv, time, statistics

poke_list = []           #will become the 2d list that stores all the values from the csv file
totals_list = []         #stores the totals from each row
lsearch_times = []       #stores the time taken to run the linear search per iteraion
bsearch_times = []       ##stores the time taken to run the binary search per iteraion

'''
This method reads the csv file into a 2D list. 
'''
def read_in():
    with open('Pokemon_numerical (1).csv', 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            poke_list.append(row)       #appends each row of the csv file into the list


'''
This method performs the linear search.
'''
def linear_search(poke_list):
    target = "Poison"
    poison_count = 0                            #stores the frequency of the target(Poison)
    for i, sublist in enumerate(poke_list):     #iterates over each row in the 2d list
        if target in sublist:
            poison_count = poison_count + 1     #increments by 1 if "Poison" is found in the row

    print("Frequency of Poison found: ", poison_count)

'''
This function performs the binary search.
'''
def binary_search(totals_list):
    left = 0                        #represents the leftmost index of the list
    right = len(totals_list) - 1    #represents the rightmost index of the list

    while left < right:
        mid = (left + right + 1) // 2               #stores the right midpoint
        if totals_list[mid] > totals_list[left]:    #max value is found in the right half of the current range
            left = mid
        else:                                       #max value is found in the left half of the current range
            right = mid - 1

    print("The maximum value in the list is: ", totals_list[left])
    return totals_list[left]

'''
This function gets a 2d list of all the names associated with the maximum value, converts it to a dictionary
and prints it. 
'''
def display_binary_search(max_value, poke_list):
    names_and_totals = []

    for row in poke_list:
        if row[4] == max_value:                             #checks if the 4th column contains the max value
            names_and_totals.append((row[1], row[4]))       #appends the name and the max value to a list

    print("Key/Value Maximums: ", dict(names_and_totals))   #converts the list to a dictionary and displays the key/value pairs


'''
Main method
'''
if __name__ == '__main__':

    read_in()                                       #calls method to read in the csv file

    totals_list = [row[4] for row in poke_list]     #populates the list of totals
    totals_list.sort()                              #sort the list in ascending order

    count = 100                                       #sets loop counter

    for i in range (count):

        print("Starting linear problem solution: ", i+1)
        print()

        start_time = time.perf_counter_ns()             #starts the timer
        linear_search(poke_list)
        end_time = time.perf_counter_ns()               #ends the timer
        lsearch_times.append(end_time - start_time)     #appends the difference of the start and end time to a list
        print("Time taken ", lsearch_times[i], "nanoseconds.")
        print()

        print("Starting binary problem solution: ", i+1)
        print()

        start_time = time.perf_counter_ns()
        max_value = binary_search(totals_list)
        end_time = time.perf_counter_ns()
        bsearch_times.append(end_time - start_time)
        print("Time taken ", bsearch_times[i], "nanoseconds.")

        display_binary_search(max_value, poke_list)

        print("\nSleeping ....\n")
        time.sleep(2)                                   #pauses the program for 2 seconds
        print("*******************************************************************************************************************")

    '''
    The last lines of code uses the mean method of the statistics module to calculate the average of the lists. The 
    average is rounded to 2 decimal places and displayed. 
    '''
    print("The average time taken for the linear search is", round(statistics.mean(lsearch_times), 2), "nanoseconds")
    print("The average time taken for the binary search is", round(statistics.mean(bsearch_times), 2), "nanoseconds")

