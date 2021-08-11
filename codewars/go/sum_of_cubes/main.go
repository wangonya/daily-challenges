package main

import "fmt"

func SumOfCubes(x int) int {
	sum := 0
	for n := 1; n <= x; n++ {
		sum += n * n * n
	}
	return sum
}

func main() {
	fmt.Println(SumOfCubes(2))
}

// func SumCubes(num int) int {
//   if num == 1 {
//     return 1
//   }
//   return num*num*num + SumCubes(num-1)
// }
