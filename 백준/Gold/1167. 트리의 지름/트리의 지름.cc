#include <iostream>
#include <vector>
#include <stack>
#include <utility>
using namespace std;

// Returns {farthest_node, max_distance} from a given start
pair<int,int> get_farthest(int start, const vector<vector<pair<int,int>>> &graph) {
    int n = graph.size();
    vector<bool> visit(n, false);
    stack<pair<int,int>> st;
    st.push({start, 0});
    int far_node = start;
    int max_dist = 0;
    
    while (!st.empty()) {
        auto [u, dist] = st.top();
        st.pop();
        if (visit[u]) continue;
        visit[u] = true;
        if (dist > max_dist) {
            max_dist = dist;
            far_node = u;
        }
        for (auto &edge : graph[u]) {
            int v = edge.first;
            int w = edge.second;
            if (!visit[v]) {
                st.push({v, dist + w});
            }
        }
    }
    return {far_node, max_dist};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int v;
    cin >> v;
    vector<vector<pair<int,int>>> graph(v + 1);

    for (int i = 0; i < v; i++) {
        int src;
        cin >> src;
        while (true) {
            int dst;
            cin >> dst;
            if (dst == -1) break;
            int w;
            cin >> w;
            graph[src].emplace_back(dst, w);
        }
    }

    // 1) from node 1 find farthest A
    auto p = get_farthest(1, graph);
    // 2) from A find diameter
    auto q = get_farthest(p.first, graph);

    cout << q.second << '\n';
    return 0;
}
