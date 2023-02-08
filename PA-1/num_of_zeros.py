def num_of_zeros(grid: list) -> int:
    """
    Given a 2D grid of 0s and 1s sorted in descending order, this function
    counts and returns the number of zeros in the input. This program takes in
    a list type as an input, and returns an integer type. I initially thought of
    using nested loops, but wanted to take a different approach to solve the
    problem. Instead, I wanted to iterate through the grid from the top right
    and check each row for 0s and move to the next row, and keep iterating until
    it finishes through the last row.
    """
    # Initialize count.
    count = 0
    # Initialize row and column values.
    i, j = 0, len(grid[0]) - 1
    # Begin iteration through outer grid.
    while i < len(grid):
        # Iterate from the top right corner backwards, checking if each element
        # within each nested list is 0.
        if grid[i][j] == 0:
            # If found, the row that is iterated upon is decreased by one and
            # the count value is increased by 1.
            j -= 1
            count += 1
            # If all list values including the left-most element are 0, still
            # increment the count by 1.
            if j == 0:
                # Increments the column iterated upon by 1.
                if grid[i][j] == 0:
                    i += 1
                    count += 1
                    # Reset the column count.
                    j = len(grid[0]) - 1
        # If element equals 1, then reset and move down to the next row.
        elif grid[i][j] == 1:
            j = len(grid[0]) - 1
            i += 1
    return count