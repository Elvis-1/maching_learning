# Simple Types

from typing import List, Dict, Tuple, Set, Optional, Union, Any

# Basic types
name: str = "John"
age: int = 25
price: float = 19.99
is_active: bool = True
data: bytes = b"hello"

# Function with type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> float:
    return a / b


# Collection Types

# Lists
from typing import List

# List of strings
names: List[str] = ["Alice", "Bob", "Charlie"]

# List of integers
scores: List[int] = [95, 87, 92]

# List of mixed types (use Union)
mixed: List[Union[str, int]] = ["hello", 42, "world"]

# List of lists
matrix: List[List[int]] = [[1, 2, 3], [4, 5, 6]]

# Function returning list of strings
def get_names() -> List[str]:
    return ["Alice", "Bob"]


# Dictionaries

from typing import Dict

# String keys, integer values
scores: Dict[str, int] = {"Alice": 95, "Bob": 87}

# String keys, list values
groups: Dict[str, List[str]] = {
    "A": ["Alice", "Bob"],
    "B": ["Charlie"]
}

# Nested dictionary
config: Dict[str, Dict[str, int]] = {
    "server": {"port": 8080, "timeout": 30}
}

# Function returning dictionary
def get_config() -> Dict[str, Any]:
    return {"host": "localhost", "port": 8080}

# Tuples

from typing import Tuple

# Fixed-length tuple
coordinates: Tuple[int, int] = (10, 20)
person: Tuple[str, int, bool] = ("Alice", 25, True)

# Variable-length tuple (homogeneous)
scores: Tuple[int, ...] = (95, 87, 92, 88)

# Function returning tuple
def get_user() -> Tuple[str, int]:
    return "Alice", 25

# Sets

from typing import Set

# Set of strings
tags: Set[str] = {"python", "coding", "tutorial"}

# Set of integers
numbers: Set[int] = {1, 2, 3, 4, 5}


# Advanced Types

# Optional (Nullable)

