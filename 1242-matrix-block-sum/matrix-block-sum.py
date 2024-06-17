class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
            
        h, w = len(mat), len( mat[0])
        integral_image = [ [ 0 for y in range(w) ] for x in range(h) ]
        for y in range(0, h):
            summation = 0
            
            for x in range(0, w):
                summation += mat[y][x]
                integral_image[y][x] = summation
                
                if y > 0:
                    integral_image[y][x] += integral_image[y-1][x]
        output = [ [ 0 for y in range(w) ] for x in range(h) ]
        
        for y in range(h):
            for x in range(w):
                
                min_r, max_r = max( 0, y-K), min( h-1, y+K)
                min_c, max_c = max( 0, x-K), min( w-1, x+K)
                
                output[y][x] = integral_image[max_r][max_c]
                
                if min_r > 0:
                    output[y][x] -= integral_image[min_r-1][max_c]
                
                if min_c > 0:
                    output[y][x] -= integral_image[max_r][min_c-1]
                    
                if min_c > 0 and min_r > 0:
                    output[y][x] += integral_image[min_r-1][min_c-1]
                
        return output