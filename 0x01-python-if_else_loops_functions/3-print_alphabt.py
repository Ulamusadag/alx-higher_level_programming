#!/usr/bin/python3
for i in range(97, 123):
    i = chr(i)
    if i == "q" or i == "e":
        continue
    else:
        print(f"{i}", end = "")
