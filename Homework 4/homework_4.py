"""
Program takes the input file, searches for chosen
words, and saves lines in which the words were found in new text files.
"""

import string


def main():
    infile = select_input_files()
    word_list = ['cat', 'House', 'mouse']
    all_lines = infile.readlines()
    positive_results = {}
    line_count = 0
    true_count = 0
    for word in word_list:
        for line in all_lines:
            new_line = line.strip('\n')
            detection, c_true = detect_word(new_line, word)
            true_count += c_true
            positive_results[word] = true_count
            outfile = writing_output_files(word)
            line_count += 1
            if detection:
                print(f'{line_count}. {new_line}')
                print(f'{line_count}. {line}', file=outfile)
        print(f'\nThere are {positive_results[word]} lines with the word {word}.\n')
        line_count = 0
        true_count = 0
    infile.close()
    outfile.close()


def select_input_files():
    infile_name = 'letters_from_a_cat.txt'
    infile = open(infile_name, 'r', encoding='utf-8')
    return infile


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


def writing_output_files(term):
    outfile_name = f'{term}-results.txt'
    outfile = open(outfile_name, 'a', encoding='utf-8')
    return outfile


main()
