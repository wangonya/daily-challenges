package main

import (
	"fmt"
	"strings"
)

func lengthOfLastWord(s string) int {
	s = strings.TrimSpace(s)
	last := s[strings.LastIndex(s, " ")+1:]
	return len(last)
}

func main() {
	fmt.Println(lengthOfLastWord("Hello World"))
	fmt.Println(lengthOfLastWord(" "))
	fmt.Println(lengthOfLastWord(""))
	fmt.Println(lengthOfLastWord("a "))
}