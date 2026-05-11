#===Day 1 Drill===
# Example_list = [1,2,3,4,5,5]
# def count(numbers, target):
#     amount = 0
#     for num in numbers:
#         if num == target:
#             amount += 1
#     return amount
# print(count(Example_list, 5))

#===Day 5 Drill===
# example_list = [5,3,8,1,4,3,2,5,-3]
# def find_smallest_number(numbers):
#     start = numbers[0]
#     for num in numbers:
#         if num < start:
#             start = num
#     return start
# print(find_smallest_number(example_list))

#===Day 6 Drill===
# numbers = [1,2,4,7,8]
# def count_even_numbers(numbers):
#     amount = 0
#     for num in numbers:
#         if num%2 == 0:
#             amount += 1
#     return amount
# print(count_even_numbers(numbers))

#===Day 7 Drill===
# numbers = [3, 8, 2, 10, 5]
# def find_biggest_number(numbers):
#     target = numbers[0]
#     for num in numbers:
#         if num > target:
#             target = num
#     return target
# print(find_biggest_number(numbers))

#===Day 8 Drill===
# numbers = [2,4,6]
# def find_average(numbers):
#     total = 0
#     amount = len(numbers)
#     for num in numbers:
#         total += num
#     return total/amount
# print(find_average(numbers))

#===Day 9 Drill===
# numbers = [1,5,8,2,10]
# def greater_than_target(numbers):
#     try:
#         target = int(input())
#     except ValueError:
#         return ('Type in a number')
#     amount = 0
#     for num in numbers:
#         if num > target:
#             amount += 1
#     return amount
# print(greater_than_target(numbers))

#===Day 10 drill===
# numbers = [3,8,2,10,5]
# def largest_and_smallest(numbers):
#     largest = numbers[0]
#     smallest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num
#         elif num < smallest:
#             smallest = num
#     return f"Largest: {largest}\nSmallest:{smallest}"
# print(largest_and_smallest(numbers))

#===Day 11 Drills===
# nums = [1,2,2,3,3,3]
# def frequent_element(nums):
#     highest_count = 0
#     freq_element = nums[0]
#     for num in nums:
#         amount = 0
#         target = num
#         for item in nums:
#             if target == item:
#                 amount +=1
#         if amount > highest_count:
#             highest_count = amount
#             freq_element = target
#     return freq_element
# print(frequent_element(nums))
        
#===Day 12 Drills===
# nums = [1,2,2,3,3,3]
# def unique_elements(nums):
#     seen_numbers = []
#     for num in nums:
#         amount = 0
#         target = num
#         for item in nums:
#             if item == target:
#                 amount += 1
#         if amount >= 1 and not num in seen_numbers:
#             seen_numbers.append(num)
#     return len(seen_numbers)
# print(unique_elements(nums))

#===Day 13 Drills===
# nums = [1,2,2,3,3,3,4]
# def appear_only_once(nums):
#     only_once_nums = []
#     for num in nums:
#         amount = 0
#         current_target = num
#         for item in nums:
#             if item == current_target:
#                 amount +=1
#         if amount == 1:
#             only_once_nums.append(num)
#     return len(only_once_nums)
# print(appear_only_once(nums))

# #=== Day 14 Drills ===
# nums = [1,2,3,2,5]
# def first_appearing_num(nums):
#     repeated_values = []
#     for num in nums:
#         target = num
#         amount = 0
#         for item in nums:
#             if item == target:
#                 amount +=1
#         if amount > 1 and num not in repeated_values:
#             repeated_values.append(num)
#     return repeated_values[0]
# print(first_appearing_num(nums))

#===Day 15 Drill===
nums =[1,2,2,2,3,3,3]
def most_frequent_num(nums):
    largest_amount = 0
    most_frequent = 0
    for num in nums:
        amount = 0
        target = num
        for item in nums:
            if item == target:
                amount += 1
        if amount > largest_amount:
            largest_amount = amount
            most_frequent = num
    return most_frequent
print(most_frequent_num(nums))