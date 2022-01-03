# Overview
This program is meant for extraction of data from many PDFs which have the same structure, specifically, that their lines numbers won't change.

Examples - monthly statements, paystubs, insurance claims, etc.

# How to Run

1. Copy the a sample PDF to the PDFs directory
1. Run `generate_parsing_json.py` as follows:
    ```
    ./generate_parsing_json -p pdfs/my-statement.pdf > parsing_jsons/statements.json
    ```
1. Manually edit the generated `statements.json` file as follows:
   * Remove any entries that you don't care about parsing or asserting
   * Keep intact those that you want to assert. Asserting is used as a safety check to ensure things that the structure of the document (i.e. the line numbers where things are at) hasn't changed.
   * Add a meaningful `name` that's a valid python variable name for each of the entries you want to extract.
   * Remove the `assert_value` for each of the entries you want to extract.
1. Run `extract_pdf.py` as follows:
    ```
    ./extract_pdf.py -p pdfs/my-statement.pdf -j parsing_jsons/statements.json > outputs/my-statement.json
    ```
1. You can then write a bash script to do this for all files in the `pdfs` folder. *I should later modifh `extract_pdf` to support input and output directories as parameters.*


