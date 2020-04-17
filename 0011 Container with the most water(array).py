height = [1,8,6,2,5,4,8,3,7]

# The first solution：
# Consider all the posible area values. 
# Complexity is O(n^2)
c = 1
max_area = 0
len_list = len(height)

for i in height:
    n = c
    l = 1 

    while n < len_list:
        h = min(height[n],i)
        area = l*h
        print('l:', l ,'h: ',h, 'area: ', area)
        if area > max_area:
            max_area = area
        n += 1
        l += 1
    c+=1
    print(i)

print(max_area)

# The second solution:
# we have two points: one starts from left, one starts from right
# area = (N-0)*min(aN,a0)
# We want a bigger value of area, and (N-1) is decreasing. 
# So we need to make sure that min(aN, aM) is increasing 
# 想要area越大。则需要 min(aN,aM)越大，则保留 aN aM 中更大的那个数字。去掉小的那个数字
# Complexity: O(n)
L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
for w in range(width, 0, -1):
    if height[L] < height[R]:
        res, L = max(res, height[L] * w), L + 1
    else:
        res, R = max(res, height[R] * w), R - 1
print(res)
