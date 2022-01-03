parser_path = 'parsing_jsons/paystub_new.json'
pdf_path = 'pdfs/2021-12-31.pdf'

from pdfminer.high_level import *
import json

raw_text = extract_text(pdf_path)
raw_lines = raw_text.split('\n')

outputs = []
for i, line in enumerate(raw_lines):
  if (line):
    output = {}
    output['index'] = i
    output['name'] = 'TBD'
    output['assert_value'] = line
    outputs.append(output)

outputs_as_string = json.dumps(outputs, indent=2)

print(outputs_as_string)
