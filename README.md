# The Best Taco Bell Path in Illinois
## Leading Question 
Taco Bell is my absolute, most favorite place to eat food. But when driving from Champaign to Chicago, I'm not sure when or where to stop to get my tasty treat. This project aims to answer the question, based on a "hungriness level" (the number of Taco Bell's you want to stop at), "What is the shortest path of Taco Bell stops from Champaign to Chicago based on my hungriness?".

## Dataset Acquisition
The data will be web scraped from Taco Bell's website, which lists all of the Illinois Taco Bell locations. Additionally, we will incorporate Google Maps data of whether a certain location is open or not.

## Data Format
This web scrape and the Google Maps API data will be compiled into a CSV file. The dataset will be a couple of hundred rows large with 5 columns: location name, address, longitude, latitude, and whether the location is open. For the graph, we will use the longitude, latitude, and whether the location is open. The other two columns will solely serve the purpose to help the user.

## Data Correction
We will web scrape the data using Python's Webdriver and Selenium and parse through it using the Pandas library. Since the dataset is not too large, we will manually go through the CSV file to make sure there are no inconsistencies. To get the longitude and latitude, we will use the Google Maps API to extract it from the scraped address.

## Data Storage
We will store the data as a graph. Each node will represent a location of a Taco Bell in Illinois, with its associated longitude, latitude, and open values. A node will have an edge to the five nearest nodes, based on longitude and latitude. Each edge will have a weight of its priority distance, i.e. the farthest node with an edge will have a weight 5, whereas the closest node with an edge will have a weight 1. This will be stored as O(n).

    NOTE: If we deem necessary, we may use a kd-Tree to initially put all the points into order, and then build the graph. This will be stored as O(n).

## Algorithm 
Our function will have 5 inputs: the start longitude, the start latitude, the destination longitude, the destination latitude, and the hungriness level. The start and destination locations will be bounded by a location within Illinois, and the hungriness level, which indicates the number of Taco Bell stops within the destination, will be maxed at 10. The dataset would need to be converted to (possibly a kd-Tree) a graph, as described in the Data Storage section above.

The expected output will be a list of Taco Bell locations, in the order of the visited Taco Bell locations. The output will simply be printed to the console.

We will use Dijkastra's Algorithm with a weight penalty (to get a minimum number of nodes) to get the shortest route with the desired number of Taco Bells. The time complexity will be O(n^2) and it will be stored with O(n). Additionally, we will implement BFS and DFS to get the closes Taco Bells to a location, which will be O(n+m) time complexity and O(n) storage. We will also measure the betweeness centrality to figure out what the most central Taco Bells can be.

## Timeline
Week of 11/7 - Web scrape and parse data, work with mentor to clean up proposal, start building Dijkastra's Algorithm (basic)

Week of 11/14 - Finish Dijkastra's, start reading CSV file and putting into graph format

Week of 11/27 - Betweeness Centrality, Build BFS and DFS algorithms 

Week of 11/28 - Finish BFS and DFS Algorithms

Week of 12/5 - Finish any other issues/conflicts that arise
