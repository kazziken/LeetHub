class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #thoughts:
        # must be in O(n) time so we can't sort it.
        # cyclic sort is O(n^2)
        # can't use hashmap. 
        # we definitely make a variable to keep track of the length of the longest sequence
        # conditionals to put these consecutive numbers into the array in O(n) time
        
        #neetcode explanation:
        #use 3sequence <-----1-2-3-4----100----200->
        # look at numbers no left neighbors 
        # easiest way to do this is to convert the array into a set
        # first check nums[0] = 100 is there a left neighbor of 99? nope 101 on right? nope. can't continue this sequence
        # check til you find something in the array with a sequence.
        # if theres nothing as left neighbor just use it as the start of the sequence and check if theres anything +1 in the set
        
        
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            #check if theres the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length +=1
                longest = max(length, longest)
        return longest
        
        
        
        