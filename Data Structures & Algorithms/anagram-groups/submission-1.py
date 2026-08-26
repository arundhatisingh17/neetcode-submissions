class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_map = {}
        final_list = []

        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in dict_map:
                dict_map["".join(sorted(strs[i]))].append(strs[i])
            else:
                dict_map["".join(sorted(strs[i]))] = [strs[i]]
        
        for key, val in dict_map.items():
            temp_tup = []
            for x in val:
                temp_tup.append(x)

            final_list.append(temp_tup)

        return final_list