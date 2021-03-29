# https://stepik.org/lesson/3377/step/3?unit=960
# > python3 my_solution.py arg1 arg2
# arg1 arg2

import sys
for i in range(1, len(sys.argv)):
    print(sys.argv[i], end=' ')
