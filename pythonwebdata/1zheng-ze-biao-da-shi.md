A regular expression, regex or regexp(sometimes called a rational expression)is a sequence of characters that define a search pattern. Usually such patterns are used by string searching algorithms for "find" or "find and replace" operations on strings, or for input validation. It is a technique developed in theoretical computer science and formal language theory
use:
1.Matching
  re.search() returns a True/False depending on whether the string matches the regular expression
2.Extracting
 if we actually want the matching string to be extracted,we use re.findall()
 Greedy Matching: .+ match the largest result
 Non-Greedy Matching: .+?
 ![](\pythonwebdata\images\cheatsheet.PNG)
 
some of the cheat sheet
^	Matches the beginning of a line
$	Matches the end of the line
.	Matches any character
\s	Matches whitespace
\S	Matches any non-whitespace character
*	Repeats a character zero or more times
*?	Repeats a character zero or more times (non-greedy)
+	Repeats a character one or more times
+?	Repeats a character one or more times (non-greedy)
[aeiou]	Matches a single character in the listed set
[^XYZ]	Matches a single character not in the listed set
[a-z0-9]	The set of characters can include a range
(	Indicates where string extraction is to start
)	Indicates where string extraction is to end
 