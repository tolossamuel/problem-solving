const INF = 100000000

func floydWarshall(graph [][]int, v int) [][]int {
	dist := make([][]int, v)
	for i := 0; i < v; i++ {
		dist[i] = make([]int, v)
		copy(dist[i], graph[i])
	}

	for k := 0; k < v; k++ {
		for i := 0; i < v; i++ {
			for j := 0; j < v; j++ {
				dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
			}
		}
	}
	return dist
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minimumCost(source string, target string,
	original []byte, changed []byte,
	cost []int,
) int64 {
	g := make([][]int, 26)
	for i := 0; i < 26; i++ {
		g[i] = make([]int, 26)
	}
	for i := 0; i < 26; i++ {
		for j := 0; j < 26; j++ {
			if i == j {
				g[i][j] = 0
				continue
			}
			g[i][j] = INF
		}
	}

	for i := range original {
		tmp := original[i] - 'a'
		tmp2 := changed[i] - 'a'
		g[tmp][tmp2] = min(g[tmp][tmp2], cost[i])
	}

	dist := floydWarshall(g, 26)
	ans := int64(0)
	for i := 0; i < len(source); i++ {
		if dist[source[i] - 'a'][target[i] - 'a'] == INF {
			return -1
		}
		ans = ans + int64(dist[source[i] - 'a'][target[i] - 'a'])
	}
	return ans
}