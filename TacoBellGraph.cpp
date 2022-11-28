#include "TacoBellGraph.h"
#include <algorithm>
#include <queue>
#include <fstream>
#include <sstream>
#include <iterator>

using namespace std;

TacoBellGraph::TacoBellGraph(string filename) {
    readFile(filename);
}

void TacoBellGraph::readFile(string filename) {
    ifstream taco_bells(filename);

     if (taco_bells.is_open()) {
        std::istream_iterator<string> taco_bell_iter(taco_bells);
        ++taco_bell_iter;
        while (!taco_bells.eof()) {
            string line = *taco_bell_iter;

            stringstream ss(line);

            vector<string> tokens;
            string token;
            while (getline(ss, token, ',')) tokens.push_back(token);

            int id = stoi(tokens[1]);
            string address = tokens[2];
            double lat = stod(tokens[3]);
            double lon = stod(tokens[4]);

            insertVertex(lat, lon, address, id);
            
            edges.push_back(vector<Edge>());
            insertEdge(id, stoi(tokens[5]), stod(tokens[8]));
            insertEdge(id, stoi(tokens[6]), stod(tokens[9]));
            insertEdge(id, stoi(tokens[7]), stod(tokens[10]));
            
            ++taco_bell_iter;
        }
    }
}

void TacoBellGraph::insertVertex(double latitude, double longitude, std::string address, int store_id) {
    TacoBellNode node(latitude, longitude, address, store_id);
    nodes.push_back(node);
}

void TacoBellGraph::insertEdge(int id1, int id2, double distance) {
    edges[id1].push_back(Edge(id2, distance));
}

bool TacoBellGraph::isConnected(int id1, int id2) const {
    for (Edge edge : edges[id1]) 
        if (edge.dest_id == id2) return true;
    return false;
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