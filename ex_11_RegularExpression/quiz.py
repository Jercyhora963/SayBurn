#What will the following program print? :

import re

s = 'A message from csev@umich.edo to cwen@iupui.edu about meeting @2pm'
lst = re.findall('\\S+@\\S+', s)
print(lst)
