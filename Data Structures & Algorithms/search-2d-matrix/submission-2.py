class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) -1
        mid = right // 2

        while left <= right:
            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[mid]) - 1]:
                return self.binarySearch(matrix[mid], target)
            elif target < matrix[mid][0]:
                right = mid - 1
                mid = (left + right) // 2
            elif target > matrix[mid][len(matrix[mid]) - 1]:
                left = mid + 1
                mid = (left + right) // 2
        return False;


    def binarySearch(self,array:List[int],target:int):
        left = 0
        right = len(array) - 1
        mid =  right //2

        while left <= right:
            if array[mid] == target:
                return True;
            elif array[mid] < target:
                left = mid +1
                mid = (left + right)//2
            else:
                right = mid -1
                mid = (left + right)//2
        return False;