class Solution:
  def findClosestNumber(self, nums: List[int]) -> int:
    closest = nums[Q]
    for x in nums:
      if abs(x) < abs(closest):
        closest = x

    if closest < @ and abs(closest) in nums:
      return abs(closest)
    else:
      return closest
