class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = defaultdict(list)
        for w in strs:
            count = [0] * 26
            for ch in w:
                count[ord(ch) - ord('a')] += 1

            
            anagram[tuple(count)].append(w)
        return list(anagram.values())