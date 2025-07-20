#Author: Jesus Arias
#GitHub username: ariasje1
#Date: 07/20/2025
#Description:

def max_independent_set(nums):
    if not nums:
        return []

    n = len(nums)
    if n == 1:
        return [nums[0]] if nums[0] > 0 else []

    # DP arrays
    dp = [0] * n
    selected = [False] * n

    dp[0] = max(0, nums[0])
    selected[0] = nums[0] > 0

    if nums[1] > dp[0]:
        dp[1] = nums[1]
        selected[1] = True
    else:
        dp[1] = dp[0]
        selected[1] = False

    for i in range(2, n):
        if dp[i-1] > dp[i-2] + nums[i]:
            dp[i] = dp[i-1]
            selected[i] = False
        else:
            dp[i] = dp[i-2] + nums[i]
            selected[i] = True

    # Reconstruct result list from selected[] and dp[]
    result = []
    i = n - 1
    while i >= 0:
        if selected[i]:
            result.append(nums[i])
            i -= 2
        else:
            i -= 1

    result.reverse()
    return result


print(max_independent_set([7, 2, 5, 8, 6]))     # Output: [7, 5, 6]
print(max_independent_set([-1, -1, 0]))         # Output: [] or [0]
print(max_independent_set([-1, -1, -10, -34]))  # Output: []
print(max_independent_set([10, -3, 0]))         # Output: [10]
