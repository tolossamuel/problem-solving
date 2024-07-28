func secondMinimum(n int, edges [][]int, time int, change int) int {
    adj := make([][]int, n)
    for _, e := range edges {
        x, y := e[0]-1, e[1]-1
        adj[x] = append(adj[x], y)
        adj[y] = append(adj[y], x)
    }
    g := make([]int, 10_001)
    for i := 1; i < len(g); i++ {
        if (g[i-1] / change) % 2 == 0 {
            g[i] = g[i-1] + time
        } else {
            g[i] = (g[i-1] / change + 1) * change + time
        }
    }
    bfs := func(src int) []int {
        q := []int{src}
        d := make([]int, n)
        for i := 0; i < n; i++ {
            if i != src {
                d[i] = -1
            }
        }
        for len(q) > 0 {
            u := q[0]
            q = q[1:]
            for _, v := range adj[u] {
                if d[v] == -1 {
                    d[v] = d[u] + 1
                    q = append(q, v)
                }
            }
        }
        return d
    }
    src, dst := bfs(0), bfs(n-1)
    first := src[n-1]
    second := math.MaxInt32
    for _, e := range edges {
        x, y := e[0]-1, e[1]-1
        if t := src[x] + dst[y] + 1; t > first && t < second {
            second = t
        }
        if t := src[y] + dst[x] + 1; t > first && t < second {
            second = t
        }
    }
    if second == math.MaxInt32 {
        return g[first+2]
    }
    return g[second]
}