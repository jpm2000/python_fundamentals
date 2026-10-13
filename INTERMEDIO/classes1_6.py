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

# 1. Write a list comprehension that returns titles of articles with views > 100.
print("Exercise 1:")


def get_titles_over_100(articles):
    return [article["title"] for article in articles if article["views"] > 100]


print(get_titles_over_100(articles))


# 2.Set comprehension:
"""
Get the unique source names from articles using a set comprehension. 
Then answer: what happens to your comprehension if one article is missing the "source" key entirely? 
Don't just say "it breaks," write the fix.
"""
print("---------------------------")
print("Exercise 2:")


def get_unique_sources(articles):
    # The { ... } tells Python to build a set, and sets automatically keep only unique values.
    return {
        article.get("source").get("name")
        for article in articles
        # This makes sure that the article has a source with a name, because otherwise it could print a None value or
        if article.get("source") and article.get("source").get("name")
    }


print(get_unique_sources(articles))

# 3. Dict comprehension
"""
Build a dict mapping title -> views for articles with more than 100 views.
"""
print("---------------------------")
print("Exercise 3:")


def get_title_views_dict(articles):
    return {
        article["title"]: article["views"]
        for article in articles
        if article["views"] > 100
    }


print(get_title_views_dict(articles))


# 4. Nested dict comprehension
"""
Without copying the pattern from your notes, build from scratch a dict where each key is a unique source name and each value is a list of titles from that source. Do it as a nested comprehension, not two loops. If you get stuck, write the traditional nested-for version first, then convert it, the way the course itself taught you to approach it.
"""
print("---------------------------")
print("Exercise 4:")


def get_source_titles_traditional(articles):
    sources = get_unique_sources(articles)
    source_titles = {}
    for source in sources:
        if source not in source_titles:
            source_titles[source] = []

        for article in articles:
            if article.get("source").get("name") == source:
                source_titles[source].append(article["title"])
    return source_titles


print(get_source_titles_traditional(articles))


def get_source_titles_comprehension(articles):
    sources = get_unique_sources(articles)
    return {
        source: [
            article["title"]
            for article in articles
            if article.get("source").get("name") == source
        ]
        for source in sources
    }


print(get_source_titles_comprehension(articles))


# 5. The judgment call
"""
Take exercise 4 and make it harder: now also filter so only articles with views > 100 are included in the inner lists. At what point does this comprehension stop being "more readable" than a regular nested for loop? Give me your actual opinion, not a hedge. This is the real skill, knowing when to stop.
"""
print("---------------------------")
print("Exercise 5:")


def filter_source_titles_traditional_100_views(articles):
    sources = get_unique_sources(articles)
    source_titles = {}
    for source in sources:
        source_titles[source] = []
        for article in articles:
            if article["source"]["name"] == source and article["views"] > 100:
                source_titles[source].append(article["title"])
    return source_titles


print(filter_source_titles_traditional_100_views(articles))


def filter_source_titles_comprehension_100_views(articles):
    sources = get_unique_sources(articles)
    return {
        source: [
            article["title"]
            for article in articles
            if article["source"]["name"] == source and article["views"] > 100
        ]
        for source in sources
    }


print(filter_source_titles_comprehension_100_views(articles))

# 6. F-strings, formatting
"""
Given balance = 1234567.891, write one f-string expression that displays it as $1,234,567.89.
"""
print("---------------------------")
print("Exercise 6:")

balance = 1234567.891
text = f"The balance is: {balance:,}"
print(text)

# 7. F-strings with logic
"""
Given the articles list above, write a single f-string (inside a loop or comprehension) that prints each title left-aligned in 20 characters, followed by its view count right-aligned in 8 characters, followed by " (popular)" if views > 100 else " (low)".
"""
print("---------------------------")
print("Exercise 7:")


def popular_articles_traditional(articles):
    for article in articles:
        if article["views"] > 100:
            print(
                f"Title: {article['title']:<20} Views count: {article['views']:>8} Popularity: (popular)"
            )
        else:
            print(
                f"Title: {article['title']:<20} Views count: {article['views']:>8} Popularity: (low)"
            )


popular_articles_traditional(articles)


# V1
def popular_articles_comprehension(articles):
    return "\n".join(
        [
            f"Title: {article['title']:<20} Views count: {article['views']:>8} Popularity: {'popular' if article['views'] > 100 else 'low'}"
            for article in articles
        ]
    )


print(popular_articles_comprehension(articles))


# V2: best practices with the join
def popular_articles_comprehension(articles):
    return [
        f"Title: {article['title']:<20} Views count: {article['views']:>8} Popularity: {'popular' if article['views'] > 100 else 'low'}"
        for article in articles
    ]


print("\n".join(popular_articles_comprehension(articles)))

# 8. Combine everything
"""
Write one line that produces a list of formatted strings like "Tech Daily: 2 articles, 1250 total views", one per source, sorted by total views descending. This needs a comprehension to aggregate, an f-string to format, and you'll need to think about whether a plain comprehension can even sort, or whether you need something wrapping it.
"""
print("---------------------------")
print("Exercise 8:")


def suma(articles):
    return sum([article["views"] for article in articles])


print(suma(articles))


def number(articles):
    return len([article["views"] for article in articles])


print(len(articles))


def sources_articles_views(articles):
    sources = get_unique_sources(articles)
    return {
        source: [
            f"{len([article['views'] for article in articles if article['source']['name'] == source])} articles, {sum([article['views'] for article in articles if article['source']['name'] == source])} total views"
        ]
        for source in sources
    }


print(sources_articles_views(articles))


"""
EXTRA:
Push beyond the exercises

Comprehensions are really a restricted, more readable syntax for a mathematical idea: set-builder notation. {x : x ∈ S, P(x)} (the set of all x in S such that P(x) holds) is literally {x for x in S if P(x)}. This is not a coincidence, Python's comprehensions were deliberately modeled on this notation from set theory.

Go investigate: how does this connect to what you'll eventually do with numpy's boolean masking (array[array > 100])? Same underlying idea, wearing different syntax. Come back and explain, in your own words, why vectorized filtering in numpy is actually faster than a Python-level comprehension doing the equivalent filter, in terms of what's happening at the memory/execution level, not just "numpy is faster."
"""
