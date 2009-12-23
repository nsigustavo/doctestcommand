from glob import glob
import doctest
import os
import sys


def doctest_runner():
    sys.path = [package(os.getcwd())] + sys.path 
    files = sys.argv[1:] or list_doc_test(dir=os.getcwd())
    for file in files:
        file_path = os.path.join(os.getcwd(), file)
        print file_path, "\n",doctest.testfile(file_path,optionflags=doctest.REPORT_ONLY_FIRST_FAILURE + doctest.ELLIPSIS, module_relative=False), "\n"


def list_doc_test(dir):
    tests = []
    for item in os.listdir(dir):
        path = os.path.join(dir, item)
        if item.endswith('.dt'):
            tests.append(path)
        elif os.path.isdir(path):
            tests += list_doc_test(path)
    return tests


def package(dir):
    last_dir = os.path.dirname(dir)
    init = os.path.join(dir, '__init__.py')
    last_init = os.path.join(last_dir, '__init__.py')
    if os.path.isfile(last_init) == False and os.path.isfile(init) == False:
        return dir
    else:
        return package(last_dir)



