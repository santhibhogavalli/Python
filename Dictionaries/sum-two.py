# Problem: Sum two numbers 
# pattern: dictionary
# Scenario: Given a list of integers and a target, return the indices of two numbers that add up to the target. 
# Assume exactly one valid answer exists, and do not use the same element twice.

# solution: Use a dictionary to store the numbers and their indices. 
# For each number, check if the complement (target - number) exists in the dictionary.
#  If it does, return the indices of the current number and its complement.

#example : int = [2, 7, 11, 15], target = 26

def main():
    int=[2, 7, 11, 15]
    target=26
    dict = {}
    # enumerate() function is used to get both the index and the value of each element in the list.
    for i, num in enumerate(int):
        # calculate the complement of the current number with respect to the target
        complement = target - num
        if complement in dict:
            print([dict[complement], i])
            return
        dict[num] = i

if __name__ == "__main__":
    main()
