from itertools import count


fhand = open('mbox-short.txt')
for line in fhand:
   line = line.rstrip()

   count = 0
   if line.startswith('From:'):
      count = count + 1
      line = line.split()
      for z in line:
         z = z.split('.')
         print(z, count)