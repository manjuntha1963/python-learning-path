def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    seen = {}
    for index, number in enumerate(numbers):
        if target - number in seen:
            return seen[target - number], index
        seen[number] = index
    return None


print(two_sum([2, 7, 11, 15], 9))
