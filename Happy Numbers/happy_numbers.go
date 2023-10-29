package main

import (
	"fmt"
	"strconv"
	"strings"
)

var inputStdin = ""
var inputCursor = 0

func splitAndSquare(number int, calls int) bool {
	calls++
	if number == 1 {
		return true
	} else if calls > 10 {
		return false
	} else {
		digits := strings.Split(strconv.Itoa(number), "")
		total := 0
		for i := 0; i < len(digits); i++ {
			num, _ := strconv.Atoi(digits[i])
			num2 := num * num
			total += num2
		}
		return splitAndSquare(total, calls)
	}
}

func main() {
	startNumber := nextInt()
	endNumber := nextInt()

	happyNums := []int{}
	for i := startNumber; i <= endNumber; i++ {
		if splitAndSquare(i, 0) {
			happyNums = append(happyNums, i)
		}
	}

	fmt.Println(len(happyNums))
	// fmt.Println(happyNums)
}

func nextInt() int {
	return parseInt(nextString())
}

func nextString() string {
	var nextString string
	clearWhitespaces()
	for inputCursor < len(inputStdin) && !isWhitespace(rune(inputStdin[inputCursor])) {
		nextString += string(inputStdin[inputCursor])
		inputCursor++
	}
	return nextString
}

func isWhitespace(character rune) bool {
	return strings.ContainsRune(" \t\n\r\v", character)
}

func clearWhitespaces() {
	for inputCursor < len(inputStdin) && isWhitespace(rune(inputStdin[inputCursor])) {
		inputCursor++
	}
}

func parseInt(s string) int {
	num, _ := strconv.Atoi(strings.TrimSpace(s))
	return num
}
