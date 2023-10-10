class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            for y in range(len(heights)-1,0,-1):
                if(heights[y]>heights[y-1]):
                    heights[y],heights[y-1]=heights[y-1],heights[y]
                    names[y],names[y-1]=names[y-1],names[y]

        return names