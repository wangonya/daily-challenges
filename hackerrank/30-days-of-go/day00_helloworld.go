package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// read string from input
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	inp := scanner.Text()
	fmt.Println("Hello, World.")
	fmt.Println(inp)
}
