## Designing a URL shortening service like tinyurl.

## Understand the problem and establish design scope
- What would be the expectation:
- Assume URL https://leetcode.com/studyplan/top-sql-50/ 
  Your service creates an alias with shorter length: https://tinyurl.com/3r9am3tn if you
click the alias, it redirects you to the original URL.
- What would be the traffic volume per sec ?
- How long is the shortened URL ? (As short as possible)
- What characters are allowed ? (combination of numbers (0-9) and characters (a-z, A-
Z))
- Can shortened URLs be deleted or updated ? (No, for this example)

## Use cases:
1. URL shortening: given a long URL => return a much shorter URL
2. URL redirecting: given a shorter URL => redirect to the original URL
3. High availability, scalability, and fault tolerance considerations