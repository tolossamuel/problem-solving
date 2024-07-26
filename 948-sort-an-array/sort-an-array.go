import "fmt"
func merge_sort(n []int ) []int{
	if len(n) > 1{
		mid := len(n) / 2
		left := make([]int, mid)
		right := make([]int, len(n)-mid)
		copy(left, n[:mid])
		copy(right, n[mid:])
        merge_sort(left)
		merge_sort(right)
		var l int= 0
		var r int = 0
		var i int = 0
		for l < len(left) && r < len(right){
			if left[l] <= right[r]{
				n[i] = left[l]
				l += 1
			} else {
				n[i] = right[r]
				r += 1
			}
			i += 1
		}
		for l < len(left){
			n[i] = left[l]
			i += 1
			l += 1
		}
		for r < len(right) {
			n[i] = right[r]
			i += 1
			r += 1
		}
		
		
		return n
	}
	return n
}
func sortArray(nums []int) []int {
    nums = merge_sort(nums)
    return nums
    
}