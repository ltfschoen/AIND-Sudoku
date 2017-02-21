# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: *Student should provide answer here*

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We pass the given string representation of the Sudoku grid to a grid_values function,
which generates and returns a dictionary representation of the Sudoku grid, where
unsolved boxes are populated with local constraints in the form of a string of possible values
(i.e. '123456789') to be used instead of a full stop character (i.e. '.').
The list of different unit types are stored in a variable unitlist. Peers comprise of the unitlist
and we update it to include the new diagonal unit constraint along with row, column, and square units to solve
the diagonal Sudoku problem. We call a search function, passing the dictionary representation of the Sudoku
grid as a parameter. The search function uses recursion to perform Depth-First Search (DFS). It calls
a reduce_puzzle function passing the latest Sudoku grid, which repeatedly performs Constraint Propagation
techniques of the Elimination Strategy and Only Choice Strategy until solved or stalled by calling
eliminate() and only_choice() functions. The eliminate() function uses the Eliminate Strategy of iterating
over all the boxes in the puzzle and using the local constraints to find those that only have one
value assigned to them (i.e. no other possible values). It then removes this value from every one of
its peers (including the diagonal peer if relevant) before returning the updated Sudoku grid.
The only_choice() function iterates through all the square units, inspects the local constraints,
and whenever there is a unit with a box that contains an unsolved value that only fits in that one box,
it assigns the value to this box.
The search function chooses one of the unfilled boxes with the fewest possibilities
and uses recursion to create a copy of the Sudoku grid (with latest updates reducing the search space)
with one of the possible values at a time to be a new search tree branch trying and find a solution with it.
Each recursive iteration attempt that does not return False (stalled or box with no possibilities) or None will
return a modified copy with updated possibilities/values from the attempt.
When all boxes have a single value (only one possible value) then the problem is solved.

### Instructions and Setup Environment
* Switch to Miniconda env `source activate aind` (same steps as in https://github.com/ltfschoen/aind/blob/master/README.md)
* IntelliJ: File > Project Structure > Project Settings > Project > Project SDK > Python 3.6.0 (~/miniconda3/bin/python)
* Run Program and visualise using PyGame: `python solution.py`
* Run Tests: `python solution_test.py`

### Project Specification Checklist - Creating an AI Agent to solve Sudoku https://review.udacity.com/#!/rubrics/689/view

## CRITERIA / MEETS SPECIFICATIONS

* Functionality

[ ] - Naked twins implemented correctly / The student correctly uses constraint propagation to solve the
naked twins problem by enforcing the constraint that no squares outside the two naked twins squares can
contain the twin values http://www.sudokudragon.com/tutorialnakedtwins.htm

[X] - Diagonal Sudoku implemented correctly. / The student correctly solves the diagonal sudoku using
constraint propagation by adding the new constraint of the diagonal sudoku

[X] - Unit tests pass. / Diagonal unit tests pass. Run solution_test.py to check.

[ ] - Unit tests pass. / Naked Twins unit tests pass. Run solution_test.py to check.

* Documentation

[ ] - Comments / Student properly comments the functionality of the code.

* Conceptual

[ ] - Naked twins implementation understanding. / In the README.md file, the student has shown an
understanding of how constraint propagation has been used to implement the naked twins function,
by enforcing the constraint that no squares outside the two naked twins squares can contain the twin values

[X] - Diagonal Sudoku implementation understanding. / In the README.md file, the student has shown an
understanding of how constraint propagation has been used to solve the diagonal sudoku, by adding the
diagonals to the set of constraints.

* Bonus

[ ] - Personalised project by implementing other strategies from http://www.sudokudragon.com/sudokustrategy.htm

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.