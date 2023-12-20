class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s_list = list(s)
        modified_list = []
        prev_index = 0
        
        for space_index in spaces:
            modified_list.append(''.join(s_list[prev_index:space_index]))
            modified_list.append(' ')
            prev_index = space_index

        modified_list.append(''.join(s_list[prev_index:]))

        return ''.join(modified_list)
