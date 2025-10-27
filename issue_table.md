# Issue Table for Lab Submission

## Copy-Paste Ready Table:

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

## Alternative Format (if you need it formatted differently):

**Issue 1:**
- Issue: Mutable default arg
- Type: Bug  
- Line(s): 8
- Description: logs=[] shared across calls
- Fix Approach: Change default to None and initialize in method

**Issue 2:**
- Issue: Use of eval
- Type: Security
- Line(s): 59
- Description: eval() allows arbitrary code execution
- Fix Approach: Remove eval() call completely

**Issue 3:**
- Issue: Bare except
- Type: Bug
- Line(s): 19
- Description: except: catches all exceptions
- Fix Approach: Change to specific except KeyError:

**Issue 4:**
- Issue: Missing context manager
- Type: Bug
- Line(s): 26, 32
- Description: Files opened without with statement
- Fix Approach: Use with open() for proper resource management

**Issue 5:**
- Issue: Function naming
- Type: Style
- Line(s): 8, 14, 22, 25, 31, 36, 41
- Description: Functions not in snake_case
- Fix Approach: Rename addItem → add_item, etc.

**Issue 6:**
- Issue: Missing docstrings
- Type: Style
- Line(s): 1, 8, 14, 22, 25, 31, 36, 41, 48
- Description: No documentation for module/functions
- Fix Approach: Add comprehensive docstrings

**Issue 7:**
- Issue: Unused import
- Type: Style
- Line(s): 2
- Description: logging imported but never used
- Fix Approach: Remove unused import statement

**Issue 8:**
- Issue: Old string formatting
- Type: Style
- Line(s): 12
- Description: Using % instead of f-strings
- Fix Approach: Change to f-string format