class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {} #Create an empty Hash Map

        for word in strs: #Read one word at a time.

            key ="".join(sorted(word)) #This creates the same key for all anagrams.# sorted(word) sorted("eat") returns ['a','e','t']

            if key in groups:  #Does this group already exist?
                groups[key].append(word)
            
            else:
                groups[key] = [word] #Create a new group.
                
        return list(groups.values()) #Convert it to a list:
         