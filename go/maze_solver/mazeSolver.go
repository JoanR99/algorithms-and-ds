package main

import "fmt"

type Point struct {
	x int
	y int
}

func walk(
	maze []string,
	wall string,
	current Point,
	end Point,
	seen [][]bool,
	path *[]Point,
) bool {
	dir := [][]int{
		{0, -1},
		{1, 0},
		{0, 1},
		{-1, 0},
	}

	// Base cases
	//1. Off the map
	if current.x < 0 || current.x >= len(maze[0]) || current.y < 0 || current.y >= len(maze) {
		return false
	}

	//2. On a wall
	c := string(maze[current.y][current.x])
	if c == wall {
		return false
	}

	//3. End
	if current.x == end.x && current.y == end.y {
		*path = append(*path, end)
		return true
	}

	//4. Seen
	if seen[current.y][current.x] {
		return false
	}

	//Recursive cases
	// Pre
	newSeen := make([]bool, len(seen[0]))

	copy(newSeen, seen[current.y])

	newSeen[current.x] = true
	seen[current.y] = newSeen
	*path = append(*path, current)

	// Recurse
	for i := 0; i < len(dir); i++ {
		points := dir[i]
		newPoint := Point{x: current.x + points[0], y: current.y + points[1]}

		if walk(maze, wall, newPoint, end, seen, path) {
			return true
		}
	}

	// Post
	*path = (*path)[:len(*path)-1]
	return false
}

func solve(maze []string, wall string, start Point, end Point) []Point {
	seen := [][]bool{}
	path := []Point{}
	seenRow := []bool{}

	for i := 0; i < len(maze[0]); i++ {
		seenRow = append(seenRow, false)
	}

	for i := 0; i < len(maze); i++ {
		seen = append(seen, seenRow)
	}

	walk(maze, wall, start, end, seen, &path)

	return path
}

func main() {
	maze := []string{
		"### ",
		"# # ",
		"# # ",
		"    ",
		"# ##",
		"#   ",
		"# ##",
	}
	start := Point{x: 1, y: 6}
	end := Point{x: 3, y: 0}

	result := solve(maze, "#", start, end)

	fmt.Println(result)
}
