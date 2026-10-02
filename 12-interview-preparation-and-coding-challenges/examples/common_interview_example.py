# Module 12 example: interview coding task
# This demonstrates a classic two-sum approach used in interviews.
#
# Common mistake:
# A beginner often writes a nested loop solution.
# That works, but it is slower and has O(n^2) time complexity.
#
# Error example:
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             return [i, j]
#
# This is correct, but not efficient for large inputs.
#
# Fix:
# Use a dictionary to store visited numbers and their indexes.
# This reduces the time to O(n).


def two_sum(nums, target):
    # seen = {number: index}
    # This dictionary stores values we have already seen.
    seen = {}

    # Check each value in the list once
    for i, value in enumerate(nums):
        # Compute the missing value needed to reach the target
        missing = target - value

        # If we have already seen the missing value, we found the pair
        if missing in seen:
            return [seen[missing], i]

        # Otherwise, store the current value for future checks
        seen[value] = i

    # No valid pair found
    return None


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([1, 2, 3, 4, 5], 6))
