# Author: Jesus Arias
# GitHub username: ariasje1
# Date: 07/20/2025
# Description: Finds the maximum-sum subsequence of non-consecutive elements.

def max_independent_set(nums):
    """
    Finds a subsequence of non-consecutive elements from the input list that produces
    the maximum possible sum, using dynamic programming.

    Rules:
    - No two selected elements can be adjacent in the original list.
    - If all numbers are negative, return an empty list.
    - If the maximum sum is 0, return either an empty list or [0].

    Parameters:
    nums (List[int]): A list of integers (positive, negative, or zero).

    Returns:
    List[int]: A subsequence of non-consecutive numbers with the highest possible sum.
    """

    # If the list is empty, return an empty list
    if not nums:
        return []

    n = len(nums)

    # If there's only one element, return it only if it's positive or zero
    if n == 1:
        return [nums[0]] if nums[0] > 0 else []

    # dp[i] stores the maximum sum of non-consecutive elements from index 0 to i
    dp = [0] * n

    # selected[i] tracks whether nums[i] is included in the optimal solution
    selected = [False] * n

    # Base case for the first element
    dp[0] = max(0, nums[0])
    selected[0] = nums[0] > 0

    # Base case for the second element
    if nums[1] > dp[0]:
        dp[1] = nums[1]
        selected[1] = True
    else:
        dp[1] = dp[0]
        selected[1] = False

    # Fill the dp and selected arrays using recurrence relation
    for i in range(2, n):
        # Option 1: Skip current element (carry forward dp[i-1])
        # Option 2: Include current element + dp[i-2]
        if dp[i - 1] > dp[i - 2] + nums[i]:
            dp[i] = dp[i - 1]
            selected[i] = False
        else:
            dp[i] = dp[i - 2] + nums[i]
            selected[i] = True

    # Reconstruct the solution by walking backward through the selected[] array
    result = []
    i = n - 1
    while i >= 0:
        if selected[i]:
            result.append(nums[i])
            i -= 2  # Skip adjacent element
        else:
            i -= 1

    # Reverse to preserve original order of elements
    result.reverse()
    return result
