package main

import (
	"fmt"
	"strconv"
)

func reverse(str string) (result string) {
	for _, v := range str {
		result = string(v) + result
	}
	return
}

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	return reverse(strconv.Itoa(x)) == strconv.Itoa(x)
}

func main() {
	res := isPalindrome(101)
	fmt.Println(res)
}

// less memory
// func isPalindrome(x int) bool {
//     if x < 0 || (x > 0 && x % 10 == 0) {
//         return false;
//     }
    
//     y := 0
//     for ; x >= y; {
//         if x == y || x / 10 == y {
//             return true
//         }
//         y = y * 10 + x % 10
//         x /= 10
//     }
//     return false
// }

// func isPalindrome(x int) bool {
// 	s := 0
// 	d := x
// 	for d != 0 {
// 		t := d % 10
// 		d = d / 10
// 		s = s*10 + t
// 	}
// 	if x != s {
// 		return false
// 	} else if x < 0 {
// 		return false
// 	} else {
// 		return true
// 	}
// }

// func isPalindrome(x int) bool {
//     strNum := strconv.Itoa(x)
    
//     first := 0
//     last := len(strNum) - 1
//     for first < last {
//         if strNum[first] == strNum[last] {
//             first++
//             last--
//             continue
//         }
        
//         return false
//     }
    
//     return true
// }


// faster
// func isPalindrome(x int) bool {
//     if x < 0 {
//         return false
//     }
//     ans := 0
//     b := x
//     for b > 0 {
//         ans = ans*10 + b%10
//         b = b/10
//     }
//     return ans == x
// }