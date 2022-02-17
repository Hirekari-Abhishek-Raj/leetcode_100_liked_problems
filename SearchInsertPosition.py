class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(arr,start,end):
            if start<=end:
                mid=(start+end)//2
                if arr[mid]==target:
                    return mid
                if arr[mid]>target:
                    return binarySearch(arr,start,mid-1)
                return binarySearch(arr,mid+1,end)
            else:
                return start
        return binarySearch(nums,0,len(nums)-1)
