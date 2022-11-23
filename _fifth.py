import os


class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __get_next__(self, mark):
        if (self.counter >= self.limit):
            return None
        self.counter += 1
        return ("C:\\Users\\marGO.LAPTOP-CEGVK39N\\laba\\dataset"+f'\\{mark}'+f'\\{self.counter:04}.txt')

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration


if __name__ == "__main__":
    mark = 4
    path_to_dataset = ("C:\\Users\\marGO.LAPTOP-CEGVK39N\\laba\\dataset")
    folder_path = path_to_dataset + f'\\{mark}'

    num_of_files = sum(os.path.isfile(os.path.join(folder_path, f))
                       for f in os.listdir(folder_path)) + 1

    iter = SimpleIterator(num_of_files)
    for i in range(1, 5):
        print(iter.__get_next__(mark))