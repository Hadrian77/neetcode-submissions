class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        current = 1
        hasZero = 0

        for x in nums:
            if x != 0:
                current = current * x
            else:
                hasZero += 1
                continue
        
        result = []


        if not hasZero:
            for x in nums:
                result.append(int(current/x))
        
        else:
            if hasZero > 1:
                for x in nums:
                    result.append(0)
            else:
                for x in nums:
                    if x == 0:
                        result.append(current)
                    else:
                        result.append(0)
        
        return result
        