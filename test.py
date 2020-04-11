nums = [2,3,1,1,4]

# generate a dic = {0:2,1:3,2:1,3:1,4:4}
# index + number, eg: 1+3 =4 , means that from nums[1], the furthest postion it can reach is nums[4] = 4
# if the posible furtest postion yet not reach the end of the array, returns False
# 假如在 nums[1] 这个位置，那么最远可以去的地方是 nums[4], 在nums[2] 最远可以去的是 nums[3], 当 max_steps = max(max_steps, index+number)
# 所以此时最远距离还是 nums[4]


def jump_game(nums):
    max_steps = 0
    for index, number in enumerate(nums):
        if index > max_steps:
            return False
        max_steps = max(max_steps, index+number)
    return True

jump_game(nums)
