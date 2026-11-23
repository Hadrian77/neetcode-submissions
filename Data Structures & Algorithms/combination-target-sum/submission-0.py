class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        global finalStore
        finalStore = []


        for x in nums:
            self.add(nums,target,[],x)
        
        return finalStore


    def add(self,nums: List[int],target: int,store: List[int], new: int):
        


        target -= new
        store.append(new)

        if target == 0:
            store.sort()

            if store in finalStore:
                    return
            else:    
                finalStore.append(store)
                return
        
        elif target < 0:
            return
        
        else:
            for x in nums:
                self.add(nums,target,store.copy(),x)

   
        