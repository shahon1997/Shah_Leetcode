class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] # assumes the first element in the list as a whole is a prefix

        for string in strs[1:]: # iterates starting from the second element 
        # bcs ov comparison with the first is pointless
            while not string.startswith(prefix): # if the word not the prefix it slices it
                prefix = prefix[:-1]
            # functionally it will give as the common prefix(the longest)
            if prefix == "":
                return ""
        return prefix
