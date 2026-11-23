class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers) - 1

        while True:
            current = numbers[i] + numbers[j]
            if current == target:
                break
            if current < target:
                i += 1
            else:
                j -= 1

        
        return [i + 1,j + 1]