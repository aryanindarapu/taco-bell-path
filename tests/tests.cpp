#include <catch2/catch_test_macros.hpp>

#include "TacoBellGraph.h"

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

TEST_CASE("test dijkstras search", "[weight=5]") {
    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> solution = {105, 283, 284, 163};

    vector<int> test = graph.dijkstraSearch(105, 163);

    for (size_t i = 0; i < solution.size(); i++) {
        REQUIRE(test[i] == solution[i]);
    }
}