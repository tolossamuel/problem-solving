
func twoSum(nums []int, target int) []int {
    maps := make(map[int]int)
    for x,y := range nums{
        dif := target - y
        val,exist := maps[dif]
        if exist{
            ans := []int{x,val}
            return ans
        }
        maps[y] = x
    }
    ans := []int{1,1}
           
    return ans
    
}