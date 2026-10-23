class Solution:

    def encode(self, strs: List[str]) -> str:
        # num_strs = len(strs)
        # len_strs = [len(s) for s in strs]

        return ''.join([chr(len(strs))] + [chr(len(s)) for s in strs]) + "".join(strs)

    def decode(self, s: str) -> List[str]:
        num_strs = ord(s[0])
        len_strs = [ord(s[i]) for i in range(1, num_strs + 1)]
        retval = []
        curr_index = num_strs + 1
        for l in len_strs:
            retval.append(s[curr_index: curr_index + l])
            curr_index += l
        return retval
