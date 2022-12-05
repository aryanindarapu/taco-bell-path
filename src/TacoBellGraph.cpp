#include "TacoBellGraph.h"
#include <algorithm>
#include <iostream>
#include <queue>
#include <fstream>
#include <sstream>
#include <iterator>
#include <utility>
#include <limits>

TacoBellGraph::TacoBellGraph(std::string filename) {
    readFile(filename);
}

void TacoBellGraph::readFile(std::string filename) {
    std::ifstream taco_bells{filename};

    if (taco_bells.is_open()) {
        std::vector<std::vector<std::string>> csvRows;

        for (std::string line; getline(taco_bells, line);) {
            std::istringstream ss(move(line));

            std::vector<std::string> row;

            if (!csvRows.empty()) {
            // We expect each row to be as big as the first row
                row.reserve(csvRows.front().size());
            }
            // std::getline can split on other characters, here we use ','
            for (std::string value; std::getline(ss, value, ',');) {
                row.push_back(std::move(value));
            }
            csvRows.push_back(std::move(row));
        }

        for (size_t i = 1; i < csvRows.size(); i++) {
            int id = stoi(csvRows[i][1]);
            std::string address = csvRows[i][2];
            double lat = stod(csvRows[i][3]);
            double lon = stod(csvRows[i][4]);
    
            insertVertex(lat, lon, address, id);
            
            edges.push_back(std::vector<Edge>());
            insertEdge(id, stoi(csvRows[i][5]), stod(csvRows[i][8]));
            insertEdge(id, stoi(csvRows[i][6]), stod(csvRows[i][9]));
            insertEdge(id, stoi(csvRows[i][7]), stod(csvRows[i][10]));
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

std::string TacoBellGraph::getAddress(int id) const {
    return nodes.at(id).address_;
}

double TacoBellGraph::getLatitude(int id) const {
    return nodes.at(id).latitude_;
}

double TacoBellGraph::getLongitude(int id) const {
    return nodes.at(id).longitude_;
}

double TacoBellGraph::getDistance(int id1, int id2) const {
    for (Edge edge : edges.at(id1)) {
        if (edge.dest_id == id2) {
            return edge.distance;
        }
    }
    throw std::runtime_error("node not found");
}

int TacoBellGraph::size() const { return nodes.size(); }

// if the vector index is simply the id itself, change algorithm to simply return the nodes.at(i) where i is our index
TacoBellNode TacoBellGraph::find(int id) const {
    for (TacoBellNode node : nodes) {
        if (node.store_id_ == id) {
            return node;
        }
    }
    throw std::runtime_error("node not found");
}

/**
 * Internal function to print out the priority queue.
 * All values are negative. Read pq in dijkstraSearch
*/
void printPQ(std::priority_queue<std::pair<int, int>> pq) {
    while (!pq.empty()) {
        std::cout << pq.top().first << "\t";
        pq.pop();
    }
    std::cout << std::endl;
}

std::vector<int> TacoBellGraph::dijkstraSearch(int id1, int id2) const {

    // Checks for valid ids
    if (id1 >= (int) nodes.size() || id2 >= (int) nodes.size() || id1 < 0 || id2 < 0)
        throw std::runtime_error("One id is out of bounds: nodes size = " + std::to_string(nodes.size()) + ", id1 = " + std::to_string(id1) + ", id2 = " + std::to_string(id2));

    // based on the dataset, we will just use index for each id
    std::vector<int> distance(nodes.size(), std::numeric_limits<int>::max());
    std::vector<int> previous(nodes.size(), -1);
    std::vector<bool> visited(nodes.size(), false);

    // Priority queue with distance as first and id as second
    // distances are represented as negative values as the pq uses a max heap
    std::priority_queue<std::pair<int, int>> pq;

    //initial start of our alogrithm
    distance[id1] = 0;
    pq.push(std::pair<int,int>(0, id1));

    while (!pq.empty())
    {   
        int current = pq.top().second;
        pq.pop();

        // current is the destination, we will terminate the pq
        if (current == id2) break;

        for (size_t i = 0; i < edges[current].size(); i++) {

            // out of scope location or we already visited the node, not going to use it
            if (edges[current][i].dest_id == -1 || visited[edges[current][i].dest_id]) {
                continue;
            }

            // we will use the distance found in our distance vecotor and add it with the edge distance.
            int alt = distance[current] + edges[current][i].distance;

            // since all values in the distance is vector, theres a safe check to ensure that alt > 0
            if (alt < distance[edges[current][i].dest_id] && alt > 0) {
                distance[edges[current][i].dest_id] = alt;
                previous[edges[current][i].dest_id] = current;
                // Again, alt is negative since pq is max heap
                pq.push(std::pair<int,int>(-alt, edges[current][i].dest_id));
            }

        }
        
        // Mark our current id that we visited it.
        visited[current] = true;
    }

    // This is to check that id2 has been marked and given a previous. If 
    if (previous[id2] == -1)
        throw std::runtime_error("Priority queue ended before reaching our destination node");

    // Generates a path that takes us back to our start id
    std::vector<int> path;
    int current = id2;
    while (current != -1) {
        path.push_back(current);
        current = previous[current];
    }

    // Path is backwards, so we need to reverse it
    reverse(path.begin(), path.end());

    return path;
}

/**
 *  Breadth first search from one taco bell to another.
 * 
 *  Returns a vector of all the taco bells that lead to the destination including the first location
*/
std::vector<int> TacoBellGraph::BFS(int id1, int id2) {
    if (id1 < 0 || (unsigned int) id1 >= nodes.size() || id2 < 0 || (unsigned int) id2 >= nodes.size())
        throw std::runtime_error("id1 or id2 is out of bounds.");
    
    std::queue<int> q;
    std::vector<bool> visited (nodes.size(), false);
    std::vector<int> previous (nodes.size(), -1);

    q.push(id1);

    // Will recieve an error that vecotor is trying to access at index -1 when id1 is not
    visited[id1] = true;

    while (!q.empty()) {

        int current = q.front();
        
        if (current == id2) {

            std::vector<int> path;
            path.push_back(id2);

            int previous_node = previous[id2];
            while (previous_node != -1) {
                path.push_back(previous_node);
                previous_node = previous[previous_node];
            }
            reverse(path.begin(), path.end());
            return path;
        }

        q.pop();
        
        for (Edge e : edges[current]) {
            // out of scope id
            if (e.dest_id == -1)
                continue;
            // valid id
            if (!visited[e.dest_id]) {
                q.push(e.dest_id);
                previous[e.dest_id] = current;
            }
        }

        visited[current] = true;
    }

    return std::vector<int>();
}

/**
 * Betweeness centrality algorithm 
 * 
 * Given a certain node, this algorithm will check the shortest weighted paths for every pair of nodes in the graph.
 * The algorithm divides the number of shortest paths with the given node in it, for a pair of nodes, by the total number of
 * shortest paths, for those same pair of nodes. In this case, every pair of nodes has a unique set of shortest paths,
 * thus the betweeness centrality will be an integer indicated the number of shortest paths in the graph containing that node.
 * Returns the betweenness centrality of the given node
*/
int TacoBellGraph::betweennessCentrality(int id) {
    int betweeness = 0;
    for (unsigned long i = 0; i < nodes.size(); i++) {
        if (i == (unsigned long) id) continue;
        for (unsigned long j = i + 1; j < nodes.size(); j++) {
            if (j == (unsigned long) id) continue;
            std::vector<int> searchList = dijkstraSearch(i, j);
            if (std::find(searchList.begin(), searchList.end(), id) != searchList.end()) betweeness += 1;
        }
    }

    return betweeness;
}