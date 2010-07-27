import doctest
import os
import sys
from termcolor import colored

def doctest_runner():
    exec_path = os.getcwd()
    sys.path.append(exec_path)
    files = sys.argv[1:] or list_doc_test(dir=os.getcwd())
    for file in files:
        file_path = os.path.join(exec_path, file)
        if file.startswith(exec_path):
            relative_path = file[len(exec_path):]
        else:
            relative_path = exec_path
        test_result = doctest.testfile(
                    file_path,
                    optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
                               +doctest.ELLIPSIS,
                    module_relative=False)
        result_text = "%-50.50s#%s"%(
                relative_path,
                test_result
                )
        if int(test_result.failed) == 0:
            print colored(result_text, 'green')
        else:
            print colored(result_text, 'red')
            print 

def list_doc_test(dir):
    tests = []
    for item in os.listdir(dir):
        path = os.path.join(dir, item)
        if item.endswith('.dt'):
            tests.append(path)
        elif os.path.isdir(path):
            tests += list_doc_test(path)
    return tests



