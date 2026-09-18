class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded = []
        for s in strs:
            encoded.append(len(s))
            encoded.append("#")
            for c in s:
                encoded.append(c)
        return "".join(map(str, encoded)) 

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = []
        index = 0
        result = []
        while index < len(s):
            next_delim_index = s.find('#', index)
            word_size = int(s[index : next_delim_index])
            word = s[next_delim_index+1 : next_delim_index+1+word_size]
            result.append(word)
            index = next_delim_index+1+word_size
        return result

            
         