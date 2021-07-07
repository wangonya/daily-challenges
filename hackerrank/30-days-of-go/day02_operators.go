package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// Complete the solve function below.
func solve(meal_cost float64, tip_percent int, tax_percent int) {
	tip_cost := float64(tip_percent) / 100 * meal_cost
	tax_cost := float64(tax_percent) / 100 * meal_cost
	total_cost := int(meal_cost + tip_cost + tax_cost + 0.5) // add 0.5 to round to the nearest int
	fmt.Println(total_cost)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	meal_cost, err := strconv.ParseFloat(readLine(reader), 64)
	checkError(err)

	tip_percentTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	tip_percent := int(tip_percentTemp)

	tax_percentTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	tax_percent := int(tax_percentTemp)

	solve(meal_cost, tip_percent, tax_percent)
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
