class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for word in strs:
            encoded += (str(len(word)))
            encoded += ","
        encoded += '&'

        for word in strs:
            encoded += word
        
        return encoded
        

    def decode(self, s: str) -> List[str]:

        currentLength = ""
        lengths = []
        index = 0

        for char in s:
            index += 1
            if char == '&':
                index + 1
                break
            if char == ',':
                lengths.append(int(currentLength))
                currentLength = ""
                continue
            currentLength += char
            
        
        result = []
        
        for length in lengths:
            result.append(s[index: index + length])
            index += length

        return result
        
        



            

