"""
Retrieval warm-up (no notes, no running code yet)
Without looking back:
- what are the three components of any comprehension, in order? Write the skeleton syntax for list, dict, and set from memory.

List: [expression for item in iterable if condition]
Dict: {key_expr: value_expr for item in iterable if condition}
Set: {expression for item in iterable if condition}
You can put it inside a function's return statement, but the comprehension itself doesn't require one. Fix that distinction before moving on.

- What's the actual difference, in terms of what's happening in memory, between a for loop with .append() and a list comprehension?
oth the traditional loop and the comprehension build a list in memory, so "it's one list instead of two" isn't actually the explanation (the comprehension doesn't skip list-creation, it still makes a list). The real reasons are:

.append() is a method lookup and function call, repeated every iteration. The comprehension compiles to a dedicated bytecode instruction (LIST_APPEND) that skips that lookup overhead.
The comprehension's loop variable lives in its own scope in Python 3, it doesn't leak into your surrounding code the way a for loop's variable does
"""

# Practical exercise
articles = [
    {"title": "Python Basics", "source": {"name": "Tech Daily"}, "views": 1200},
    {"title": "AI", "source": {"name": "Tech Daily"}, "views": 50},
    {"title": "Market News", "source": {"name": "Finance Weekly"}, "views": 800},
    {"title": "Crypto Update", "source": {"name": "Finance Weekly"}, "views": 15},
]

# Write a list comprehension that returns titles of articles with views > 100.
