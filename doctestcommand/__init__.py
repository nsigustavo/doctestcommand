import doctest
import os
import sys

def doctest_runner():
    exec_path = os.getcwd()
    sys.path.append(exec_path)
    files = sys.argv[1:] or list_doc_test(dir=os.getcwd())
    for file in files:
        file_path = os.path.join(exec_path, file)
        if file.startswith(exec_path):
            relative_path = file[len(exec_path):]
        print "%-50.50s#%s"%(
                    relative_path,
                    doctest.testfile(
                        file_path,
                        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
                                   +doctest.ELLIPSIS,
                        module_relative=False))


def list_doc_test(dir):
    tests = []
    for item in os.listdir(dir):
        path = os.path.join(dir, item)
        if item.endswith('.dt'):
            tests.append(path)
        elif os.path.isdir(path):
            tests += list_doc_test(path)
    return tests



