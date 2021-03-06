import json, sys, time
from pprint import pprint

absolute_path = sys.argv[1]
file_json = '%s/5-ep-cluster-dump.json' % absolute_path
output_file_json = "%s/output-ep.json" % absolute_path

string_sh = """}
{"""

with open(file_json) as f:
	data = f.read()
	data_list = data.split(string_sh)
	file = open("bkp/output-ep.json","w") 
	for index, d in enumerate(data_list):
		index_list = index + 1
		if index_list == len(data_list):
			json_str = "{\n%s" % d
			data_json = json.loads(json_str)
			if data_json["subsets"]:
				file.write(json_str) 
		elif index == 0:
			json_str = "%s\n}" % d
			data_json = json.loads(json_str)
			if data_json["subsets"]:
				file.write(json_str) 
		else:
			file.write("\n")
			json_str = "{\n%s\n}" % d
			data_json = json.loads(json_str)
			if data_json["subsets"]:
				file.write(json_str)
	file.close() 