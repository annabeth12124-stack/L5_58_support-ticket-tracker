# Lab 5: Static Code Analysis — Support Ticket Tracker

**Your file:** `support_ticket_tracker.py`

Follow the lab handout for the full instructions.

## About the program

A support ticket tracker. It creates tickets with a priority and category, assigns them to agents, updates their status, searches and reports on them, and saves them to a JSON file.

The code works, but only just. It has quality, style and security problems of the kind Pylint, Flake8 and Bandit are built to find.

## What to do

1. **Run it first** and read the output carefully:
   ```bash
   python support_ticket_tracker.py
   ```
   It asks one question. Press Enter to skip, then try a few inputs of your own (for example a ticket id that does not exist). Not every problem in this file is something a tool will flag, so pay attention to output that looks wrong.

2. **Install the tools:**
   ```bash
   python -m pip install pylint bandit flake8
   ```

3. **Run the analysis** and save the reports:
   ```bash
   python -m pylint support_ticket_tracker.py > pylint_report.txt
   python -m bandit -r support_ticket_tracker.py > bandit_report.txt
   python -m flake8 support_ticket_tracker.py > flake8_report.txt
   ```

4. **Document the issues** in `issues.md` using this table (at least 4 rows, high and medium severity first):

   | Issue | Type | Line(s) | Description | Fix Approach |
   |-------|------|---------|-------------|--------------|
   | Use of eval() | Security (Bandit B307, Pylint W0123) | 92 | eval runs arbitrary code, and it was triggered by an environment variable. Bandit rated it medium severity. | Removed the RUN_UNSAFE_DEMO block and the now-unused import os. |
   | Bare except: pass | Security / Bug (Bandit B110, Pylint W0702, Flake8 E722)	 | 24-25 | Catches every exception and silently ignores it, which hides real errors. | Catch only KeyError and return False from the handler. |
   | Mutable default argument | Bug (Pylint W0102) | 10 | audit_log=[] is created once and shared across every call. | Removed the parameter and used a module-level AUDIT_LOG list. |
   | open() without with or encoding | Bug / Quality (Pylint R1732, W1514) | 46,53 | The file isn’t guaranteed to close if an error occurs, and the encoding is unspecified. | Used with open(..., encoding="utf-8") in save_tickets and load_tickets. |
   | Unused imports | Quality (Pylint W0611, Flake8 F401) | 4,5 | sys and random were imported but never used. | Deleted both prompts |
   | Missing docstrings | Quality (Pylint C0114, C0116) | module and 10 functions | No documentation on the module or any function. | Added one-line docstrings |
   | Global statement | Quality (Pylint W0603) | 52 | load_tickets reassigned the module-level TICKETS using global. | Cleared and updated the existing dictionary in place. |
   | Naming and comparison style | Style (Pylint C0103, C0121) | 66, 37 | closeTicket isn’t snake_case, and != None should use is not None. | Renamed to close_ticket and used is not None. |
   | Unused variable and argument | Quality (Pylint W0612, W0613) | 84, 20 | count and notify were never used. | Removed both |
   | Line length and whitespace | Style (Flake8 E501, W291, E305) | 10, 14 and others | Lines over 79 characters, trailing spaces, and one blank line too few before if __name__. | Wrapped long lines, trimmed whitespace, and added the second blank line. |
   

6. **Fix the code.** Fix at least 4 of the issues you documented, then rerun all three tools to confirm they are gone. Repeat until you are satisfied. The program should still do its job when you are done.

7. **Reflect.** Answer the four reflection questions from the handout in `reflection.md`.

## Deliverables

1. `support_ticket_tracker.py`: your cleaned version, with at least 4 issues fixed.
2. `issues.md`: the completed issue table.
3. `reflection.md`: your answers to the reflection questions.

**Target:** aim for a Pylint score above 9.5 on your final file. A perfect 10.00/10 is very good.

Be ready to explain the bugs you found and how you fixed them. You may be called on to present.
