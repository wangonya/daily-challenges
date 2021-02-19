package main

import (
	"fmt"
)

// func twoSum(nums []int, target int) []int {
// 	sort.Ints(nums)
// 	left := 0
// 	right := len(nums)-1
// 	for {
// 		fmt.Println("nums =", nums)
// 		sum := nums[left] + nums[right]
// 		fmt.Println("sum =", sum)
// 		fmt.Println("left =", left)
// 		fmt.Println("right =", right)
// 		if sum == target {
// 			break
// 		} else if sum > target {
// 			right--
// 		} else if sum < target {
// 			left++
// 		}
// 	}

// 	return []int{left, right}
// }

func twoSum(nums []int, target int) []int {
	var m map[int]int
	m = make(map[int]int)
	result := []int{}
	for i := 0; i < len(nums); i++ {
		remainder := target - nums[i]
		n, exists := m[remainder]
		if exists {
			result = []int{i, n}
		}
		m[nums[i]] = i
	}
	return result
}

func main() {
	nums := []int{3, 2, 4}
	target := 6
	result := twoSum(nums, target)
	fmt.Println(result)
}

// func twoSum(nums []int, target int) []int {
//     m := make(map[int]int)
//     for i, v := range nums {
//         fmt.Println(v)
//         compliment := target - v
//         if _, ok := m[compliment]; ok {
//             return []int{m[compliment], i}
//         }

//         m[v] = i
//     }
    
//     fmt.Println(m)
    
//     return []int{}
// }