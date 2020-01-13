from os import listdir
from os.path import join


def Choice():
    print("*" * 30)
    print("Press 1 : to enter DataSet path \nEles press any number \n")
    choice = int(input("Enter your choice : "))

    return choice


def CreateWholeDataSetFile():
    if Choice() == 1:
        path = input("Enter the DataSet path : ")
    else:
        path = "train"

    create_file = open("whole_dataset.txt", "w", encoding="utf8")

    for file in listdir(path):
        temp_file = open(join(path, file), "r", encoding="utf8")
        create_file.write(temp_file.read())
        temp_file.close()

    create_file.close()


if __name__ == "__main__":
    CreateWholeDataSetFile()
    open_whole_dataset_file = open("whole_dataset.txt", "r", encoding="utf8")
    print(len(open_whole_dataset_file.readlines()))
