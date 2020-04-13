Domain Modeling Recap
Domain modeling
This is the part of your code that is closest to the business, the most likely to change, and the place where you deliver the most value to the business. Make it easy to understand and modify.

Distinguish entities from value objects
A value object is defined by its attributes. It’s usually best implemented as an immutable type. If you change an attribute on a Value Object, it represents a different object. In contrast, an entity has attributes that may vary over time and it will still be the same entity. It’s important to define what does uniquely identify an entity (usually some sort of name or reference field).

Not everything has to be an object
Python is a multiparadigm language, so let the "verbs" in your code be functions. For every FooManager, BarBuilder, or BazFactory, there’s often a more expressive and readable manage_foo(), build_bar(), or get_baz() waiting to happen.

This is the time to apply your best OO design principles
Revisit the SOLID principles and all the other good heuristics like "has a versus is-a," "prefer composition over inheritance," and so on.

You’ll also want to think about consistency boundaries and aggregates
But that’s a topic for [chapter_07_aggregate].<Paste>
