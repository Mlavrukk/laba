import csv
import os


def write_to_file(path_dataset, paths_files):

    with open("dataset_first.csv", "w+", encoding='utf-8', newline='') as file:
        csv_file = csv.writer(file, delimiter=';')
        csv_file.writerow(["Absolute path", "Relative path", "Class"])

        for i in range(0, len(paths_files)):
            csv_file.writerow([f'{path_dataset+paths_files[i]}',
                              f'dataset{paths_files[i]}', f'{paths_files[i][1]}'])


def get_paths_to_files(path_dataset):

    paths_files = list()

    for folder_num in range(1, 6):
        folder_path = path_dataset+'/'+str(folder_num)
        num_of_files = sum(os.path.isfile(os.path.join(folder_path, f))
                           for f in os.listdir(folder_path)) + 1

        for file_num in range(1, num_of_files):
            path_to_file = folder_path+f'/{(file_num):04}'+'.txt'
            print(f'{folder_num} : {(file_num):04}')
            paths_files.append(path_to_file[len(path_dataset):])

    return paths_files


if __name__ == '__main__':

    path_dataset =("C:\\Users\\marGO.LAPTOP-CEGVK39N\\laba\\dataset")
    paths_files = get_paths_to_files(path_dataset)

    write_to_file(path_dataset, paths_files)
