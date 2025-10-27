# Static Code Analysis Issues Documentation

## Issues Identified and Fixed

| Issue # | Tool | Line | Issue Type | Severity | Description | Fix Applied |
|---------|------|------|------------|----------|-------------|-------------|
| 1 | Manual/Security | 59 | Security Vulnerability | **HIGH** | Use of `eval()` function - allows arbitrary code execution | Removed `eval()` call completely |
| 2 | Pylint | 8 | Dangerous Default Value | **HIGH** | Mutable default argument `logs=[]` can cause unexpected behavior | Changed to `logs=None` with proper handling |
| 3 | Pylint/Flake8 | 19 | Exception Handling | **MEDIUM** | Bare `except:` clause hides all exceptions | Changed to specific `except KeyError:` |
| 4 | Pylint | 26,32 | Resource Management | **MEDIUM** | Files opened without context managers | Implemented `with open()` statements |
| 5 | Pylint | 26,32 | Encoding Issue | **MEDIUM** | File operations without explicit encoding | Added `encoding='utf-8'` parameter |
| 6 | Flake8 | 2 | Unused Import | **LOW** | `logging` module imported but never used | Removed unused import |
| 7 | Pylint | 8,14,22,25,31,36,41 | Naming Convention | **LOW** | Function names not in snake_case | Renamed all functions to snake_case |
| 8 | Flake8 | Multiple | PEP 8 Spacing | **LOW** | Missing blank lines between functions | Added proper spacing per PEP 8 |
| 9 | Pylint | 12 | String Formatting | **LOW** | Old-style string formatting | Changed to f-string formatting |
| 10 | Pylint | 1,8,14,22,25,31,36,41,48 | Documentation | **LOW** | Missing docstrings | Added comprehensive docstrings |

## Summary
- **Total Issues Found**: 10
- **High Severity**: 2 (Security & Dangerous defaults)
- **Medium Severity**: 3 (Exception handling, resource management)
- **Low Severity**: 5 (Style and documentation)
- **Issues Fixed**: 10 (All issues addressed for bonus marks)

## Tools Performance
- **Pylint**: Most comprehensive, found 22 individual violations
- **Flake8**: Good for style compliance, found 11 PEP 8 violations  
- **Bandit**: Had compatibility issues with Python 3.14, manual security review performed