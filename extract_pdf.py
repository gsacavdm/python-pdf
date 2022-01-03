parsing_json_path = 'parsing_jsons/paystub.json'
pdf_path = 'pdfs/2021-12-31.pdf'

from pdfminer.high_level import *
import json

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
