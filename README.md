# The Path of Taco Bells
## Leading Question 
Taco Bell is my absolute, most favorite place to eat food. But when driving from Champaign to Chicago, I'm not sure when or where to stop to get my tasty treat. This project aims to answer the question, "What is the shortest path of Taco Bell stops from Champaign to Chicago?".

## Project Submission
We have several files located in our repository to submit for our project. 
### Dataset
- The dataset and dataset code is located in the `data` folder
- The web data scraping from Taco Bell's website is stored in `data.py` and `functions.py`. Running `data.py` will create a CSV file with the latitude and longitude values of the current locations and the three nearest locations.
- The data cleaning and Google Maps API functions are stored `refactor_csv.py`. This file cleans the null values and calculate the distance between two locations. The output CSV file is named `final_data_dist.csv`.

### Technical Portion
- The data test suite is located in the `mid_project_check` folder, under `test_suite.py`
- The graph test suite is located in the `test` folder, under `tests.cpp`
- Our code, which includes our graph building and storage, BFS, Dijkstra's, and Betwenness Centrality is located in the `src` folder

### Non-Technical Portion
- All of the "non-technical" portions of the submission are contained within the main directory of the repository. This includes the README, written report, and presentation.


## The Executable
### Running the Executable
First, run the following commands from the main directory of the repository

    $ mkdir build
    $ cd build
    $ cmake ..

To run the main executable, run

    $ make
    $ ./main

As seen above, the main script (and the test script) take no arguments, and the output is solely in the console.

## The Test Suite
### Running the Data Test Suite
To run the test suite for the data scraping, `test_suite.py` must be run. However, `Python 3` must be installed, along with the `numpy`, `googlemaps`, and `pandas` libraries. Finally, `YOUR_KEY_HERE` from line 8 (show below)

    client = googlemaps.Client("YOUR_KEY_HERE")

must be replaced with a Google Maps API key with the Distance Matrix API enabled.

### Running the Graph Test Suite
The graph test suite, and the code, must be run on the CS 225 EWS. To run the test suite, first follow the instructions for running the executable. Then run the following commsands from the `build` directory of the repository

    $ make test
    $ ./test

### The Graph Test Suite
The test suite contains a variety of tests on all of the algorithms and the graph itself. It goes through the following tests, in order:

1. Checking whether the Taco Bell graph was build correctly
2. A small graph Dijkstra's test
3. Dijkstra's on the Taco Bell graph
4. BFS on the Taco Bell graph
5. Betweenness Centrality for the Champaign and Chicago locations
6. Returns Taco Bell locations from Champaign to Chicago

