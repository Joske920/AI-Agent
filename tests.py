from calculator.functions.get_files_info import get_files_info
from calculator.functions.get_file_content import get_file_content
from calculator.functions.write_file_content import write_file
from calculator.functions.run_python_file import run_python_file

def tests():
    print(get_files_info({'directory': '.'}))

    #print(get_files_info('calculator', 'pkg'))

    #print(run_python_file("calculator", "main.py"))
    #print(run_python_file("calculator", "main.py", ["3 + 5"]))
    #print(run_python_file("calculator", "tests.py"))

    #print(run_python_file("calculator", "../main.py"))
    #print(run_python_file("calculator", "nonexistent.py"))
    #print(run_python_file("calculator", "lorem.txt"))
    
if __name__ == "__main__":
    tests()