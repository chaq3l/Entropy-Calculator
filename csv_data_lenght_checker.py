from PyQt5.QtWidgets import QFileDialog

from read_csv_path import chose_csv_file
import pandas as pd
import os.path
import glob


def chose_file(MainWindow):

    path = chose_csv_file(MainWindow)
    if path:
        make_list_of_files_in_folder(path)
    else:
        pass


def make_list_of_files_in_folder(path):

    head, tail = os.path.split(path)

    list_of_files_in_directory = glob.glob(str(head) + "/*.csv")
    # print(glob.glob(str(head) + "/*.csv"))
    all_files_names = []
    all_files_length = []
    for file in list_of_files_in_directory:
        df = pd.read_csv(file, header=None)
        single_file_head, single_file_tail = os.path.split(file)
        all_files_names.append(single_file_tail)
        all_files_length.append(len(df[[0]].values))
        # print(str(single_file_tail)+" length: " + str(len(df[[0]].values)))

    first_row = all_files_length[0]
    the_rest_rows = all_files_length[1:]

    max_length = max(all_files_length)
    min_length = min(all_files_length)


    output_path, sheet_name = os.path.split(head)

    output_path, localization_to_name_of_output_file = os.path.split(output_path)

    #output_path = output_path + '/file length results.xlsx'
    output_path = str(output_path) + '/file length results ' + str(sheet_name) \
                        + ' '+ str(localization_to_name_of_output_file)\
                        + '.xlsx'


    df1 = pd.DataFrame([min(all_files_length), max(all_files_length)],

                        index = ['min', 'max'],

                        columns = [localization_to_name_of_output_file])

    # df2 = pd.DataFrame([[min_length, max_length,first_row, ], *the_rest_rows],
    #
    #                    index=[*all_files_names],
    #
    #                    columns=['files length', 'min length', 'max length'])

    df2 = pd.DataFrame([*all_files_length],

                       index=[*all_files_names],

                       columns=['files length'])

    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    df1.to_excel(writer, sheet_name=sheet_name)
    df2.to_excel(writer, sheet_name='min and max length')
    writer.save()




