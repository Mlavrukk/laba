import csv
import os
import shutil


def write_to_file(path_dataset, paths_files):

    with open("dataset_second.csv", "w+", encoding='utf-8', newline='') as file:
        csv_file = csv.writer(file, delimiter=';')
        csv_file.writerow(["Absolute path", "Relative path", "Class"])

        for path in paths_files:
            path = path[0:2] + '_' + path[3:] #raplce / with _
            csv_file.writerow([f'{path_dataset+path}',
                              f'dataset{path}', f'{path[1]}'])


def mk_newdataset(nd_path):
    os.mkdir(nd_path)


def copy_dataset(path_dataset):

    nd_path='./new_dataset'
    mk_newdataset(nd_path)

    for folder_num in range(1,6):

        folder_path = path_dataset+'/'+str(folder_num) #path to current folder (mark 1-5)

        num_of_files = sum(os.path.isfile(os.path.join(folder_path, f)) #amount of files in current folder
                           for f in os.listdir(folder_path)) + 1

        for file_num in range(0, (num_of_files - 1)):
            shutil.copy(folder_path+f"/{(file_num+1):04}.txt", nd_path) #rewrite
            os.rename(f"./new_dataset/{(file_num+1):04}.txt", f"./new_dataset/{folder_num}_{(file_num+1):04}.txt") #rename
    
    return nd_path


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

    path_dataset = ("C:\\Users\\marGO.LAPTOP-CEGVK39N\\laba\\dataset")
    paths_files = get_paths_to_files(path_dataset)

    new_dataset_path = copy_dataset(path_dataset)

    write_to_file(new_dataset_path, paths_files)
