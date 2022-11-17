#include <iostream>
#include <string>

class TacoBellNode {
    public:
        TacoBellNode(double latitude, double longitude, std::string address, int store_id);

        double longitude_;
        double latitude_;
        std::string address_;
        int store_id_;
};