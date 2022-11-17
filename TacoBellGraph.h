#include <iostream>
#include <vector>
#include "TacoBellNode.h"

using namespace std;

class Graph {
    public:
        void insertVertex();
        void insertEdge();
        bool isConnected(int, int);
        /**
         * Arguments are the starting and ending coordingates.
         * 
         * Internally, the coordinates will find the first and last Taco Bells that will be visited
         * dijkstraSearch will then be called to find all the Taco Bells in between
         * 
         * Returns all the ids
        */
        vector<int> getPath(int startLong, int startLat, int endLong, int endLat);
    private:
        /**
         * Intenal search for getPath
         * 
         * Returns a vector of all the ids that are from the first and last Taco Bell
        */
        vector<int> dijkstraSearch(int id1, int id2);
        vector<TacoBellNode> vertexList;
        vector<std::vector<int>> edgeLists;
};