matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(matrix[::-1])
# >>> [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

print(*matrix[::-1])
# >>> [7, 8, 9] [4, 5, 6] [1, 2, 3]

# And then use zip, which will match the elements
print(zip(*matrix[::-1]))
#<zip object at 0x105466cc8>

matrix[:] = zip(*matrix[::-1])
print(matrix)
# >>> [(7, 4, 1), (8, 5, 2), (9, 6, 3)]


