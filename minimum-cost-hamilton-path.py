#Problem: Minimum Cost Hamiltonian Path (Graph + DP + Bitmask)
#Description

#Given a directed weighted graph, find the minimum cost Hamiltonian path (visiting every vertex exactly once) without returning to the start.

#Variant of TSP, but no need to return to starting node

#Solved using DP + Bitmask in O(n² * 2^n)

#Useful in logistics, robotics path planning, task scheduling



import sys

def min_cost_hamiltonian_path(graph):
    n = len(graph)
    dp = [[float('inf')]*n for _ in range(1<<n)]
    for i in range(n):
        dp[1<<i][i] = 0  # start at each node

    for mask in range(1<<n):
        for u in range(n):
            if not (mask & (1<<u)):
                continue
            for v in range(n):
                if mask & (1<<v):
                    continue
                dp[mask | (1<<v)][v] = min(dp[mask | (1<<v)][v], dp[mask][u] + graph[u][v])

    full_mask = (1<<n) - 1
    return min(dp[full_mask][i] for i in range(n))

# ---------------- Example Usage ----------------
if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    print("Minimum Hamiltonian Path cost:", min_cost_hamiltonian_path(graph))
