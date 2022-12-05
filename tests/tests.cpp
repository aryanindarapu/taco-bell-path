#include <catch2/catch_test_macros.hpp>

#include "TacoBellGraph.h"


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

TEST_CASE("test graph", "[weight=5][timeout=8000]") {
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
/*
TEST_CASE("test dijkstras search", "[weight=5]") {
    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> solution = {105, 283, 284, 163};

    vector<int> test = graph.dijkstraSearch(105, 163);

    for (size_t i = 0; i < solution.size(); i++) {
        // REQUIRE(test[i] == solution[i]);
    }
}
*/

TEST_CASE("test BFS search 1", "[weight=5") {
    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> solution = {21, 143, 89, 131, 45};
    vector<int> test = graph.BFS(21, 45);

    cout << "test BFS search" << endl;
    cout << "solution: " << vectorToString(solution) << endl;
    cout << "test: " << vectorToString(test) << endl;
    
    // for (size_t i = 0; i < solution.size(); i++) {
    //     REQUIRE(test[i] == solution[i]);
    // }

    REQUIRE(solution == test);
}

TEST_CASE("test BFS search 2", "[weight=5") {
    
}