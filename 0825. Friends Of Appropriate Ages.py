# method 2, if ages[i] can only be interger [0,120], 
# then we can simply build a collections.Counter(ages), and then iterate all of them
# time will be O(120*120), space is O(120)


# method 1, general method if age could be floating point, 
# time n*log(n), space O(n)
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        cnt = 0
        for i, age in enumerate(ages):
            left = self.search(ages, 0.5*age+7)
            right = self.search(ages, age)
            cnt += max(right - left - 1, 0)
        return cnt
        
    
    def search(self, ages, target):
        # search the last index i such that ages[i] <= target
        left, right = 0, len(ages)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if ages[mid] <= target:
                left = mid
            else:
                right = mid
        if ages[right] <= target:
            return right
        elif ages[left] <= target:
            return left
        else:
            return -1

"""
825. Friends Of Appropriate Ages

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
"""
