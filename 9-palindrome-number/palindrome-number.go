import "fmt"
func reve(y string) string {
    ans := ""

    for _,v := range y{
     
        ans = string(v) + ans
    }

    return ans
}
func isPalindrome(x int) bool {
    y := fmt.Sprint(x)
    // fmt.Printf("%T",y[::-1])
    // fmt.
    return y == reve(y)
  
    
}