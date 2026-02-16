# Last updated: 2/16/2026, 6:34:39 PM
1class NumArray:
2
3    def __init__(self, nums: List[int]):
4        self.nums = nums
5
6    def sumRange(self, left: int, right: int) -> int:
7        return sum(self.nums[left: right + 1])
8
9
10# Your NumArray object will be instantiated and called as such:
11# obj = NumArray(nums)
12# param_1 = obj.sumRange(left,right)