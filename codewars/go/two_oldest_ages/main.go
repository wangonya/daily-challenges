package main

import "fmt"

func TwoOldestAges(ages []int) [2]int {
	oldest := 0
	second_oldest := 0

	for _, age := range ages {
		if age > oldest {
			second_oldest = oldest
			oldest = age
		} else if age > second_oldest {
			second_oldest = age
		}
	}

	return [2]int{second_oldest, oldest}
}

func main() {
	fmt.Println(TwoOldestAges([]int{1, 5, 87, 45, 8, 8}))
	fmt.Println(TwoOldestAges([]int{61, 11, 33, 79, 81, 27, 79, 83, 9, 95}))
}
