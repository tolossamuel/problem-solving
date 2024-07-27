func isValid(s string) bool {
    stack := []string{}
    for _,x := range s{
        if string(x) == ")"{
            if len(stack) > 0 && stack[len(stack)-1] == "("{
                stack = stack[:len(stack)-1]
            } else {
                return false
            }
        } else if string(x) == "}" {
            if len(stack) > 0 && stack[len(stack)-1] == "{"{
                stack = stack[:len(stack)-1]
            } else {
                return false
            }
        } else if string(x) == "]" {
            if len(stack) > 0 && stack[len(stack)-1] == "["{
                stack = stack[:len(stack)-1]
            } else {
                return false
            }
        } else {
            stack = append(stack,string(x))
        }

    }
    return len(stack) == 0
}