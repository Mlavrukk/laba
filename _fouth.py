import os


def get_next(rate, id):
    return ("C:\\Users\\marGO.LAPTOP-CEGVK39N\\laba\\dataset"+f'\\{rate}'+f'\\{id:04}.txt')


if __name__ == "__main__":
    rate = 3
    path_dataset = ("C:\\Users\\marGO.LAPTOP-CEGVK39N\\laba\\dataset")
    folder_path = path_dataset + f'/{rate}'

    num_of_files = sum(os.path.isfile(os.path.join(folder_path, f))
                       for f in os.listdir(folder_path)) + 1

    for id in range(1, num_of_files):
        print(get_next(rate, id))