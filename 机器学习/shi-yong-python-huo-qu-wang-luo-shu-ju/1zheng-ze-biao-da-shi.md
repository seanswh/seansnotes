A regular expression, regex or regexp(sometimes called a rational expression)is a sequence of characters that define a search pattern. Usually such patterns are used by string searching algorithms for "find" or "find and replace" operations on strings, or for input validation. It is a technique developed in theoretical computer science and formal language theory
use:
1.Matching
  re.search() returns a True/False depending on whether the string matches the regular expression
2.Extracting
 if we actually want the matching string to be extracted,we use re.findall()
 Greedy Matching: .+ match the largest result
 Non-Greedy Matching: .+?