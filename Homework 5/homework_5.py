"""
Program takes the input file, searches for chosen
words, and saves lines in which the words were found in new text files.
"""

import json
import string


def main():
    infile, file_name = select_input_files()
    word_list = ['cat', 'House', 'mouse']
    all_lines = infile.readlines()
    positive_results = {
        'file_name': file_name,
        'num_terms': len(word_list)
    }
    line_count = 0
    true_count = 0
    for word in word_list:
        positive_results[word] = {}
        matches_lines = []
        for line in all_lines:
            new_line = line.strip('\n')
            detection, c_true = detect_word(new_line, word)
            true_count += c_true
            outfile = writing_output_files()
            line_count += 1
            if detection:
                matches_lines.append(new_line)
                positive_results[word] = {
                    'count': true_count,
                    'lines': matches_lines
                }
        line_count = 0
        true_count = 0
    json_object = json.dumps(positive_results, indent=4)
    outfile.write(json_object)
    infile.close()
    outfile.close()

    json_file = read_json()
    print(json_file)


def select_input_files():
    infile_name = 'letters_from_a_cat.txt'
    infile = open(infile_name, 'r', encoding='utf-8')
    return infile, infile_name


def detect_word(line, search_term):
    search_term = search_term.lower()
    line = line.lower()
    line_list = line.split(' ')
    cleaned_list = []
    for word in line_list:
        cleaned_list.append(word.strip(string.punctuation))
    count_true = 0
    if search_term in cleaned_list:
        result = True
        count_true += 1
    elif search_term not in cleaned_list:
        result = False
    else:
        print('Error')

    return result, count_true


def writing_output_files():
    outfile = open('term_results.json', 'a', encoding='utf-8')
    return outfile


def read_json():
    infile = open('term_results.json', 'r')
    file = json.load(infile)
    return file


main()
