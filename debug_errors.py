def calculate_average(numbers):
    try:
        total = 0
        for num in numbers:
            total += num
        return total / len(numbers)
    except ZeroDivisionError:
        print("Cannot calculate average: the list is empty.")
        return 0 
def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print("Index is out of range.")
        return None
    except TypeError:
        print("Input is not a list.")
        return None
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []

print("Average of data1:", calculate_average(data1))
print("Average of data2:", calculate_average(data2))
print("Average of data3:", calculate_average(data3))  

print("\nTesting get_list_element:")
print("Valid:", get_list_element([1, 2, 3], 1))     
print("Out of range:", get_list_element([1, 2, 3], 5))  
print("Wrong type:", get_list_element("hello", 1))