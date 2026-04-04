"""
We’ll break it into:

Basic arithmetic operations
Division types (very important)
Rounding (normal, up, down, precision)
Advanced numeric tools (math module)
Common real-world patterns
"""

# 1️⃣ Basic Number Operations in Python

# Python supports standard arithmetic operators:

"""
| Operation           | Operator | Example  | Result |
| ------------------- | -------- | -------- | ------ |
| Addition            | `+`      | `5 + 3`  | `8`    |
| Subtraction         | `-`      | `5 - 3`  | `2`    |
| Multiplication      | `*`      | `5 * 3`  | `15`   |
| Division            | `/`      | `5 / 2`  | `2.5`  |
| Floor division      | `//`     | `5 // 2` | `2`    |
| Modulus (remainder) | `%`      | `5 % 2`  | `1`    |
| Exponent            | `**`     | `5 ** 2` | `25`   |

"""

# 2️⃣ Division Types (Critical to Understand)
# Normal division /

# Always returns a float:

5 / 2   # 2.5

# Floor division //
# Rounds down to the nearest integer.

5 // 2    # 2
9 // 4    # 2

# ⚠ Important with negatives:

-5 // 2   # -3   (NOT -2)

# Why? Because it floors toward negative infinity.

# Modulus %

# Returns remainder:

9 % 4   # 1

"""
Very useful for:
Even/odd checks
Time calculations
Cyclic behavior
"""
number = 10
if number % 2 == 0:
    print("Even")

# 3️⃣ Rounding Numbers

# Now the part you asked about: rounding up and related behavior

round(3.6)   # 4
round(3.2)   # 3

# With precision:

round(3.14159, 2)   # 3.14

# ⚠ Important: Python uses banker’s rounding.

round(2.5)   # 2
round(3.5)   # 4

# This rounds to the nearest even number.

# B. Always Round Up → math.ceil()

# Use this when you need strict upward rounding.

import math

math.ceil(3.2)   # 4
math.ceil(3.0)   # 3
math.ceil(-3.2)  # -3

"""
Use case:

Calculating required pages
Splitting items into groups
Billing increments
"""

people = 5
seats_per_table = 2

tables_needed = math.ceil(people / seats_per_table)

print(tables_needed)

# C. Always Round Down → math.floor()

math.floor(3.8)   # 3
math.floor(-3.8)  # -4

# D. Truncation (Cut off decimals)

# This does NOT round — it simply removes decimals.

int(3.8)   # 3
int(-3.8)  # -3

"""
Notice the difference:
| Function  | -3.8 |
| --------- | ---- |
| `floor()` | -4   |
| `int()`   | -3   |

"""

# 4️⃣ Precision Formatting (Very Common)

# Instead of rounding numerically, sometimes you just format output.

# Using f-strings:

pi = 3.1415926
print(f"{pi:.2f}")   # 3.14

# This does:
# Round to 2 decimal places
# Format as float

"""
| Function            | Purpose                           |
| ------------------- | --------------------------------- |
| `math.sqrt(x)`      | Square root                       |
| `math.pow(x, y)`    | Power                             |
| `math.abs(x)`       | Absolute value (or just `abs(x)`) |
| `math.ceil(x)`      | Round up                          |
| `math.floor(x)`     | Round down                        |
| `math.factorial(x)` | Factorial                         |

"""

# 6️⃣ Floating Point Precision Issue (Important)

# This surprises many engineers:
0.1 + 0.2
0.30000000000000004
# This is due to binary floating-point representation.

# If precision matters (finance), use:
from decimal import Decimal
Decimal("0.1") + Decimal("0.2")

# 7️⃣ Real-World Rounding Patterns
# Round up to nearest 10

import math
math.ceil(number / 10) * 10

# Round down to nearest 10

(number // 10) * 10

# Round to nearest 0.5

round(number * 2) / 2

"""
8️⃣ Quick Mental Model

| Need                   | Use            |
| ---------------------- | -------------- |
| Normal rounding        | `round()`      |
| Always up              | `math.ceil()`  |
| Always down            | `math.floor()` |
| Remove decimals        | `int()`        |
| Display precision only | `f"{x:.2f}"`   |

"""

"""
9️⃣ Professional Advice

When solving real problems, ask:
Is rounding part of business logic?
Is rounding only for display?
Do negative numbers matter?
Does floating precision matter?
Many production bugs happen here.
"""




