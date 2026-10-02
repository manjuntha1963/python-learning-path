# Module 12 example: interview coding task
# This demonstrates a classic two-sum approach used in interviews


def two_sum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        missing = target - value
        if missing in seen:
            return [seen[missing], i]
        seen[value] = i
    return None


print(two_sum([2, 7, 11, 15], 9))
