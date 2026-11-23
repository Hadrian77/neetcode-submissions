class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramMap = {}
        resultList = []

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord in anagramMap:
                anagramMap[sortedWord].append(word)
            else:
                anagramMap[sortedWord] = [word]

        for lis in anagramMap.values():
            resultList.append(lis)

        return resultList

        