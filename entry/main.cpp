#include "TacoBellGraph.h"

using namespace std;

int main() {

    TacoBellGraph graph("../data/final_data_dist.csv");

    // std::cout << "Welcome to Find Taco Bell Path\n" << std::endl;
    // std::vector<int> temp = graph.BFS(186, 207);
    // std::cout << temp.size() << std::endl;
    // for (unsigned long i = 0; i < temp.size(); i++) {
    //     std::cout << temp[i] << std::endl;
    // }

    // //std::cout << graph.betweennessCentrality(207) << std::endl;
    
    // std::string address1;
    // std::string address2;

    // std::cout << "Type an origin TacoBell address: ";
    // std::getline(std::cin, address1);

    // std::cout << "Type a destination TacoBell address: ";
    // std::getline(std::cin, address2);


    // vector<int> store_ids = graph.findTacoBellPath(address1, address2);

    // double distance = 0.0;
    // std::cout << "\nStart: " << graph.getAddress(store_ids[0]) << " ----- Distance: " << distance << " miles" << std::endl;

    // for (size_t i = 1; i < store_ids.size(); i++) {
    //     if (i == store_ids.size() - 1) std::cout << "End: ";
    //     distance += graph.getDistance(store_ids[i - 1], store_ids[i]);
    //     std::cout << graph.getAddress(store_ids[i]) << " ----- Distance: " << distance << " miles" << std::endl;
    // }

    // std::cout << '\n';

    graph.champaignToChicago();

    return 0;
}
