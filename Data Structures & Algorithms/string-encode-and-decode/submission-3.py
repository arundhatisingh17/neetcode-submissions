class Solution:

    def encode(self, strs: List[str]) -> str:

        str_builder = ""
        for i in range(len(strs)):
            local_len = len(strs[i])
            str_builder += str(local_len)
            str_builder += '#'
            str_builder += strs[i]

        return str_builder

    def decode(self, s: str) -> List[str]:

        final_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j = j + 1
            
            number = int(s[i : j])
            start = j + 1
            str_builder = s[start : start + number]
            final_list.append(str_builder)

            i = start + number

        return final_list