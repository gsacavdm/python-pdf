#!python3

import sys 
import argparse

from pdfminer.high_level import *
import json

parser = argparse.ArgumentParser(description='Extract contents as json based on json-based parser definition.')
parser.add_argument('--pdf', '-p', dest='pdf_path', help='path to the pdf', required=True)
parser.add_argument('--json', '-j', dest='parsing_json_path', help='path to the json-based parser definition', required=True)

args = parser.parse_args()

parsing_json_path = args.parsing_json_path
pdf_path = args.pdf_path

raw_text = extract_text(pdf_path)
raw_lines = raw_text.split('\n')

lines_to_extract = json.load(open(parsing_json_path))

output = {}

for line_to_extract in lines_to_extract:
	index = line_to_extract["index"]
	name = line_to_extract["name"]
	assert_value = "" if "assert_value" not in line_to_extract else line_to_extract["assert_value"]

	value = raw_lines[index]
	if not(assert_value):
		output[name]=value
	elif (assert_value and assert_value != value):
		raise Exception(f'Assert value does not match actual value. index={index} field={name} assert_value={assert_value} value={value}')

output_as_string = json.dumps(output, indent=2)
print(output_as_string)
