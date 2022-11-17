#include "TacoBellGraph.h"
#include <algorithm>

using namespace std;

void TacoBellGraph::insertVertex(TacoBellNode node) {
    nodes.push_back(node);
}

void TacoBellGraph::insertEdge(int id1, int id2) {
    if (id1 >= size() || id2 >= size()) throw runtime_error("Id out of bounds");

    edges[id1].push_back(id2);
    edges[id2].push_back(id1);
}

bool TacoBellGraph::isConnected(int id1, int id2) const {
    return find(edges[id1].begin(), edges[id1].end(), id2) != edges[id1].end();
}

int TacoBellGraph::size() const { return nodes.size(); }