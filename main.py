import ast
import sys
import json
import matplotlib.pyplot as plt

def calculate_complexity(src):
    tree = ast.parse(src)
    complexity = 0
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.For, ast.While, ast.FunctionDef, ast.Lambda)):
            complexity += 1
    return complexity

def calculate_lloc(src):
    tree = ast.parse(src)
    lloc = 0
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            lloc += len(node.body)
        elif isinstance(node, (ast.If, ast.For, ast.While)):
            lloc += 1
    return lloc

def calculate_sloc(src):
    lines = src.split("\n")
    return len([line for line in lines if line.strip()])

def calculate_ploc(src):
    return len(src.split("\n"))

if __name__ == "__main__":
    sys.stdout.write('Enter a Path: ')
    path = input()
    with open(path) as f:
        src = f.read()
        complexity = calculate_complexity(src)
        sloc = calculate_sloc(src)
        ploc = calculate_ploc(src)
        lloc = calculate_lloc(src)
        print(f"complexity: {complexity}")
        print(f"sloc: {sloc}")
        print(f"ploc: {ploc}")
        print(f"lloc: {lloc}")

    b = {}
    a = {}
    a['COMPLEXITY'] = complexity
    a['PLOC'] = ploc
    a['SLOC'] = sloc
    a['LLOC'] = lloc
    b['CC'] = a
    json_cc = json.dumps(b, indent=4)
    with open("cc.json", "w") as outfile:
        outfile.write(json_cc)
    print(json_cc)
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(12, 4))
    ax1.hist(complexity)
    ax1.set_title("Cyclomatic Complexity")
    ax1.set_xlabel("Complexity")
    ax1.set_ylabel("Frequency")
    ax2.hist(sloc)
    ax2.set_title("Source Lines of Code")
    ax2.set_xlabel("Lines of Code")
    ax2.set_ylabel("Frequency")
    ax3.hist(ploc)
    ax3.set_title("Physical Lines of Code")
    ax3.set_xlabel("Lines of Code")
    ax3.set_ylabel("Frequency")
    ax4.hist(lloc)
    ax4.set_title("Logical Lines of Code")
    ax4.set_xlabel("Lines of Code")
    ax4.set_ylabel("Frequency")
    plt.show()