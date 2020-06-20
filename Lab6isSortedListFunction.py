'''
Author....: Matt Verini
Assignment: Lab06 Flesch Text Analysis
Date......: 03/30/2020
Program...: Sorted List
'''

'''
A list is sorted in ascending order if it is empty or
each item except the one is less than or equal to its
successor. Define a predicate isSorted that expects a
list as an argument and returns True if the list is
sorted, or returns False otherwise.

For a list of length 2 or greater, loop through the
list and compare pairs of items, from left to right,
and return False if the first item in a pair is greater.
'''


def isSorted(sample_list):
    if len(sample_list) >= 0 and len(sample_list) < 2:
        return True
    else:
        for index in range(len(sample_list) - 1):
            if sample_list[index] > sample_list[index + 1]:
                return False
            else:
                return True

def main():
    '''
    Different list examples to test function defined above
    '''
    sample_list = []
    print(isSorted(sample_list))
    sample_list = [6]
    print(isSorted(sample_list))
    sample_list = list(range(10))
    print(isSorted(sample_list))
    sample_list = list(range(8))
    sample_list.insert(0, 3)
    print(sample_list)
    print(isSorted(sample_list))
    sample_list = [7, 3, 5]
    print(isSorted(sample_list))


main()
