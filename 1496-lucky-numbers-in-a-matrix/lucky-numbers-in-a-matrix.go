import "fmt"
func luckyNumbers (matrix [][]int) []int {
    row := make([]int,len(matrix[0]))
    col := make([]int, len(matrix))
    for i,_ := range matrix{
        for j,val := range matrix[i]{
            if row[j] < val || row[j] == 0{
                row[j] = val
            }
            if col[i] > val || col[i] == 0{
                col[i] = val
            }
        }
    }
    ans := []int{}
 
    for _,val := range row{
        for _,vall := range col{
            if val == vall{
                ans = append(ans,val)
            }
        }
    }
    return ans
}