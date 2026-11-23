class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()){
            return false;
        }

        int counter = s.length();
        HashMap<Character,Integer> cache = new HashMap<Character,Integer>();

        for(char letter: s.toCharArray()){
            cache.put(letter,cache.getOrDefault(letter,0) + 1);
        }

        for(char letter: t.toCharArray()){

            if (cache.getOrDefault(letter,0) > 0){
                cache.put(letter,cache.getOrDefault(letter,0) - 1);
            }
            else{
                return false;
            }
            
        }
        
        return true;
        



    }
}
