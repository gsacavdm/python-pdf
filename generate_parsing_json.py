#!python3

import sys
import argparse

from pdfminer.high_level import *
import json

parser = argparse.ArgumentParser(description='Generate the parser json for the extract_pdf script.')
parser.add_argument('--pdf', '-p', dest='pdf_path', help='path to the pdf', required=True)

args = parser.parse_args()
pdf_path = args.pdf_path

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
