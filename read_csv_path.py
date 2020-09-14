from PyQt5.QtWidgets import QFileDialog


def chose_csv_file(MainWindow):
    filterTypes = 'comma-separated values Csv (*.csv);; Python (*.py);; Text Document(*.txt)'
    path, _ = QFileDialog.getOpenFileName(
        parent=MainWindow,
        caption='Open file',
        directory='',
        filter=filterTypes
    )

    if path:
        try:
            with open(path, 'r') as f:
                text = f.read()
                f.close()
        except Exception as e:
            MainWindow.dialog_message(str(e))
        else:

            return path
