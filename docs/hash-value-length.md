## Choosing the Right Hash Length for URL Shortening

it has a major impact on how your system performs — from scalability and collision risk to usability and readability.

### How Many Unique Hashes Can Each Length Support?

The hashValue consists of characters from [0-9, a-z, A-Z], containing 10 + 26 + 26 = 62
possible characters.

| N |           Maximal number of URLs            | 
|:--|:-------------------------------------------:| 
| 1 |                 62 ^ 1 = 62                 | 
| 2 |                62 ^ 2 = 3844                |
| 3 |              62 ^ 3 = 238,328               | 
| 4 |             62 ^ 4 = 14,776,336             |
| 5 |            62 ^ 5 = 916,132,832             | 
| 6 |   62 ^ 6 = 56,800,235,584 =~ 56.8 billion   |
| 7 | 62 ^ 7 = 3,521,614,606,208 = ~ 3.5 trillion |

### Trade-Offs: Short (5-6) vs. Long Hashes (7-8)
- Use shorter hashes for personal projects, internal tools, or small-scale apps.

- Use longer hashes for public-facing services, production apps, or when future growth is expected.

### Why 7 Characters Is a Popular Choice
A 7-character hash offers around 3.5 trillion unique combinations. That's a sweet spot for most practical use cases:

- Large enough to support millions or billions of URLs

- Still short enough to be human-friendly

- Minimizes the chance of collisions without being overkill

For comparison, a 6-character hash only offers 56.8 billion combinations — that’s 61× fewer than 7 characters. That one extra character buys you a massive boost in capacity.

