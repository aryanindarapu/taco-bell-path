#include "TacoBellGraph.h"
#include <algorithm>
#include <queue>

using namespace std;

TacoBellGraph::TacoBellGraph(string filename) {

}

void TacoBellGraph::readFile(string filename) {

}

void TacoBellGraph::insertVertex(TacoBellNode node) {
    nodes.push_back(node);
}

void TacoBellGraph::insertEdge(int id1, int id2) {
    if (id1 >= size() || id2 >= size()) throw runtime_error("Id out of bounds");

    double distance = calculateDistance(id1, id2);

    edges[id1].push_back(Edge(id2, distance));
    edges[id2].push_back(Edge(id1, distance));
}

bool TacoBellGraph::isConnected(int id1, int id2) const {
    return find(edges[id1].begin(), edges[id1].end(), id2) != edges[id1].end();
}

int TacoBellGraph::size() const { return nodes.size(); }

vector<int> TacoBellGraph::dijkstraSearch(int id1, int id2) const {

    priority_queue<int> pq;

    for (TacoBellNode node : nodes) {

    }


    //for reference

    // int dist[V]; // The output array.  dist[i] will hold the
    //              // shortest
    // // distance from src to i
 
    // bool sptSet[V]; // sptSet[i] will be true if vertex i is
    //                 // included in shortest
    // // path tree or shortest distance from src to i is
    // // finalized
 
    // // Initialize all distances as INFINITE and stpSet[] as
    // // false
    // for (int i = 0; i < V; i++)
    //     dist[i] = INT_MAX, sptSet[i] = false;
 
    // // Distance of source vertex from itself is always 0
    // dist[src] = 0;
 
    // // Find shortest path for all vertices
    // for (int count = 0; count < V - 1; count++) {
    //     // Pick the minimum distance vertex from the set of
    //     // vertices not yet processed. u is always equal to
    //     // src in the first iteration.
    //     int u = minDistance(dist, sptSet);
 
    //     // Mark the picked vertex as processed
    //     sptSet[u] = true;
 
    //     // Update dist value of the adjacent vertices of the
    //     // picked vertex.
    //     for (int v = 0; v < V; v++)
 
    //         // Update dist[v] only if is not in sptSet,
    //         // there is an edge from u to v, and total
    //         // weight of path from src to  v through u is
    //         // smaller than current value of dist[v]
    //         if (!sptSet[v] && graph[u][v]
    //             && dist[u] != INT_MAX
    //             && dist[u] + graph[u][v] < dist[v])
    //             dist[v] = dist[u] + graph[u][v];
    // }
 
    // // print the constructed distance array
    // printSolution(dist);
}