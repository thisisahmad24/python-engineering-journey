def analyze_numbers(nums):
    if not nums:
        return "Empty list"

    return {
        "max": max(nums),
        "min": min(nums),
        "avg": sum(nums) / len(nums)
    }

print(analyze_numbers([10, 20, 30]))