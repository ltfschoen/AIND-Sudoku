# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: We pass the given string representation of the Sudoku grid to a grid_values function,
which generates and returns a dictionary representation of the Sudoku grid, where
unsolved boxes are populated with local constraints in the form of a string of possible values
(i.e. '123456789') to be used instead of a full stop character (i.e. '.').
The list of different unit types are stored in a variable unitlist. Peers of the unitlist
include the row, column, square, and diagonal units constraints to that are used to solve
the diagonal Sudoku problem. We call a search function, passing the dictionary representation of the Sudoku
grid as a parameter. The search function uses recursion to perform Depth-First Search (DFS). It calls
a reduce_puzzle function passing the latest Sudoku grid, which repeatedly performs Constraint Propagation
techniques of the Elimination Strategy, Naked Twins Strategy, and Only Choice Strategy until solved or stalled by calling
eliminate(), naked_twins(), and only_choice() functions that each return an updated Suduko grid that may narrow the search space.
We use constraint propagation to solve problems with naked twins
by explicitly calling the naked_twin() function, which enforces the constraints.
The eliminate() function uses the Eliminate Strategy of iterating
over all the boxes in the puzzle and using the local constraints to find those that only have one
value assigned to them (i.e. no other possible values). It then removes this value from every one of
its peers (including the diagonal peer if relevant) before returning the updated Sudoku grid that may narrow the search space.
The naked_twins() function uses the Naked Twins Strategy of enforcing the constraint that no peer boxes
that are shared between the pair of naked twins may contain their twin values. The point of using the Naked Twins
Constraint Propagation Strategy (as with the other strategies) is to try and narrow the search space so that
the DFS incrementally runs faster. It involves finding all instances of naked twins by first finding all boxes with
exactly two possibilities by iterating over all boxes in puzzle. We then store in a list of tuples all pairs of boxes
that each contain the same twin possibilities (naked twins). Lastly we iterate over all the pairs of naked twins to
find peer boxes that they have in common between them based on calculating their intersection, and then with the set of
intersecting peers determined, we iterate over the set of intersecting peers and delete the naked twins values from each
of those intersecting peers that contain more than two possible values. It may return an updated Sudoku grid that narrows the search space.
The only_choice() function iterates through all the square units, inspects the local constraints,
and whenever there is a unit with a box that contains an unsolved value that only fits in that one box,
it assigns the value to this box. It may return an updated Sudoku grid that narrows the search space.
The search function chooses one of the unfilled boxes with the fewest possibilities
and uses recursion to create a copy of the Sudoku grid (with latest updates reducing the search space)
with one of the possible values at a time to be a new search tree branch trying and find a solution with it.
Each recursive iteration attempt that does not return False (stalled or box with no possibilities) or None will
return a modified copy with updated possibilities/values from the attempt.
When all boxes have a single value (only one possible value) then the problem is solved.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We pass the given string representation of the Sudoku grid to a grid_values function,
which generates and returns a dictionary representation of the Sudoku grid, where
unsolved boxes are populated with local constraints in the form of a string of possible values
(i.e. '123456789') to be used instead of a full stop character (i.e. '.').
The list of different unit types are stored in a variable unitlist. Peers comprise of the unitlist
and we update it to also enforce the new diagonal unit constraint (whereby the goal is for boxes along the diagonal
from A1 to I9 to each only contain a unique value between 1 and 9, and the same constraint applies
along the diagonal from I1 to A9, noting that a further constraint applies in that the E5 box at the
intersection of the two diagonals must be the same value for both diagonals) along with row, column, and square units to solve
the diagonal Sudoku problem. We call a search function, passing the dictionary representation of the Sudoku
grid as a parameter. The search function uses recursion to perform Depth-First Search (DFS). It calls
a reduce_puzzle function passing the latest Sudoku grid, which repeatedly performs Constraint Propagation
techniques of the Elimination Strategy and Only Choice Strategy until solved or stalled by calling
eliminate() and only_choice() functions that each return an updated Suduko grid that may narrow the search space.
The eliminate() function uses the Eliminate Strategy of iterating
over all the boxes in the puzzle and using the local constraints to find those that only have one
value assigned to them (i.e. no other possible values). It then removes this value from every one of
its peers (including the diagonal peer if relevant) before returning the updated Sudoku grid that may narrow the search space.
The only_choice() function iterates through all the square units, inspects the local constraints,
and whenever there is a unit with a box that contains an unsolved value that only fits in that one box,
it assigns the value to this box. It may return an updated Sudoku grid that narrows the search space.
The search function chooses one of the unfilled boxes with the fewest possibilities
and uses recursion to create a copy of the Sudoku grid (with latest updates reducing the search space)
with one of the possible values at a time to be a new search tree branch trying and find a solution with it.
Each recursive iteration attempt that does not return False (stalled or box with no possibilities) or None will
return a modified copy with updated possibilities/values from the attempt.
When all boxes have a single value (only one possible value) then the problem is solved.

### Instructions and Setup Environment
* Switch to Miniconda env `source activate aind` (same steps as in https://github.com/ltfschoen/aind/blob/master/README.md)
* IntelliJ: File > Project Structure > Project Settings > Project > Project SDK > Python 3.6.0 (~/miniconda3/bin/python)
* Run Program and visualise using PyGame: `python main.py --log=DEBUG`
* Run Tests: `python solution_test.py`

### Project Specification Checklist - Creating an AI Agent to solve Sudoku https://review.udacity.com/#!/rubrics/689/view

## CRITERIA / MEETS SPECIFICATIONS

* Functionality

[X] - Naked twins implemented correctly / The student correctly uses constraint propagation to solve the
naked twins problem by enforcing the constraint that no squares outside the two naked twins squares can
contain the twin values http://www.sudokudragon.com/tutorialnakedtwins.htm

[X] - Diagonal Sudoku implemented correctly. / The student correctly solves the diagonal sudoku using
constraint propagation by adding the new constraint of the diagonal sudoku

[X] - Unit tests pass. / Diagonal unit tests pass. Run solution_test.py to check.

[X] - Unit tests pass. / Naked Twins unit tests pass. Run solution_test.py to check.

* Documentation

[X] - Comments / Student properly comments the functionality of the code.

* Conceptual

[X] - Naked twins implementation understanding. / In the README.md file, the student has shown an
understanding of how constraint propagation has been used to implement the naked twins function,
by enforcing the constraint that no squares outside the two naked twins squares can contain the twin values

[X] - Diagonal Sudoku implementation understanding. / In the README.md file, the student has shown an
understanding of how constraint propagation has been used to solve the diagonal sudoku, by adding the
diagonals to the set of constraints.

* Bonus

[ ] - Personalised project by implementing other strategies from http://www.sudokudragon.com/sudokustrategy.htm

[ ] - Added 

[X] - PyGame Visualisation of the project

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