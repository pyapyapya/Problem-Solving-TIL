#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>

#define MAX 1000000000

int n, m, x;
bool visited[1002] = { 0 };
int dist[1002] = { 0 };
int dp[1002];

using namespace std;

vector<pair<int, int>> graph[1001];
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

int dijkstra(int start, int end, int flag) {

	fill(visited, visited + n + 1, 0);
	fill(dist, dist + n + 1, MAX);

	dist[start] = 0;
	pq.push(make_pair(0, start));

	while (!pq.empty()) {
		int cur;
		do {
			cur = pq.top().second;
			pq.pop();
		} while (!pq.empty() && visited[cur]);

		if (visited[cur]) break;
		visited[cur] = true;

		for (auto &p : graph[cur]) {
			int next = p.first;
			int d = p.second;

			if (dist[next] > dist[cur] + d) {
				dist[next] = dist[cur] + d;
				pq.push(make_pair(dist[next], next));
			}
		}	
	}
	if (!flag) {
		if (dist[end] == MAX)
			return 0;
		else
			return dist[end];
	}
	else {
		for (int i = 1; i <= n; i++) {
			dp[i] += dist[i];
		}
		return 0;
	}
}

int main() {
	int ans = 0;
	cin >> n >> m >> x;

	for (int i = 0; i < m; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		graph[u].push_back(make_pair(v, w));
	}

	for (int i = 1; i <= n; i++) {
		dp[i] = dijkstra(i, x, 0);
	}

	dijkstra(x, 1001, 1);
	
	cout << *max_element(dp, dp+n+1);
	return 0;
}