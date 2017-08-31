import itertools as it
import enum


class Direction(enum.Enum):
    UP    = (0, -1)
    DOWN  = (0,  1)
    RIGHT = (1,  0)
    LEFT  = (-1, 0)


class Mark(enum.Enum):
    UNMARKED      = 0
    MARKED        = 1
    BACKTRACKED   = 2
    UNTRAVERSABLE = 3


class Maze():
    __NEXT_MARKER = {
        Mark.UNMARKED: Mark.MARKED,
        Mark.MARKED: Mark.BACKTRACKED,
        Mark.BACKTRACKED: Mark.BACKTRACKED,
        Mark.UNTRAVERSABLE: Mark.UNTRAVERSABLE
    }

    __MARKER_CHARS = {
        Mark.UNMARKED:      '0',
        Mark.MARKED:        '1',
        Mark.BACKTRACKED:   '2',
        Mark.UNTRAVERSABLE: '-',
    }

    def __init__(self, maze):
        if maze == [] or maze[0] == []:
            self.__cols = 0
            self.__rows = 0
            self.markers = []
        else:
            self.__cols = len(maze[0])
            self.__rows = len(maze)
            self.markers = init_array(Mark.UNMARKED, self.__cols + 2, self.__rows + 2)
            border_array(self.markers, Mark.UNTRAVERSABLE, self.__cols + 2, self.__rows + 2)

        for col in range(self.__cols): 
            for row in range(self.__rows):
                if maze[col][row] is True:
                    self.markers[col + 1][row + 1] = Mark.UNMARKED
                else:
                    self.markers[col + 1][row + 1] = Mark.UNTRAVERSABLE

    @staticmethod
    def init_array(initial_value, cols, rows):
        """
        Initialize a new array with an initial value.
        """
        if cols == 0 or rows == 0:
            return []

        array = [[initial_value for i in range(rows)]]
        for _ in range(cols-1):
            array.append(array[0][:])

        return array

    @staticmethod
    def border_array(array, sentinel, cols, rows):
        """
        Place a sentinel-valued border around the maze.
        """
        for col in range(cols):
            array[col][0] = array[col][rows - 1] = sentinel
        
        for row in range(rows):
            array[0][row] = array[cols - 1][row] = sentinel

    def __contains__(self, index):
        col, row = index[0], index[1]
        return (col >= 0) and (col < self.__cols) \
           and (row >= 0) and (row < self.__rows)

    def mark(self, col, row):
        """
        We traverse the marker map in column-major order; the ``col``
        represents the x-coordinate, whereas the ``row`` represents 
        the y-coordinate.
        """
        if (col, row) in self:
            self.markers[col + 1][row + 1] = \
                self.__NEXT_MARKER[self.markers[col + 1][row + 1]]

    def peek(self, col, row, direction):
        d_col, d_row = direction.value
        new_col = col + d_col
        new_row = row + d_row
        if ((new_col, new_row) in self) and (self.is_traversable(new_col, new_row)):    
            return self.markers[new_col + 1][new_row + 1]
        else: 
            return None

    def is_traversable(self, col, row):
        """
        Determine whether a tile in the maze is traversable.
        """
        if (col, row) in self:
            return self.markers[col + 1][row + 1] != Mark.UNTRAVERSABLE
        else:
            return False

    def is_passage(self, col, row):
        """
        Determine whether a tile in the maze is in a passage tile.
        """
        if (col, row) in self:
            # Can we move left or right?
            if (self.markers[(col + 1) -1][row + 1] != Mark.UNTRAVERSABLE)\
                or (self.markers[(col + 1) + 1][row + 1] != Mark.UNTRAVERSABLE):
                
                # We can move left or right.
                # If we cannot move up or down, we are in a passage tile.
                return (self.markers[col + 1][(row + 1) - 1] == Mark.UNTRAVERSABLE)\
                    and (self.markers[col + 1][(row + 1) + 1] == Mark.UNTRAVERSABLE)
            else:
                # We cannot move left or right.
                # This leaves only the possibility of moving up or down.
                return (self.markers[col + 1][(row + 1) - 1] != Mark.UNTRAVERSABLE)\
                    or (self.markers[col + 1][(row + 1) + 1] != Mark.UNTRAVERSABLE)
        else:
            return False

    def is_junction(self, col, row):
        """
        Determine whether a tile in the maze is at a junction.
        """
        if (col, row) in self:
            # Can we move left or right?
            if (self.markers[(col + 1) - 1][row + 1] != Mark.UNTRAVERSABLE)\
                or (self.markers[(col + 1) + 1][row + 1] != Mark.UNTRAVERSABLE):
                
                # We can move left or right.
                # If we can move up or down, we are at a junction.
                return (self.markers[col + 1][(row + 1) - 1] != Mark.UNTRAVERSABLE)\
                    or (self.markers[col + 1][(row + 1) + 1] != Mark.UNTRAVERSABLE)
            else:   
                # We cannot move left or right. Being at a junction tile
                # requires that we can move horizontally and vertically.
                # We are not at a junction tile.
                return False
        else:
            return False

    def __str__(self):
        string = ''
        for row in range(self.__rows + 2):
            for col in range(self.__cols + 2):
                string += self.__MARKER_CHARS[self.markers[col][row]]

            string += '\n'

        return string


class MoveIter():
    def __init__(self, maze, start):
        self.visited = []
        self.maze = maze
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        pass


"""
def path_gen(marked_maze):


def solve(maze, entrance, exit):


gen1: 
    marks and traverses stepwise.
    terminated when no more traversals are possible.
    yields (DIRECTION, (target_coords)
gen2: 
    mark out a path on resulting map.
    trace single marked tiles until exit found.

solve: find path in maze. (dynamic programming?)
    create gen1.
    for move in gen1:
        if exit node is found:
            break
        if stopiteration is raised.
            the maze has no solution
    
    create gen2.
    path = []
    for move in gen2:
        path += move

    return path
"""
