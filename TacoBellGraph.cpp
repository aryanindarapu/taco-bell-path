#include "TacoBellGraph.h"
#include <algorithm>
#include <queue>
#include <fstream>
#include <sstream>
#include <iterator>
#include <pair>

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

// if the vector index is simply the id itself, change algorithm to simply return the nodes.at(i) where i is our index
TacoBellNode TacoBellGraph::find(int id) const {
    for (TacoBellNode node : nodes) {
        if (node.store_id_ == id) {
            return node;
        }
    }
    throw runtime_error("node not found");
    return TacoBellNode();
}

vector<int> TacoBellGraph::dijkstraSearch(int id1, int id2) const {

    if (id1 >= nodes.size() || id2 >= nodes.size() || id1 < 0 || id2 < 0)
        throw runtime_error("One id is out of bounds: nodes size = " + nodes.size() + ", id1 = " + id1 + ", id2 = " + id2);

    // based on the dataset, we will just use index for each id
    vector<int> distance(nodes.size(), INT64_MAX);
    vector<int> previous(nodes.size(), -1);
    priority_queue<pair<int, int> pq;

    // this is not implemented but we may needed if the algorithm is not functioning properly
    vector<bool> visited(nodes.size(), false);

    //initial start of our alogrithm
    distance[id1] = 0;
    pq.push(id1, 0);

    while (!pq.empty())
    {
        int current = pq.top().first;
        pq.pop();

        for (int i = 0; i < edges[current].size(); i++) {
            int alt = distance[current] + edges[current][i].distance;

            if (alt < distance[current]) {
                distance[current] = alt;
                previous[current] = current;
                pq.push(pair<int,int>(edges[current][i].dest_id, alt))
            }

            if (edges[current][i].dest_id == id2) {
                break;
            }
        }
    }
    
    if (previous[id2] == -1)
        throw runtime_error("Priority queue ended before reaching our destination node")

    vector<int> path;

    int current = id2;
    while (current != -1) 
    {
        path.push_back(current);
        current = previous(current);
    }

    reverse(path.begin(), path.end());

    return path;
}

/**
 *  Breadth first search from one taco bell to another.
 * 
 *  Returns a vector of all the taco bells that lead to the destination including the first location
*/
vector<int> TacoBellGraph::BFS(int id1, int id2) {

    queue<int> q;
    vector<bool> visited (nodes, false);
    vector<int> previous (nodes.size(), -1);

    q.push(id1);
    visited[id1] = true;

    while (!q.empty()) {

        int current = q.front();
        
        if (current == id2) {

            vector<int> path();
            path.push_back(id2);

            int previous_node = previous[id2];
            while (previous_node != -1) {
                path.push_back(previous_node);
                previous_node = previous[previous_node];
            }
            reverse(previous.begin(), previous.end());
            return path;
        }

        q.pop();
        
        for (Edge e : edges[current]) {
            if (!visited[e.dest_id]) {
                q.push(e.dest_id)
                previous[e.dest_id] = current;
            }
        }

        visited[current] = true;
    }

    return vector<int>();
}