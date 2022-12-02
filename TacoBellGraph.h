#include <iostream>
#include <vector>
#include "TacoBellNode.h"

using namespace std;

class TacoBellGraph {
    public:
        TacoBellGraph(string filename);
        void insertVertex(double latitude, double longitude, std::string address, int store_id);
        void insertEdge(int id1, int id2, double distance);
        bool isConnected(int id1, int id2) const;
        int size() const;
        double getDistance(int id1, int id2) const;
        
        /**
         * Arguments are the starting and ending coordingates.
         * 
         * Internally, the coordinates will find the first and last Taco Bells that will be visited
         * dijkstraSearch will then be called to find all the Taco Bells in between
         * 
         * Returns all the ids
        */
        vector<int> getPath(int startLong, int startLat, int endLong, int endLat) const;

        /**
         *  Breadth first search from one taco bell to another.
         * 
         *  Returns a vector of all the taco bells that lead to the destination including the first location
        */
        vector<int> BFS(int id1, int id2);
        
    private:
        /**
         * Intenal search for getPath
         * 
         * Returns a vector of all the ids that are from the first and last Taco Bell
        */
        vector<int> dijkstraSearch(int id1, int id2) const;

        /**
         * Reads csv file with Taco Bell locations data
        */
        void readFile(string filename);

        /**
         * Calculates the distance between two nodes using Google Maps API
        */
        double calculateDistance(int id1, int id2) const;

        /**
         * Edge struct for storing destiny id and distance(weight)
        */
        struct Edge {
            Edge(int dest_id_, double distance_) {
                dest_id = dest_id_;
                distance = distance_;
            }

            int dest_id;
            double distance;
        };

        /**
         * @brief Helper function to find the node that corresponds to the id
         * 
         * @param id is the id that we want the node for
         * @return TacoBellNode of that id 
         */
        TacoBellNode find(int id) const;

        vector<TacoBellNode> nodes;
        vector<std::vector<Edge>> edges;
};