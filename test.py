def trap(height):
    n = len(height)

    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n
 
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
   
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water

assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert trap([4, 2, 0, 3, 2, 5]) == 9
assert trap([3, 0, 2, 0, 4]) == 7
assert trap([1, 0, 1]) == 1
assert trap([]) == 0
assert trap([5]) == 0
assert trap([0, 0, 0]) == 0
assert trap([3, 3, 3]) == 0

print("All tests passed.")
