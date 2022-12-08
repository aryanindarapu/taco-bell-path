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


TEST_CASE("Test Graph Size", "[weight=5") {
    std::cout << "Testing Graph Size" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");
    REQUIRE(graph.size() == 285);
}

TEST_CASE("Test Graph 1", "[weight=5][timeout=8000]") {
    std::cout << "Testing Graph 1" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");
    REQUIRE(graph.getAddress(0) == "555 W. Lake St.");
    REQUIRE(graph.getLatitude(0) == 41.93787872988780);
    REQUIRE(graph.getLongitude(0) == -88.00291031599050);

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

TEST_CASE("Test Graph 2", "[weight=5][timeout=8000]") {
    std::cout << "Testing Graph 2" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");
    REQUIRE(graph.getAddress(167) == "2410 E Rand Rd");
    REQUIRE(graph.getLatitude(167) == 42.094717788641900);
    REQUIRE(graph.getLongitude(167) == -87.95317505301680);

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

TEST_CASE("Test Dijkstra's Search - Small", "[weight=5]") {
    std::cout << "Testing Dijkstra's Search - Small" << std::endl;
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

TEST_CASE("Test Dijkstra's Search 1", "[weight=5]") {
    std::cout << "Testing Dijkstra's Search 1" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> solution = {10, 238, 54, 156};
    vector<int> test = graph.dijkstraSearch(10, 156);

    REQUIRE(test == solution);
}

TEST_CASE("Test Dijkstra's Search 2", "[weight=5]") {
    std::cout << "Testing Dijkstra's Search 2" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> solution = {229, 137, 4, 242, 239, 238, 54, 147};
    vector<int> test = graph.dijkstraSearch(229, 147);
    
    REQUIRE(test == solution);
}

TEST_CASE("Test Dijkstra's Search no results", "[weight=5]") {
    std::cout << "Testing Dijkstra's Search No Results" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> solution = {};
    vector<int> test = graph.dijkstraSearch(2, 13);
    
    REQUIRE(test == solution);
}

TEST_CASE("Test BFS Search 1", "[weight=5") {
    std::cout << "Testing BFS Search 1" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> solution = {4, 137, 243, 278};

    vector<int> test = graph.BFS(4, 278);

    REQUIRE(test == solution);
}

TEST_CASE("Test BFS Search 2", "[weight=5") {
    std::cout << "Testing BFS Search 2" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> solution = {151, 76, 261, 262, 12, 167};

    vector<int> test = graph.BFS(151, 167);

    REQUIRE(test == solution);
}

TEST_CASE("Test BFS No Results", "[weight=5]") {
    std::cout << "Testing BFS Search No Results" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> solution = {};

    vector<int> test = graph.BFS(1, 13);

    REQUIRE(test == solution);
}

TEST_CASE("Test Betweenness Centrality - Champaign", "[weight=5]") {
    std::cout << "Testing Betweenness Centrality - Champaign" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");
    int solution = graph.betweennessCentrality(186);
    REQUIRE(80 == solution);
}

TEST_CASE("Test Betweenness Centrality - Chicago", "[weight=5]") {
    std::cout << "Testing Betweenness Centrality - Chicago" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");
    int solution = graph.betweennessCentrality(207);
    REQUIRE(377 == solution);
}

/**
 * @brief This test case is just so you can see the final result of our graph.
 * 
 * If all other test cases pass, this should be the final representation of our path
 * 
 */
TEST_CASE("Printing out Champaign to Chicago", "[weight=5]") {
    std::cout << "\nOutputting Taco Bells From Champaign to Chicago" << std::endl;
    TacoBellGraph graph("../data/final_data_dist.csv");
    graph.champaignToChicago();
    REQUIRE(true);
}