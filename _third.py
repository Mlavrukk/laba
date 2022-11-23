import csv
import os
import pathlib
from random import Random, random


class Article:

    def __init__(self):  # по умолчанию
        self.name = None
        self.comment_text = None
        self.rate = None


def create_repo():
    os.mkdir("dataset_copy")
    for i in range(1, 6):
        os.mkdir("dataset_copy/"+str(i))


def save_comments(data, filename):

    for i in range(1, len(data)):

        used_digits = [0]
        random = Random()
        digit = 0

        while digit in used_digits:
            digit = random.randint(1, 10000)

        file = open(filename+f'/{digit:04}'+'.txt', "w", encoding="utf-8")
        file.write(data[i].name)
        file.write('\n')
        file.write(data[i].comment)
        file.close

        used_digits.append(digit)


def write_dataset(dataset):

    one_data = [el for el in dataset if el.mark < 2.0]
    save_comments(one_data, "dataset_copy/1")

    two_data = [el for el in dataset if el.mark < 3.0 and el.mark >= 2.0]
    save_comments(two_data, "dataset_copy/2")

    three_data = [el for el in dataset if el.mark < 4.0 and el.mark >= 3.0]
    save_comments(three_data, "dataset_copy/3")

    four_data = [el for el in dataset if el.mark < 5.0 and el.mark >= 4.0]
    save_comments(four_data, "dataset_copy/4")

    five_data = [el for el in dataset if el.mark == 5.0]
    save_comments(five_data, "dataset_copy/5")


def create_copy(path):
    dataset = get_dataset(path)
    create_repo()
    write_dataset(dataset)


def get_dataset(path):
    dataset = list()
    for folder_num in range(1, 6):

        folder_path = path+'/'+str(folder_num)
        num_of_files = sum(os.path.isfile(os.path.join(folder_path, f))
                           for f in os.listdir(folder_path)) + 1

        for file_num in range(1, num_of_files):
            path_to_file = folder_path+f'/{(file_num):04}'+'.txt'

            try:
                file = open(path_to_file, 'r', encoding='utf-8')
                print(f'{folder_num} : {(file_num):04}')
            except Exception as e:
                print(e.args)

            comment = Article()
            buffer_comment_text = ""
            line_counter = 0
            while True:

                line = file.readline()

                if not line:
                    try:
                        file.close()
                    except Exception as e:
                        print(e.args)
                    break

                if line_counter == 0:
                    comment.name = line
                else:
                    buffer_comment_text += line

                line_counter += 1

            buffer_comment_text = buffer_comment_text.replace(u'\xa0', u' ')

            comment.mark = folder_num
            comment.comment = buffer_comment_text.strip()

            dataset.append(comment)

    return dataset


def get_paths_to_files(path_dataset):

    paths_files = list()

    for folder_num in range(1, 6):
        folder_path = path_dataset+'/'+str(folder_num)

        currentDirectory = pathlib.Path('./dataset_copy'+f'/{folder_num}')
        for currentFile in currentDirectory.iterdir():
            print(currentFile)
            paths_files.append(currentFile)

    return paths_files


def write_as_csv(path_dataset, paths_files):

    with open("dataset_third.csv", "w+", encoding='utf-8', newline='') as file:
        csv_file = csv.writer(file, delimiter=';')
        csv_file.writerow(["Absolute path", "Relative path", "Class"])

        for i in range(0, len(paths_files)):
            paths_files[i] = str(paths_files[i])
            csv_file.writerow([f'{path_dataset + paths_files[i]}',
                              paths_files[i], os.path.basename(paths_files[i])])


if __name__ == '__main__':

    path_dataset = ("C:\\Users\\marGO.LAPTOP-CEGVK39N\\laba\\dataset")

    create_copy(path_dataset)

    path_new_dataset = os.path.abspath("./dataset_copy")
    paths_files = get_paths_to_files(path_new_dataset)

    write_as_csv(path_new_dataset, paths_files)