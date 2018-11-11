import re
import csv
import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join, abspath

def get_files_list(path ,file_ext_name):
	files_list = [f for f in listdir(path) if (isfile(join(path, f)) and f.endswith("."+file_ext_name))]
	return files_list

def get_csv2dic(path):
	maping_list = []
	with open(path) as fh:
		rd = csv.DictReader(fh, delimiter=',')
		for row in rd:
			maping_list.append(dict(row))
	return maping_list

def get_reName_list(list_in, ele_name):
	list_out = []
	for i in list_in:
		if i[ele_name]:
			list_out.append(re.escape(i[ele_name]))
	return list_out

def get_reMatch_list(pattern, contents, id, type):
	res_list = []
	for r in re.finditer(pattern, contents):
		if r:
			res_list.append([id, r.start(), r.end(), r.group(), type])
	return res_list

def main():
	mypath = abspath('.')
	### get all the txt files name ###
	path_txt = mypath+'/../demo_txt/demo_txt'
	files_txt = get_files_list(path_txt, 'txt')

	### get the keyword of mapping csv list ###
	path_mapping = mypath+'/../demo_mapping_csv'
	files_mapping = [path_mapping+'/'+f for f in ['Compound.csv', 'diease.csv', 'gene.csv']]
	list_comp = get_csv2dic(files_mapping[0])
	list_diea = get_csv2dic(files_mapping[1])
	list_gene = get_csv2dic(files_mapping[2])

	### find the keyword in all txt files
	result = []
	for f_name in files_txt:
		contents = open(path_txt+"/"+f_name, encoding = 'utf8').read()
		id = f_name.replace(".txt","")
	
		for i in get_reName_list(list_comp,'NAME'):
			pattern = i
			r = get_reMatch_list(pattern, contents, id, 'Compound')
			if r:
				result+=(r)
		
		for i in get_reName_list(list_diea,'String'):
			pattern = i
			r = get_reMatch_list(pattern, contents, id, 'diease')
			if r:
				result+=(r)
				
		for i in get_reName_list(list_gene,'name'):
			pattern = i
			r = get_reMatch_list(pattern, contents, id, 'gene')
			if r:
				result+=(r)

	for r in result:
		print(r)

if __name__ == "__main__":
	main()