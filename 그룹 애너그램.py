#그룹 애너그램
#답
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an = collections.defaultdict(list)
        
        for word in strs:
            an[''.join(sorted(word))].append(word)
        
        return list(an.values())
