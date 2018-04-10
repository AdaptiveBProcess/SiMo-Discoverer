# -*- coding: utf-8 -*-
from sys import stdout
import numpy as np
import datetime
import os
import csv


#printing process functions
def print_progress(percentage, text):
	stdout.write("\r%s" % text + str(percentage)[0:5] + chr(37) + "...      ")
	stdout.flush()

def print_done_task():
	stdout.write("[DONE]")
	stdout.flush()
	stdout.write("\n")

def file_size(path_file):
	size = 0
	file_exist = os.path.exists(path_file)
	if file_exist:
		size = len(open(path_file).readlines())
	return size

#printing formated float
def ffloat(num, dec):
	return float("{0:.2f}".format(np.round(num,decimals=dec)))

#transform a string into date object
def get_time_obj(date, timeformat):
	date_modified = datetime.datetime.strptime(date,timeformat)
	return date_modified

#reduce list of lists with no repetitions
def reduce_list(input):
	text = str(input).replace('[', '').replace(']', '')
	temp_list = list()
	for number in text.split(','):
		temp_list.append(int(number))
	return list(set(temp_list))

#print debuging csv file
def create_csv_file(index, output_file):
	file_exist = os.path.exists(output_file)
	with open(output_file, 'w') as f:
		fieldnames = index[0].keys()
		w = csv.DictWriter(f, fieldnames)
		w.writeheader()
		for element in index:
			w.writerow(element)
		f.close()

# rounding lists values preserving the sum values
def round_preserve(l,expected_sum):
	actual_sum = sum(l)
	difference = round(expected_sum - actual_sum,2)
	if difference > 0.00:
		idx= l.index(min(l))
	else:
		idx= l.index(max(l))
	l[idx] +=difference
	return l
