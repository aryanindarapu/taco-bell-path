#include <iostream>
#include <vector>
#include "TacoBellNode.h"

class Graph {
    public:
        void insertVertex();
        void insertEdge();
        bool isConnected(int, int);
        void dijkstraSearch(int hungriness, int startLong, int startLat, int endLong, int endLat);
    private:
        std::vector<TacoBellNode> vertexList;
        std::vector<std::vector<int>> edgeLists;
};