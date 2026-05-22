class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = {}
        result =[]
        for words in strs:
            count = [0] * 26
            for char in range(len(words)):
                count[ord(words[char]) - ord('a')] += 1
            key = tuple(count)
            if key not in anagram:
                anagram[key] = [words]
            else:
                anagram[key].append(words)
        result = anagram.values()
        return result
            
                 