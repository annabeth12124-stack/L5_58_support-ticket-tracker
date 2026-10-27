# Reflection

**Q1. Which tool’s report was the most useful, and why?**

Pylint was the most useful for improving the code, because it gave the broadest feedback: it started at 5.00/10 and covered bugs (the mutable default argument), design problems (too many arguments, the global statement), and missing documentation. Bandit was the most important for risk, since its two findings (eval at medium severity and except: pass at low severity) were the only security issues. Flake8 was the least informative, because it only checks formatting, but it’s the easiest to fix and keeps the code consistent. Together they gave a complete picture that none of them gives alone.

**Q2. Did any fix create a new problem, or were there any findings that weren’t really problems?**

Yes. When I removed the audit_log parameter from create_ticket to fix the mutable default, I left one line still using audit_log. Pylint reported E0602: undefined variable, and the program would have crashed with a NameError as soon as a ticket was created. Rerunning the tools after every change caught this. On the other side, the eval call was only reachable if an environment variable was set, so it was unlikely to run, but Bandit was still right to flag it, because eval should never be left in code.

**Q3. How do the three tools overlap, and why use all of them?**

They overlap on some issues. The bare except was flagged by all three (Bandit B110, Pylint W0702, Flake8 E722), and unused imports were flagged by both Pylint and Flake8. Each tool also catches things the others don’t: Bandit finds security risks like eval, Pylint finds design and quality problems like the mutable default, and Flake8 enforces PEP 8 formatting such as line length and whitespace. Using only one would leave gaps, so using all three gives better coverage.

**Q4. How would static analysis fit into a real project workflow?**

I would run the tools automatically, for example with a pre-commit hook or in a CI pipeline, so problems are caught before code review instead of after merging. That also saves reviewers time on style comments. Static analysis has limits, though: it can’t find logic errors that only appear at runtime, and a 10/10 Pylint score doesn’t prove the code is correct. It works best alongside testing and code review.
