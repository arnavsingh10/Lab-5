# Reflection: Static Code Analysis Lab

**Name:** Arnav Singh  
**File:** Inventory_sytstem_new.py  

## 1. Which issues were the easiest and hardest to fix?
The easiest ones were removing the unused import and fixing naming conventions.  
The hardest was replacing the `eval()` and handling the mutable default argument properly.

## 2. Did the tools report any false positives?
Yes, Pylint reported the use of a global variable as a warning.  
However, in this small project, it’s acceptable and not an actual problem.

## 3. How would you integrate static analysis tools in real development?
I would set up these tools (Pylint, Flake8, Bandit) in a pre-commit hook or CI pipeline  
so code gets checked automatically before merging or deploying.

## 4. What improvements did you observe in your code?
The code became more secure (no eval), more maintainable,  
and more readable with better naming, documentation, and safe file handling.
