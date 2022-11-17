#include <iostream>
#include <vector>
#include "TacoBellNode.h"

using namespace std;

class TacoBellGraph {
    public:
        TacoBellGraph(string filename);
        void insertVertex(TacoBellNode node);
        void insertEdge(int id1, int id2);
        bool isConnected(int id1, int id2);
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
        void readFile(string filename);

        vector<TacoBellNode> nodes;
        vector<std::vector<int>> edges;
};