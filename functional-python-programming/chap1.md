More importantly, the presence of abstractions and virtual machines doesn't
materially change our approach to designing software to exploit the functional
programming features of Python.

Our functional Python programs will rely on the following three stacks of
abstractions:
- Our applications will be functions - all the way down - until we hit the
	objects
- The underlying Python runtime environment that supports our functional
	programming is objects - all the way down - until we hit the turtles
- The libraries that support Python are a turtle on wich Python stands
