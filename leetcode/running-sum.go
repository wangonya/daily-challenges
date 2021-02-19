package main

import "fmt"

func runningSum(nums []int) []int {
	for i := 1; i < len(nums); i++ {
		nums[i] = nums[i] + nums[i-1]
	}
	return nums
}

func main() {
	result := runningSum([]int{1, 2, 3, 4})
	fmt.Println(result)
}
