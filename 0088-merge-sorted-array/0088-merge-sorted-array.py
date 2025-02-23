class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1copy = nums1[:m]
        n1, n2, n3 = 0, 0, 0

        while n1 < m and n2 < n:
            if nums1copy[n1] < nums2[n2]:
                nums1[n3] = nums1copy[n1]
                n1 += 1
                n3 += 1
            else:
                nums1[n3] = nums2[n2]
                n2 += 1
                n3 += 1
        while n1 < m:
            nums1[n3] = nums1copy[n1]
            n1 += 1
            n3 += 1
        while n2 < n:
            nums1[n3] = nums2[n2]
            n2 += 1
            n3 += 1

