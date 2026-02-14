# Task 4: Optimization Model (Linear Programming)

*Domain:* Operations Research  
*Technique:* Linear Programming  
*Library:* PuLP  

## Description
This project solves a resource allocation problem to *maximize business profit* using Python's PuLP library. The model determines the optimal production quantity of two products (A and B) while respecting constraints on labor hours and raw materials.

## Problem Statement
* *Goal:* Maximize Profit.
    * Product A Profit: $40
    * Product B Profit: $30
* *Constraints:*
    * *Labor Limit:* 100 Hours max (Product A: 2 hrs, Product B: 1 hr).
    * *Material Limit:* 80 Units max (Product A: 1 unit, Product B: 2 units).

## Results
The linear programming model successfully calculated the optimal number of units to produce to achieve the highest possible profit without exceeding resources.

## How to Run
1. Install the library: pip install pulp
2. Run the notebook: optimization_task.ipynb
