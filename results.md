# Written Report
## Data Processing
To get a hold of our data, we had to parse through html of the website for every Taco Bell location in Illinois. From each of these websites, we parsed the address, and latitude and longitude data. Furthermore, the three nearest locations were also hyperlinked on the current location website, so we were able to parse through those websites to extract the latitude and longitude of those locations as well. For this, we used the BeautifulSoup and json python libraries. The accuracy of this was tested and confirmed throughout the development of this project. We knew we had the accurate data when there were the same number of rows as there are Taco Bells in Illinois, and the program outputted no more than 3 nearest locations. The locations outside of Illinois were then deleted from the csv file using the Google Maps API.

## Breadth First Search
This algorithm searches through the graph to find a specific node, and on average runs in O(V + E), where V are the number of vertices and E are the number of edges. In order to find a specific node, there is a visited array that keeps track of which node has been visited. Then, the algorithm starts at the start node, marks it as visited, and then adds each of its neighbors to the priority queue. That process is then repeated on the top vertex of the queue and popped after processing until the queue is empty. Our BFS algorithm was tested similar to our Dijkstra's search algorithm. Our BFS search returns a vector of the nodes visited before we get to the destination node. We returned BFS vectors on a small graph and the real graph and compared them to solution vectors that we manually created.

## Dijkstra's search algorithm
This algorithm returns the shortest path between two different paramatarized nodes. In our case, these two nodes were the locations of two different Taco Bell locations. Using an adjacency list, this algorithm on average runs in O(V2), where V is the number of vertices. Starting from the first paramatarized node, this search algorithm adds neighboring nodes to a priority queue in order of shortest to greatest distance between the current and neighboring nodes. As each node is visited, it is marked as visited so that it is not processed twice. After all the neighboring nodes have been processed, each node is updated with its new shortest path length value, and the process is repeated until the destination node is reached. Our tests consisted of first testing the algorithm on a small graph, which consisted of 21 edges, and then testing on the final data itself, with different start and destination points, not just Champaign and Chicago. The output of the search algorithm is a vector of nodes which are travelled through, so we created a vector that contains the correct nodes and tested our output against that solution vector. We also tested a search that should return no solution, which worked as intended.

## Betweenness Centrality
Betweenness centrality represents how central a certain node is in a graph, i.e. how many times a node is present in all of the shortest paths of each pair of nodes. It is better represented by the following sum
 
![Betweenness Centrality Formula](./formula.png)


where σst(v)  is the the total number of shortest paths from node s to node v and σst is the number of those paths that pass through v (not where v is an endpoint).The algorithm used to calculate the betweenness centrality is Brandes’ Algorithms, which has an worst case runtime of O(|V|^2 log|V| + |V||E|), where V is the number of vertices and E is the number of edges. To test to make sure that the algorithm was working, a smaller graph, with about 10 nodes, was created. The betweenness centrality was calculated for each node manually, and the output was then checked.

## Leading Question
What is the shortest path of Taco Bell stops from Champaign to Chicago? We answered this question by creating a graph, where nodes are individual Taco Bell locations and the edges are the distance between each location. Using this graph, we were able to use Dijkastra’s search algorithm to search for the shortest path of Taco Bells from Champaign to Chicago. We discovered that there are 16 Taco Bells that we could pass through on our way to Chicago. 

1) 512 E. Green Street
2) 1707 S. Neil Street
3) 582 Main NW
4) 195 South Creek Drive
5) 5737 W. Monee Manhattan Road
6) 413 Sauk Trail
7) 201 S Halstead St.
8) 2945 West 159th Street
9) 12716 Ashland Ave.
10) 1644 W 95th St
11) 7906 S. Western Avenue
12) 5350 S Pulaski
13) 4614 S Damen Ave
14) 255 W Garfield Blvd
15) 3365 S Martin Luther King Drive
16) 407 S. Dearborn

Additionally, we also found that the path through Taco Bells was 27.3 miles longer than the direct path.

## General Thoughts
Our biggest success was our ability to split up tasks between people. There were very little issues when it came to people doing what they were assigned to do, and everyone successfully completed their tasks. I think we could’ve done a better job initially communicating ideas with each other. Towards the end, a couple of us were wanting to add functionality to the program, but ideally, that should’ve been discussed sooner in the process rather than later.
