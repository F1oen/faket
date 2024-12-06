number = [1,2,3,4,5,6,7,8,9,0]

def  print_list(lst):
    print("List:", lst)
def sum_list(lst):
    print("Sum:",sum(lst))
def max_min_list(lst):
    print("Max: ",max(lst), "Min: ", min(lst))
def revers_list(lst):
    print("Reversed: ",lst[::-1])

print_list(number)
sum_list(number)
max_min_list(number)
revers_list(number)