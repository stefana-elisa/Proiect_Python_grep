import os
import sys
import argparse
import re


def grep():
    parser = argparse.ArgumentParser(description="Grep copy")
    parser.add_argument("regex", type=str, help="the regular expression to search for")
    parser.add_argument("path", type=str, help="the file in which to search")
    parser.add_argument("-r", dest="recursive", action="store_true", help="search recursively")
    parser.add_argument("-not", dest="not_in_file", action="store_true", help="not in file")
    parser.add_argument("-count", dest="count", action="store_true", help="count appearances in file")
    parser.add_argument("-ignoreCase", dest="ignoreCase", action="store_true", help="ignore the case of the regex")
    args = parser.parse_args()
    regex = re.compile(args.regex)

    if args.recursive == True:
        if args.ignoreCase == True:
            for root, dirs, files in os.walk(args.path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    for line in open(file_path, "r"):
                        if re.search(args.regex, line, re.IGNORECASE):
                            sys.stdout.write(file_name + "\n")
                            break
        else:
            for root, dirs, files in os.walk(args.path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    for line in open(file_path, "r"):
                        if regex.search(line):
                            sys.stdout.write(file_name + "\n")
                            break

    else:
        if args.not_in_file == True:
            found = False
            for line in open(args.path, "r"):
                if args.ignoreCase == True:
                    if re.search(args.regex, line, re.IGNORECASE):
                        found = True
                        sys.stdout.write("expression found in file")
                        break
                else:
                    if regex.search(line):
                        found = True
                        sys.stdout.write("expression found in file")
                        break
            if found == False:
                    sys.stdout.write("expression NOT found in file")
        else:
            count = 0
            for line in open(args.path, "r"):
                if args.ignoreCase == True:
                    if re.search(args.regex, line, re.IGNORECASE):
                        if args.count == True:
                            for word in line.split():
                                if re.match(args.regex, word, re.IGNORECASE):
                                    count = count + 1
                        else:
                            sys.stdout.write(line)
                else:
                    if regex.search(line):
                        if args.count == True:
                            for word in line.split():
                                if regex.match(word):
                                    count = count + 1
                        else:
                            sys.stdout.write(line)
            if args.count == True:
                sys.stdout.write(str(count))

if __name__ == '__main__':
    grep()

