# Challenge Title:  business trip

### Given a business trip itinerary, and an Alaska Airlines route map, is the trip possible with direct flights? If so, how much will the total trip cost be?

## Write a function called **business trip**
- Arguments: graph, array of city names
- Return: the cost of the trip (if it’s possible) or null (if not)
- Determine whether the trip is possible with direct flights, and how much it would cost.

## Whiteboard Process
![Whiteboard-CC36](./Whiteboard-CC37.PNG)

## Approach & Efficiency

Approach:

        1. Initialize the total_cost variable to 0.

        2. Iterate over the cities list, considering pairs of consecutive cities (city1 (cities[i]) and city2(cities[i + 1])).

        3. For each pair, check if there is a direct path from city1 to city2 in the graph.

        4. If there is no direct path, return None as it is impossible to complete the trip.

        5. Otherwise, add the weight of the edge (path) between city1 and city2 to the total_cost.

        6. After iterating through all city pairs, return the total_cost.


Efficiency:

        The time complexity of the function is O(N)bec the function iterates over the cities list once, and the loop runs (len(cities) - 1) times.

        The space complexity of the function is determined by the additional memory used, the function uses a constant amount of additional memory. 

        `Time Complexity`: O(n) (where n is the number of cities in the cities list).
        `Space Complexity`: O(1) (constant memory usage).


## Solution
- **_[The Code Link](./graph/graphbusinesstrip.py)_**

- **_[The Test Code Link](./tests/test_graph.py)_**

- **To run the code :**

        python3 -m venv .venv

        source .venv/bin/activate
    
- **To run the Test:**

        pytest

