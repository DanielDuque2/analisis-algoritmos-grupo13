import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        tails = []

        for num in nums:
            # buscar posición donde colocar num
            idx = bisect.bisect_left(tails, num)

            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num

        return len(tails)