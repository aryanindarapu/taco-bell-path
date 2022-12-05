#include "TacoBellGraph.h"

using namespace std;

int main() {

    TacoBellGraph graph("../data/final_data_dist.csv");

    vector<int> test = graph.dijkstraSearch(105, 163);
    
    for (int t : test) {
        cout << t << " " << endl;
    }

    return 0;
}