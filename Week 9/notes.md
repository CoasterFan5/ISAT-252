# Random Knowledge
This is a long, text-heavy section. Sorry.

## Problem Solving in Programming
### Problem solving steps:
1) Recognize and understand the problem
   - Indentify programming opportunities
     - Repetitive work
     - Large amounts of data
     - Complex calculations
     - Info that needs to be organized, stored, or retried efficiently
   - Analyze the problem
     - Where is the current system failing
     - Consider stakeholders
     - Inputs/outputs
     - Constraints or regulations
     - How might the solution change in the future
   - Define the scope
     - Boundaries of solution
     - What will the program address and not address 
     - What features are essential, what can be added later?
     - Potential roadblocks or challenges
2) Break down the problem
   - Once the problem is understood, break it down into smaller, manageable sub-problems
   - This technique is known as "decomposition"
   - Make the problem more approachable
3) Plan your approach
   - Sketch out a plan
   - Flowcharts, pseudocode, just a list describing program steps
4) Start simple, then expand
   - Begin with a simple version of the program that solves the core problem
   - Once that's working, add features or handle edge cases
5) Use what you know
   - Start with the programming concepts you know best
6) Test as you go
   - Test each part as you write it 
7) Learn from your errors

## Principles of program design: Crafting effective and maintainable code
### Modularity: Building blocks of good design
- Modularity is the practice of dividing a program into seperate, interchangeable components
- Each module should have a specific, well-defined purpose
- Modularity is good!
  - Easier to understand
  - Easier to debug
  - Reusability
  - Collaboration

### Abstraction
- Abstraction involves hiding complex implementation details behind a simple interface
- Abstraction is about creating a clear, separation between what a module does and how it does it
- Design functions that have a clear purpose, even if the purpose seems like a black box

### Separation of concerns
- Principle that suggests program should be divided into distinct sections
- Each section should address a seperate concern
- Ex: If you have a menu, each menu task should be a different part of the program
- Common separations:
  - I/O operations
  - Data processing
  - User interface
  - Business Logic

### DRY (Don't Repeat Yourself)
- This principal advocates for reducing repetition in code
- Don't write similar code in a lot of places, make it a function or module
- This reduces possible errors
- Improves the maintainability of the program

### KISS (Keep it simple, stupid)
- Simplicity in design
- Avoid over-engineering solutions
- Start with the simplest design that solves the problem
- Only add complexity when necessary
- Makes programs easier to understand and maintain
- Reduces bugs
- Speeds up development

### Planning your design

### Iterative Design
- Creating a design often emerges through iteration
  1) Create an initial design
  2) Implement og design
  3) Test and evaluate
  4) Identify improvements
  5) Refine the design
  6) Repeat steps 2-5

## Strategies for effective debugging: Solving the puzzle of code errors
### Understanding debugging
- Debugging is like being a detective in a mystery novel
- Job is about figuring out why code isn't working 
### Get in the right mindset
- Stay calm and positive: Bugs are normal in programming
- By systematic: Random changes rarely solve the problem
- Learn from each bug
### High level debugging strategy:
1) Reproduce the problem
   - Identify exact conditions under which the error occurs
   - Create a simple, reliable way to make error happen consistently
2) Describe and understand the problem
   - What did you expect to happen
   - What actually happened?
   - Are there any error messages? If so, what do they say?
3) Gater Information
   - Use print or assert statements to track variable values and program flow
   - If available, use a debugger to step through code line by line
   - Check your assumptions about how your code should work
   - Maybe ask AI or google your problem
4) Form a hypothesis
5) Test hypothesis
6) Repeat 3-5
7) Profit???

### More debugging tips
- Use good variable names, it will help
- Ensure code is understandable, if there is complex logic, abstract it or add comments
  - Comments should explain WHY code is written in such a way
  - Comments need to be useful, if you need comments to explain what code is doing, that's a problem
- [Rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging) 
- Divide and conquer
  - Binary search to solve a problem
- Take a break
- Use version control (GitHub)
- Learn to read error messages
- Check for common errors
  - Spelling errors
  - Stop by 1 error in loops
  - etc.
- Use debugging tools like breakpoints
- Write test cases and utilize testing frameworks (See week 2 assignment)

## Professionalism

### Important Considerations
- Reliability: Code must work consistently and correctly 
- Maintainability: Others should be able to understand and modify code
- Scalability: Solutions should be able to scale to new demands
- Efficiency: Use resources like time and memory efficiently
- Security: Don't make security vulnerabilities

### Teamwork
- Version Control
  - Learn Git
- Code reviews
  - Peer review code before it is merged into the main codebase
  - Catch errors, ensure quality
- Agile Methodologies
  - Many teams use agile methods like [Scrum](https://www.scrum.org/resources/what-scrum-module) or [Kanban](https://www.atlassian.com/agile/kanban#:~:text=In%20Japanese%2C%20kanban%20literally%20translates,in%20a%20highly%20visual%20manner.) to manage projects
- Communication Skills
  - Clear communication is crucial
  - Explain ideas
  - defend decisions
  - prepare to compromise

### Writing profession grade code
- Write readable, self-documenting code
- Comments that explain "why" not "what"
- ```python
  # poor naming
  def calc(a, b):
    return a * b
  
  # good naming
  def calculate_rectangle_area(length, width):
    return length * width
- Error handling
  - Try-except blocks
- Testing
  - Write unit tests
  - Implement tests for larger systems
  - Practice test-driven development
- Code organization
  - Follow DRY
  - Use appropriate design patterns
  - Modulation and classes
- 
