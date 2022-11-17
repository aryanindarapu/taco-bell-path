#include <iostream>
#include <string>

struct TacoBellNode {
    public:
        TacoBellNode(double latitude, double longitude, std::string address, int store_id) {
            longitude_ = longitude;
            latitude_ = latitude;
            address_ = address;
            store_id_ = store_id;
        }

        double longitude_;
        double latitude_;
        std::string address_;
        int store_id_;
};