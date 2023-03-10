# -*- coding: utf-8 -*-
"""splitFiles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1to7IFWTnbLG1IpfOgJ-tWrGM1FD8DatC
"""

#This code splits the domain list into smaller files 

from datetime import date

#number of domains in each file
lines_per_file = 250
file_path = '/home/domains/'
today = date.today().strftime("%Y-%m-%d")
dir = file_path + "domain-names.txt"
smallfile = None
with open(dir) as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(file_path + 'small_files/' + small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()