# Issue Table for Lab Submission

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Mutable default arg | Bug | 8 | logs=[] shared across calls | Change default to None and initialize in method |
| Use of eval | Security | 59 | eval() allows arbitrary code execution | Remove eval() call completely |
| Bare except | Bug | 19 | except: catches all exceptions | Change to specific except KeyError: |
| Missing context manager | Bug | 26, 32 | Files opened without with statement | Use with open() for proper resource management |
| Function naming | Style | 8, 14, 22, 25, 31, 36, 41 | Functions not in snake_case | Rename addItem → add_item, etc. |
| Missing docstrings | Style | 1, 8, 14, 22, 25, 31, 36, 41, 48 | No documentation for module/functions | Add comprehensive docstrings |
| Unused import | Style | 2 | logging imported but never used | Remove unused import statement |
| Old string formatting | Style | 12 | Using % instead of f-strings | Change to f-string format |
