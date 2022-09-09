#!/usr/bin/python3
for lower in range(97, 122):
      if lower == ord('q')  or lower == ord('e'):
         continue
      print("{:c}".format(lower), end="")
