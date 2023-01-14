# Code Complexity Analyzer

This script is a tool for measuring various metrics of code complexity in a given Python source file. It uses the `ast` module to parse the code and extract information about the number of control structures (such as if-statements, for-loops, while-loops, and function/lambda definitions), the number of source lines of code (SLOC), the number of physical lines of code (PLOC), and the number of logical lines of code (LLOC). 

## Usage

To use the script, run it in the command line and provide the path to the Python file you want to analyze as input. The script will then output the results to the console and write them to a file named "cc.json" in the same directory. 

The script also generates histograms for each metric to visualize the data.

### Required Libraries
* ast
* sys
* json
* matplotlib

### Example

```
python script.py
Enter a Path: main.py

complexity: 10
sloc: 67
ploc: 73
lloc: 17
```


## Metrics

1. **Cyclomatic Complexity**: This is a measure of the number of linearly independent paths through a program's source code. It is calculated by counting the number of control structures (such as if-statements, for-loops, while-loops, and function/lambda definitions) in the code.
2. **Source Lines of Code (SLOC)**: This is a measure of the number of lines of code in the source file, excluding comments and blank lines.
3. **Physical Lines of Code (PLOC)**: This is a measure of the total number of lines of code in the source file, including comments and blank lines.
4. **Logical Lines of Code (LLOC)**: This is a measure of the number of lines of code that contribute to the program's functionality, calculated by counting the number of lines in functions and class definitions.

# CodeComplexityAnalyzer
# CodeComplexityAnalyzer
