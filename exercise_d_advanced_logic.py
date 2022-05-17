# For the following list of numbers:

from unittest import skip


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_list = []

for number in numbers:
    if number %2 == 0:
        even_list.append(number)

print(even_list)


# 2. Print the difference between the largest and smallest value:
difference = max(numbers) - min(numbers)
print(difference) 


# 3. Print True if the list contains a 2 next to a 2 somewhere.

last_number = 0

for number in numbers:
    if number == 2 and last_number == 2:
        print(True)
    last_number = number



# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# numbers = [11, 6, 4, 99, 7, 11] 

total = 0
ignoring = False

for number in numbers:

    if ignoring == True and number != 7:
        continue

    elif number == 6:
        ignoring = True
        continue

    elif number == 7:
        ignoring = False
        continue

    else:
        total += number

print(f"Ignoring numbers bound by 6 then 7 inclusive gives a total of {total} (I think)")


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

# get index of thirteen add to a skip list.  
# Add index(13)+1 (next number) too
# loop over list retreiving index and value (enumerate)
# Add number to total if current index is not in skip list.


total = 0
skip_list = []
index_of_13 = numbers.index(13)
skip_list.append(index_of_13)
skip_list.append(index_of_13 + 1)
# print(skip_list)

for index, number in enumerate(numbers):
    if index not in skip_list:
        total += number

print(f"Ignoring '13' and it's evil neighbour (on the right hand side) gives us a total of ... {total}")







