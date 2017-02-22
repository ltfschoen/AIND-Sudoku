import logging

assignments = []

# Box - dictionary with keys for the strings in each box, an value
# for the digit (or '.' if not) in each box
rows = 'ABCDEFGHI'
cols = '123456789'

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def cross(a, b):
    """
    Input: Given two strings a and b, i.e. cross('abc', 'def')
    Returns: returns list formed by all possible concatentations
        of a letter s in string a, with a letter t in string b.
        (i.e. cross product of elements in a and elements in b)
        i.e. ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    """
    return [s+t for s in a for t in b]

# Box Labels

"""
Output:
    [
        'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
        'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
        'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
        'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
        'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9',
        'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
        'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9',
        'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9',
        'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'
     ]
"""
boxes = cross(rows, cols)

# Units

"""
Output:
    [
        ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'],
        ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'],
        ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
        ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'],
        ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'],
        ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'],
        ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'],
        ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'],
        ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
    ]

    Top row is:
        row_units[0] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
"""
row_units = [cross(r, cols) for r in rows]

"""
Output:
    Left-most column is:
        column_units[0] = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
"""
column_units = [cross(rows, c) for c in cols]

"""
Output:
    Top-left square is:
        square_units[0] = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
"""
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

# Diagonals Units

# Option 1: Using zip function
# diagonal_units1 = [a[0]+a[1] for a in zip(rows, cols)]
# diagonal_units2 = [a[0]+a[1] for a in zip(rows, cols[::-1])]

# Option 2: More easily understood
diagonal_units1 = [[rows[i]+cols[i] for i in range(9)]]
diagonal_units2 = [[rows[i]+cols[8-i] for i in range(9)]]

unitlist = row_units + column_units + square_units + diagonal_units1 + diagonal_units2
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def grid_values(grid):
    """
    Convert grid string of a Sudoku puzzle into a {<box>: <value>}
    dictionary representation with '123456789' value for empty values

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
        - i.e.
            {
              'A1': '123456789'
              'A2': '123456789',
              'A3': '3',
              'A4': '123456789',
              'A5': '2',
              ...
              'I9': '123456789'
            }
    """
    logging.info("Converting Sudoku puzzle to dictionary is processing")

    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81
    return dict(zip(boxes, values))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    logging.info("Converting Sudoku puzzle dictionary to 2D grid is processing")

    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """
    Input: Puzzle in dictionary form.
    Output: Iterate over all boxes in puzzle that only have one value assigned to them,
    remove this value from every one of its peers, and return puzzle in dictionary form
    """
    logging.info("Elimination Strategy is processing")

    update_dict = values
    for k, v in update_dict.items():
        if len(update_dict[k]) == 1:
            peer_keys = peers[k]
            digit = update_dict[k]
            for pk in peer_keys:
                # update_dict[pk] = update_dict[pk].replace(digit,'')
                # PyGame Attempt
                values = assign_value(values, pk, values[pk].replace(digit,''))

    return values

def only_choice(values):
    """
    Finalize all values that are the only choice for a unit.

    Go through all the units/squares, and whenever there is a unit with
    a box that contains an unsolved value that only fits in that one box,
    assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in Only Choices.
    """
    logging.info("Only Choice Strategy is processing")

    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box
                       for box in unit
                       if digit in values[box]]
            if len(dplaces) == 1:
                # values[dplaces[0]] = digit
                # PyGame Attempt
                values = assign_value(values, dplaces[0], digit)
    return values


def naked_twins(values):
    """
    Eliminate values using the naked twins strategy. Find all instances of naked twins by:
    - Find all boxes with exactly two possibilities by iterating over all boxes in puzzle.
    - Storing in a list of tuples all pairs of boxes that each contain the same twin possibilities (naked twins)
    - Iterate over all the pairs of naked twins to:
        - Find peer boxes that they have in common between them based on calculating their intersection
        - With the set of intersecting peers determined, iterate over the set of intersecting peers and
        delete the naked twins values from each of those intersecting peers that contain more than two possible values

    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    logging.info("Naked Twins Strategy processing")

    # Find all boxes containing exactly two possibilities
    possible_twins = [box
                      for box in values.keys()
                      if len(values[box]) == 2]
    # print("Possible naked twins: ", possible_twins)

    # Store in list of tuples all pairs of boxes that each contain the same twin possibilities (naked twins)
    naked_twins = []
    for box_twin1 in possible_twins:
        for box_twin2 in peers[box_twin1]:
            if values[box_twin1] == values[box_twin2]:
                naked_twins.append((box_twin1, box_twin2))
    # print("Naked twins: ", naked_twins)

    # Iterate over all the pairs of naked twins.
    #   - Find peer boxes that they have in common between them based on calculating their intersection
    #   - Iterate over the set of intersecting peers
    #   - Delete the naked twins values from each of those intersecting peers that contain over two possible values
    for index in range(len(naked_twins)):
        box1, box2 = naked_twins[index][0], naked_twins[index][1]
        peers1, peers2 = peers[box1], peers[box2]
        peers_intersection = set(peers1).intersection(peers2)
        for peer_box in peers_intersection:
            if len(values[peer_box]) > 2:
                for digit in values[box1]:
                    # values[peer_box] = values[peer_box].replace(digit, '')
                    # PyGame Attempt
                    values = assign_value(values, peer_box, values[peer_box].replace(digit,''))
    # print("After naked twin: ", values)
    return values

def reduce_puzzle(values):
    """
    Constraint Propagation and Only Choice Techniques applied.
    Input: Unsolved Sudoku puzzle as dict
    Process: Apply repeatedly the eliminate() and only_choice() functions
    as constraints. Stop and return puzzle when solved. Exit loop by returning
    False when stuck at box with no available values. If Sudoku puzzle unchanged
    after iterating both eliminate() and only_choice() functions then return the Sudoku
    Output: Solution to Sudoku puzzle as dict
    """
    stalled = False
    while not stalled:
        logging.warning("Constraint Propagation - Strategies narrowing search space")

        # Check how many boxes have a determined value
        solved_values_before = len([box
                                    for box in values.keys()
                                    if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Naked Twins Strategy
        values = naked_twins(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box
                                   for box in values.keys()
                                   if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box
                for box in values.keys()
                if len(values[box]) == 0]):

            logging.error("Constraint Propagation - Found box with missing values")

            return False

    logging.warning("Constraint Propagation - Stalled")

    return values

def search(values):
    """
    Use Depth-First Search (DFS) and Constraint Propagation,
    create a search tree and solve the Sudoku.
    """

    logging.info("Depth-First Search Algorithm processing")

    # First, reduce the puzzle with using the reduce_puzzle function
    values = reduce_puzzle(values)
    if values is False:
        logging.error("Depth-First Search Algorithm - Found box with missing values")

        return False # Failed
    if all(len(values[s]) == 1 for s in boxes):
        logging.info("Depth-First Search Algorithm - Solution found")

        return values # Solved!

    # Choose one of the unfilled squares with the fewest possibilities
    # and extract the n,s (i.e. 2 possibilities at 'A' would return: 2, 'A')
    n,s = min((len(values[s]), s)
              for s in boxes
              if len(values[s]) > 1)

    # Now use recursion to solve each one of the resulting Sudokus,
    # and if one returns a value (not False), return that answer!
    # i.e. loop for 8 and 9 when possibilities for a box is 89
    for value in values[s]:

        logging.info("Depth-First Search Algorithm - Generating recursive tree branch attempt")

        new_sudoku = values.copy() # copy of latest Sudoku puzzle with updates from calling reduce_puzzle function
        new_sudoku[s] = value # modify copy (new search tree branch) with attempt at trying reduced possibility of 8
        attempt = search(new_sudoku) # recursion using modified copy with new tree branch attempt
        if attempt: # if does not return False or None from modified copy it returns the values from the attempt

            logging.info("Depth-First Search Algorithm - Attempt success")

            return attempt
        else:
            logging.info("Depth-First Search Algorithm - Attempt failure")

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    logging.info("Loading grid")
    logging.info("Loading Sudoku puzzle string representation is processing")

    # Get Sudoku grid representation with unsolved boxes populated with possible values
    values = grid_values(grid)
    # display(values)
    # Call recursive function that performs Depth First Search using Constraint Propagation techniques
    # of Elimination and Only Choice to solve harder Sudoku problems including those using diagonals as peers
    values = search(values)

    logging.info("Depth-First Search Algorithm - Finished")

    logging.debug("Values after search 1: ", values)

    if not isinstance(values, bool):
        return values

def run():
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    # naked_twins_grid1 = '84.632.....34798257..518.6...6.97..24.8256..12..84.6...8..65..3.54.2.7.8...784.96'
    # naked_twins_grid2 = '1.4.9..68956.18.34..84.695151.....868..6...1264..8..97781923645495.6.823.6.854179' # from test1
    grid = diag_sudoku_grid

    values = solve(grid)

    logging.debug("Values after solve 2: ", values)

    logging.info("Sudoku values returned after search")

    if values:
        display(solve(grid))

    try:
        from visualize import visualize_assignments

        logging.info("PyGame using visualize being called")

        visualize_assignments(assignments)

    except SystemExit:
        logging.exception('SystemExit occurred')
    except:
        logging.exception('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')


if __name__ == '__main__':
    run()