"""
This program:
1. Loads data as JSON.
2. Joins ingredients from a list into a string.
3. Counts number of ingredients per recipe.
4. Sorts all dictionaries within a list by the 'id' key in ascending order.
4. Writes out a new file as CSV.
"""

import json
import csv
import operator


def main():
    data_directory = 'data'
    infile_name = 'ingredients.json'
    outfile_name = 'ingredients_transformed.csv'
    infile = file_read(data_directory, infile_name)
    outfile = file_write(data_directory, outfile_name)
    data = processing(infile)
    fieldnames = data[0].keys()  # Python for Everybody - I went through the chapters with lists and dictionaries to
    # refresh my memory on how to operate on those structures
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)  # Geeks for Geeks - I was looking for different ways to
    # create my csv file and this resource gave me an idea for my project
    writer.writeheader()
    for i in data:
        writer.writerow(i)
    infile.close()
    outfile.close()


def file_read(data_directory, infile_name):
    infile_path_and_name = f'{data_directory}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    return infile


def processing(infile):
    data = json.load(infile)        # Python for Everybody - as in the previous example, I used this resource
    # to refresh my memory on how to work with json files
    for i in data:
        ingredients_list = i['ingredients']
        i['num_of_ingredients'] = len(ingredients_list)
        ingredients_string = ', '.join(ingredients_list)    # Python Documentation, Simplilearn - I forgot how to use .join()
        # function, so first I found Simplilearn where they went over that topic, after that I went to Python Documentation to confirm it
        i['ingredients'] = ingredients_string
    data = sorted(data, key=operator.itemgetter('id'))  # Stack Overflow - I forgot how to use sorted function and I
    # found a very helpful discussion on Stack Overflow where they discussed that and related topics
    return data


def file_write(data_directory, outfile_name):
    outfile_path_and_name = f'{data_directory}/{outfile_name}'
    outfile = open(outfile_path_and_name, 'w', encoding='utf-8')
    return outfile


main()
