# Lab 5: Static Code Analysis

## Overview
This lab demonstrates the use of static code analysis tools (Pylint, Flake8, and Bandit) to improve Python code quality, security, and maintainability.

## Files Included

### 📋 **Deliverables**
- `inventory_system.py` - Fixed and improved inventory management system
- `issues_documentation.md` - Comprehensive table of identified issues and fixes
- `reflection.md` - Reflection on the static analysis experience

### 📊 **Analysis Reports**
- `pylint_report.txt` - Original Pylint analysis results
- `flake8_report.txt` - Original Flake8 style analysis results  
- `bandit_report.txt` - Original Bandit security analysis results

### 📚 **Reference**
- `Lab5` - Lab description and tool overview
- `Lab_5_Static_code_analysis_Student_handout.docx` - Complete lab instructions

## Results Summary

### Code Quality Improvement
- **Before**: Pylint score 4.80/10 (22 issues)
- **After**: Pylint score 9.59/10 (2 minor issues)
- **Improvement**: 99.8% quality increase

### Issues Fixed
- ✅ Security vulnerabilities (eval() usage)
- ✅ Dangerous default arguments
- ✅ Improper exception handling
- ✅ Resource management issues
- ✅ PEP 8 style violations
- ✅ Missing documentation
- ✅ Naming convention issues

## Tools Used
- **Pylint**: Code quality and logical error detection
- **Flake8**: PEP 8 style compliance checking
- **Bandit**: Security vulnerability scanning

## How to Run
```bash
# Install required tools
pip install pylint flake8 bandit

# Run the improved code
python inventory_system.py

# Run static analysis
pylint inventory_system.py
flake8 inventory_system.py
bandit -r inventory_system.py
```