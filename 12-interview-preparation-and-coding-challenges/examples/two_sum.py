# Purpose: Solve the classic "Two Sum" interview problem.
# This demonstrates problem-solving approach: constraints, algorithm, implementation, testing.

def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    """
    Find two numbers in the list that add up to the target.
    
    Problem:
        Given a list of integers and a target sum,
        return the indexes of the two numbers that add to the target.
        Assume each input has exactly one solution.
        You cannot use the same element twice.
    
    Approach:
        Use a dictionary to store numbers we've seen and their indexes.
        For each number, check if (target - number) is already in the dict.
        If yes, we found the pair. If no, add the current number to the dict.
    
    Time Complexity: O(n) - one pass through the list
    Space Complexity: O(n) - dictionary stores up to n numbers
    
    Args:
        numbers: List of integers
        target: The target sum
    
    Returns:
        Tuple of (index1, index2) if found, None otherwise
    
    Example:
        two_sum([2, 7, 11, 15], 9) -> (0, 1)  # 2 + 7 = 9
    """
    # Dictionary to store numbers we've seen and their indexes
    # Format: {number: index}
    seen = {}
    
    # Loop through each number with its index
    for index, number in enumerate(numbers):
        # Calculate what number we need to reach the target
        needed = target - number
        
        # Check if we've already seen this needed number
        if needed in seen:
            # Found a pair! Return the indexes
            # seen[needed] is the index of the first number
            # index is the index of the current number
            return (seen[needed], index)
        
        # Store this number for future lookups
        seen[number] = index
    
    # No pair found
    return None


# Test cases
print("Two Sum Problem - Test Cases")
print("=" * 50)
print()

# Test 1: Basic example
test1_numbers = [2, 7, 11, 15]
test1_target = 9
result1 = two_sum(test1_numbers, test1_target)
print(f"Test 1: {test1_numbers}, target={test1_target}")
print(f"  Result: {result1}")
if result1:
    i, j = result1
    print(f"  Verification: {test1_numbers[i]} + {test1_numbers[j]} = {test1_numbers[i] + test1_numbers[j]}")
print()

# Test 2: Numbers at the ends
test2_numbers = [1, 2, 3, 4, 5]
test2_target = 6
result2 = two_sum(test2_numbers, test2_target)
print(f"Test 2: {test2_numbers}, target={test2_target}")
print(f"  Result: {result2}")
if result2:
    i, j = result2
    print(f"  Verification: {test2_numbers[i]} + {test2_numbers[j]} = {test2_numbers[i] + test2_numbers[j]}")
print()

# Test 3: No solution
test3_numbers = [1, 2, 3]
test3_target = 10
result3 = two_sum(test3_numbers, test3_target)
print(f"Test 3: {test3_numbers}, target={test3_target}")
print(f"  Result: {result3}")
print(f"  (No pair adds up to {test3_target})")
print()

# Test 4: Negative numbers
test4_numbers = [-1, -2, -3, 5, 10]
test4_target = 8
result4 = two_sum(test4_numbers, test4_target)
print(f"Test 4: {test4_numbers}, target={test4_target}")
print(f"  Result: {result4}")
if result4:
    i, j = result4
    print(f"  Verification: {test4_numbers[i]} + {test4_numbers[j]} = {test4_numbers[i] + test4_numbers[j]}")
print()

print("Interview tips:")
print("  1. Clarify constraints: duplicates? negative? already sorted?")
print("  2. Start with a simple approach, then optimize")
print("  3. Explain your algorithm before coding")
print("  4. Test edge cases: empty list, single element, no solution")
print("  5. Discuss complexity and alternative approaches")
