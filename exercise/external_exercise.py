"""
Please write the solution in Python -Description-
An Australian Rules Football (AFL) season consists of regular season fixtures, where each team plays each other twice - once at Home and once Away, followed by the "Finals". The Finals format is similar to "Playoffs" in other sports.
Files
tas
t
To work out which teams make it to Finals, a league ladder is created in which teams are ranked by highest points and percentage.
A win is worth 4 points
A draw is worth 2 points
A loss is worth 0 points
Where teams have the same number of points, they are then ranked by percentage, with a higher percentage being better, the percentage is calculated as:
(100* For / Against)
Where For is the sum of the total number of points scored by the team in all fixtures
Where Against is the sum of the total number of points scored by opponents in all fixtures.   We will also assume that only the top two teams in the ladder will progress to Finals.
You can start with the assumption that there are no draws.
task1
solut.
Latesti...
2
uS
// ex
4
Write a function
de
me
class Solution { public stringll solution(stringll A, stringll B, stringlC); }
9
that parses the teams, the fixtures, and the results and returns a 2-element array containing the NAMES of the top 2 teams in the ladder at the end of the season. If you have any errors or exceptions, you should return an array containing two empty strings.
Error handling is required for the function. If the function receives invalid input data, you should handle the resulting errors appropriately and return an array containing two empty strings.
10
11
12
13
Teams are in the format l'a: Team1", "b:Team2]
.. where a key and value are separated by a "."
To leave ed
Test Output
Fixtures are in the format - ['a:b", "b:a"
- where the key for each team is used
G taski
I solut...
In test-i....
Results are in the format
['50:100", "75.25")
... where the first value corresponds to the first team in a fixture
-Edge cases--
- If you have any errors or exceptions, you should return an array containing two empty strings
- How would you account for draws?
- How would you account for more teams?
- What checks would you put in for bad data?
-Example-
If you are given:
A-l"a:Essendon""b:East Coast","c:Swans""d: Tigers]
B-"ab""ac""ad""ba""b:c""b:d","c:a","c:b"cid""d:a""d:b","d:c"]
C=*87:55944:509111:88 102:4211281 81:36 7239:38:64 57:53 46:65 3773 95:621
Then your function should return ['East Coast', 'Swans' ].
"""