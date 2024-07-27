func productExceptSelf(nums []int) []int {
    sufix := []int{1,nums[len(nums)-1]}
    n := len(nums)-2
    for n >= 0 {
        temp := sufix[len(sufix)-1] * nums[n]
        sufix = append(sufix,temp)
        n -= 1
    }
    ans := []int{}
    _mul := 1
    n = len(sufix)-2
    for i,x := range nums{
        temp := sufix[n-i] * _mul
        _mul *= x
        ans = append(ans,temp)
        
    }
    return ans

}