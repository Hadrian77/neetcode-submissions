class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        arr = []
        candidates.sort()
        def bk(index,candidates,target,current,arr):


            if current == target:
                nonlocal result
                result.append(arr)
                return
            
            if current > target:
                return


            if index > len(candidates) -1:
                return


            
            
            arr.append(candidates[index])

            bk(index + 1,candidates,target,current + candidates[index],arr.copy())

            arr.pop(-1)
            
            while index < len(candidates) -1 and candidates[index] == candidates[index + 1] :
                index += 1
            
            bk(index + 1,candidates,target,current,arr.copy())

        bk(0,candidates,target,0,arr)
        return result