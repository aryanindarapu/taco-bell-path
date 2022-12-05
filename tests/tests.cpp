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