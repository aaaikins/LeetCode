class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        n = len(nums1)

        res = [-1] * n

        for i, n in enumerate(nums1):
            hashmap[n] = i

        for i in range(len(nums2)-1):
            if nums2[i] in hashmap:
                j = i + 1
                while nums2[j] < nums2[i] and j < len(nums2) - 1:
                    j += 1
                res[hashmap[nums2[i]]] = nums2[j] if nums2[j] > nums2[i] else -1
            else:
                continue

        
        
        return res

