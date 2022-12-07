#include <catch2/catch_test_macros.hpp>

#include "TacoBellGraph.h"

using namespace std;

string vectorToString(vector<int> vect) {
    string out = "(";

    for (size_t i = 0; i < vect.size(); i++) {
        out.push_back(vect[i]);
        if (i != vect.size() - 1) {
            out.push_back(',');
            out.push_back(' ');
        }
    }

    out.push_back(')');
    return out;
}


TEST_CASE("graph size is correct", "[weight=5") {
    TacoBellGraph graph("../data/final_data_dist.csv");
    REQUIRE(graph.size() == 285);
}

TEST_CASE("test node 1", "[weight=5][timeout=8000]") {
    TacoBellGraph graph("../data/final_data_dist.csv");
    REQUIRE(graph.getAddress(0) == "555 W. Lake St.");
    REQUIRE(graph.getLatitude(0) == 41.93787872988775);
    REQUIRE(graph.getLongitude(0) == -88.00291031599045);

    REQUIRE(graph.isConnected(0, 159));
    REQUIRE(graph.getDistance(0, 159) == 2.8);
    REQUIRE(graph.getAddress(159) == "322 W Irving Park Rd");

    REQUIRE(graph.isConnected(0, 6));
    REQUIRE(graph.getDistance(0, 6) == 4.0);
    REQUIRE(graph.getAddress(6) == "1140 S York Rd");

    REQUIRE(graph.isConnected(0, 239));
    REQUIRE(graph.getDistance(0, 239) == 5.2);
    REQUIRE(graph.getAddress(239) == "270 E Army Trail Rd");
}

TEST_CASE("test node 2", "[weight=5][timeout=8000]") {
    TacoBellGraph graph("../data/final_data_dist.csv");
    REQUIRE(graph.getAddress(167) == "2410 E Rand Rd");
    REQUIRE(graph.getLatitude(167) == 42.094717788641915);
    REQUIRE(graph.getLongitude(167) == -87.95317505301682);

    REQUIRE(graph.isConnected(167, 12));
    REQUIRE(graph.getDistance(167, 12) == 3.9);
    REQUIRE(graph.getAddress(12) == "50 W Dundee Road");

    REQUIRE(graph.isConnected(167, 166));
    REQUIRE(graph.getDistance(167, 166) == 5.8);
    REQUIRE(graph.getAddress(166) == "1530 W Algonquin Rd");

    REQUIRE(graph.isConnected(167, 157));
    REQUIRE(graph.getDistance(167, 157) == 5.4);
    REQUIRE(graph.getAddress(157) == "150 E. Dundee Road");
}
/* Template to test a node
    TEST_CASE("test node", "[weight=5][timeout=8000]") {
    TacoBellGraph graph("../data/final_data_dist.csv");
    REQUIRE(graph.getAddress() == "");
    REQUIRE(graph.getLatitude() == );
    REQUIRE(graph.getLongitude() == );

    REQUIRE(graph.isConnected(, ));
    REQUIRE(graph.getDistance(, ) == );
    REQUIRE(graph.getAddress() == "");

    REQUIRE(graph.isConnected(, ));
    REQUIRE(graph.getDistance(, ) == );
    REQUIRE(graph.getAddress() == "");

    REQUIRE(graph.isConnected(, ));
    REQUIRE(graph.getDistance(, ) == );
    REQUIRE(graph.getAddress() == "");
}
*/

TEST_CASE("test dijkstras search small", "[weight=5]") {
    vector<int> solution = {0, 3, 6, 5};
    TacoBellGraph graph;
    for (int i = 0; i < 7; i++) {
        graph.insertVertex(0, 0, to_string(i));
    }
    graph.insertEdge(0, 1, 2.7);
    graph.insertEdge(0, 2, 6);
    graph.insertEdge(0, 3, 2.3);

    graph.insertEdge(1, 0, 3);
    graph.insertEdge(1, 2, 3.8);
    graph.insertEdge(1, 3, 1.5);

    graph.insertEdge(2, 0, 5.3);
    graph.insertEdge(2, 1, 4);
    graph.insertEdge(2, 4, 4);

    graph.insertEdge(3, 0, 1.9);
    graph.insertEdge(3, 1, 2);
    graph.insertEdge(3, 6, 2.7);

    graph.insertEdge(4, 2, 3.7);
    graph.insertEdge(4, 5, 2.1);
    graph.insertEdge(4, 6, 6.7);

    graph.insertEdge(5, 0, 8.9);
    graph.insertEdge(5, 4, 2.3);
    graph.insertEdge(5, 6, 2.7);

    graph.insertEdge(6, 3, 3.6);
    graph.insertEdge(6, 4, 6.2);
    graph.insertEdge(6, 5, 3.2);

    REQUIRE(solution == graph.dijkstraSearch(0, 5));
    // Add more path checks
}

TEST_CASE("test dijkstras search 1", "[weight=5]") {
    REQUIRE(true);
}

TEST_CASE("test dijkstras search 2", "[weight=5]") {
    REQUIRE(true);
}

TEST_CASE("test BFS search 1", "[weight=5") {
    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> solution = {4, 137, 243, 278};

    vector<int> test = graph.BFS(4, 278);

    REQUIRE(test == solution);
}

TEST_CASE("test BFS search 2", "[weight=5") {
    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> solution = {151, 76, 261, 262, 12, 167};

    vector<int> test = graph.BFS(151, 167);

    REQUIRE(test == solution);
}

TEST_CASE("test BFS no results", "[weight=5]") {
    TacoBellGraph graph("../data/final_data_dist.csv");

    
}