"""
🔍 Step 1: Identify Features (Decompose the shapes)

For each figure, extract objective attributes:

| Shape | Sides | Type     | Orientation             | Symmetry      |
| ----- | ----- | -------- | ----------------------- | ------------- |
| 1     | 5     | Pentagon | Upright                 | Symmetrical   |
| 2     | 5     | Pentagon | Rotated                 | Symmetrical   |
| 3     | 6     | Hexagon  | Upright                 | Symmetrical   |
| 4     | 3     | Triangle | Right-angled            | Not symmetric |
| 5     | 6     | Hexagon  | Flat top                | Symmetrical   |
| 6     | 3     | Triangle | Right-angled (mirrored) | Not symmetric |

Step 2: Look for Strong Patterns

The most reliable grouping features are:

1. Number of sides
Triangles → (3 sides): 4, 6
Pentagons → (5 sides): 1, 2
Hexagons → (6 sides): 3, 5
2. Shape type (most dominant pattern here)

This is the cleanest and most consistent grouping.

Final Grouping

(1,2); (3,5); (4,6)

1,2 → Pentagons
3,5 → Hexagons
4,6 → Triangles


How to Tackle These Questions (General Strategy)
1. List observable attributes

Always break shapes into:

Number of sides
Angles (right angle? acute?)
Orientation (rotated, flipped)
Symmetry
Size (if relevant)
2. Test grouping hypotheses quickly

Try grouping by:

Shape type (most common answer)
Rotation/orientation
Symmetry vs asymmetry
Regular vs irregular

Reject any grouping that doesn’t cleanly include all items.

3. Prefer the simplest consistent rule

If one rule cleanly partitions everything (like number of sides here), it’s almost always correct.

4. Ignore distractions

Rotation (e.g., shape 1 vs 2) is often a trap—they’re still the same shape.

⚠️ Common Traps
Overfocusing on orientation instead of structure
Mixing grouping rules (e.g., some by shape, others by rotation)
Ignoring a simpler pattern in favor of a complex one
"""



"""
Practice Question

You are given 6 figures with the following properties:

| Shape | Description                         |
| ----- | ----------------------------------- |
| 1     | Square, rotated 45° (diamond shape) |
| 2     | Square, normal orientation          |
| 3     | Circle                              |
| 4     | Rectangle (long horizontal)         |
| 5     | Circle                              |
| 6     | Rectangle (vertical)                |


❓ Task

Group the shapes into 3 pairs based on a consistent rule.

Write your answer like:

(?, ?); (?, ?); (?, ?)

MY ANSWER: Orientation could have worked but it is not consistent. So I am grouping with shape, (1,2),(3,5),(4,6)

That’s exactly the right reasoning—and the correct answer.

✅ Your grouping:

(1,2), (3,5), (4,6)

🔍 Why this is correct

You explicitly did two important things:

1. Tested a hypothesis (orientation)
Squares: 1 (rotated), 2 (normal) → mismatch
Rectangles: 4 (horizontal), 6 (vertical) → mismatch
👉 So orientation is not a stable grouping rule
2. Fell back to a stronger invariant (shape type)
Squares → 1, 2
Circles → 3, 5
Rectangles → 4, 6

This is exactly how high-performing candidates approach these problems:

Try → Break → Replace with a more stable rule
"""


"""
Types of Number Pattern Questions
1. Arithmetic Progression (constant difference)

2, 5, 8, 11, ?
Pattern: +3
Answer: 14

2. Geometric Progression (constant ratio)

3, 6, 12, 24, ?
Pattern: ×2
Answer: 48

3. Alternating Patterns

2, 5, 3, 6, 4, ?
Split into two sequences:

2, 3, 4 → +1
5, 6, ? → +1
Answer: 7


4. Increasing Differences

1, 3, 6, 10, ?
Differences:
+2, +3, +4 → next is +5
Answer: 15

5. Multiplication + Addition Combo

2, 5, 11, 23, ?
Pattern:
×2 +1 → ×2 +1 → ×2 +1
Answer: 47

6. Squares / Cubes / Powers
1, 4, 9, 16, ?
Pattern: squares
Answer: 25

7. Fibonacci-style (sum of previous terms)
1, 1, 2, 3, 5, ?
Answer: 8

8. Position-based patterns
2, 6, 12, 20, ?

Pattern:
n(n+1):
1×2=2
2×3=6
3×4=12
4×5=20
5×6=30
Answer: 30

Step-by-Step Strategy

When you see a sequence:

1. Check differences

→ If constant → arithmetic
→ If increasing → pattern in differences

2. Check ratios

→ If constant → geometric

3. Look for alternating patterns

→ Split into odd/even positions

4. Look for known sequences

→ squares, cubes, Fibonacci

5. Try combinations

→ multiply + add
→ alternating operations
"""



"""
3, 9, 27, 81, ?
CHECKING DIFF (NOT CONSTANT)
6, 18, 54 
CHECKING RATIOS
9/3 = 3, 27/9 = 3, 81/27 = 3
ANSWER 243 CORREDD

TRY THIS: 2, 6, 7, 21, 22, ?


Look for an alternating pattern

Odd positions:
2, 7, 22
2 -> 7 = 2X3+1
7 -> 22 = 7X3+1

Even positions:
6, 21, ?
6 -> 21 = 6X3 + 3
21 -> ? = 21X3 + 3 = 66 CORRECT


What you missed (important learning)

You stopped at differences, but didn’t escalate to:

“Is this alternating?”

That’s the next level move when:

Differences look irregular
Small numbers alternate with big jumps


Try this (this is a real test-level question):
5, 10, 12, 24, 27, ?

alternating sequence observed
odd position
5, 12, 27
5-> 12 = 5x2+2
12 -> 27 = 12x2+3

even position
10,24,?
10->24 = 10x2+4
24->? =  48+5 = 53


"""


