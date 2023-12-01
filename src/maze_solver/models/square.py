from dataclasses import dataclass
from maze_solver.models.border import Border
from maze_solver.models.role import Role

@dataclass(frozen=True)
class Square:
    """
    The Square class conveys information about a particular location in the maze.
    Each location is unique and each square has a border pattern that describes the maze structure at that location"""
    index: int
    row: int
    column: int
    border: Border
    role: Role = Role.NONE