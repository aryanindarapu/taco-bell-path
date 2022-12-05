#include <iostream>
#include <vector>
#include "TacoBellNode.h"

class TacoBellGraph {
    public:
        TacoBellGraph() = default;
        TacoBellGraph(std::string filename);
        void insertVertex(double latitude, double longitude, std::string address, int store_id);
        void insertEdge(int id1, int id2, double distance);
        bool isConnected(int id1, int id2) const;
        int size() const;
        double getDistance(int id1, int id2) const;
        std::string getAddress(int id) const;
        double getLatitude(int id) const;
        double getLongitude(int id) const;
        
        /**
         * Arguments are the starting and ending coordingates.
         * 
         * Internally, the coordinates will find the first and last Taco Bells that will be visited
         * dijkstraSearch will then be called to find all the Taco Bells in between
         * 
         * Returns all the ids
        */
        std::vector<int> getPath(int startLong, int startLat, int endLong, int endLat) const;

        /**
         *  Breadth first search from one taco bell to another.
         * 
         *  Returns a vector of all the taco bells that lead to the destination including the first location
        */
        std::vector<int> BFS(int id1, int id2);
        
        /**
         * Internal search for getPath
         * 
         * Returns a vector of all the ids that are from the first and last Taco Bell
        */
        std::vector<int> dijkstraSearch(int id1, int id2) const;

        /**
         * Betweeness centrality algorithm
         * 
         * Returns the betweenness centrality of the given node
        */
        int betweennessCentrality(int id);

        /**
         * Algorithms that returns the taco bells on the way from Champaign to Chicago
         * 
         * Returns a vector of node IDs
        */
        std::vector<int> champaignToChicago();

    private:
        

        /**
         * Reads csv file with Taco Bell locations data
        */
        void readFile(std::string filename);

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

        std::vector<TacoBellNode> nodes;
        std::vector<std::vector<Edge>> edges;
};