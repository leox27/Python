
from typing import List
"""
Question 1:
Rotate the elements of an array by k positions.
	* You are given an array of integers.
	* Ask the user to input:
	* The direction of rotation (`left` or `right`)
	* The number of positions `k`
	* If the direction is left, shift the elements towards the left by `k` positions.
	* If the direction is right, shift the elements towards the right by `k` positions.
	* The rotation should be circular, meaning elements shifted out from one side should reappear on the other side.

Input:
numbers = [1, 2, 3, 4, 5]
direction = right
k = 2

Output:
[4, 5, 1, 2, 3]

Input:
numbers = [1, 2, 3, 4, 5]
direction = left
k = 2

Output:
[3, 4, 5, 1, 2]

Constraints:
* Do not use `while` loops
* Use only `for` loops for iteration
* Do not use inbuilt rotation functions
"""

def rotate(numbers: List[int], direction: str, k: int) -> List[int]:
    if direction == 'right':
        for i in range(k):
            pop = numbers.pop()
            numbers.insert(0, pop)
    elif direction == 'left':
        for i in range(k):
            pop = numbers.pop(0)
            numbers.append(pop)
    return numbers
print(rotate([1, 2, 3, 4, 5], 'right', 2))
print(rotate([1, 2, 3, 4, 5], 'left', 2))
'''
>>>
[4, 5, 1, 2, 3]
[3, 4, 5, 1, 2]
'''

