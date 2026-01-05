from pathlib import Path
from typing import List
import shutil

from PyQt6.QtWidgets import QFileDialog, QMessageBox, QWidget

from generated.dialog import Ui_Dialog
from options_window import OptionsWindow
from utilities.junk_searcher import get_junks

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.options_window = OptionsWindow()

        self.selected_path = ""
        self.files: List[Path] = []
        self.dirs: List[Path] = []

        self.ui.findButton.setDisabled(True)
        self.ui.cleanButton.setDisabled(True)

        self.ui.selectFolderButton.clicked.connect(self.on_select_folder_button_clicked)
        self.ui.findButton.clicked.connect(self.on_find_button_clicked)
        self.ui.cleanButton.clicked.connect(self.on_clean_button_clicked)
        self.ui.optionsButton.clicked.connect(self.on_options_button_clicked)

    def on_select_folder_button_clicked(self):
        selected_path = QFileDialog.getExistingDirectory(self, "Select a folder", "")
        if selected_path:
            self.ui.textBrowser.clear()
            self.ui.label.setText(selected_path.__str__())
            self.ui.findButton.setDisabled(False)
            self.selected_path = selected_path

    def on_find_button_clicked(self):
        if not Path(self.selected_path).exists():
            QMessageBox.warning(self, "Warning", "Folder not found!")
            return
        self.files, self.dirs = get_junks(Path(self.selected_path))
        self.ui.textBrowser.clear()
        for file in self.files:
            self.ui.textBrowser.append(file.__str__())
        for directory in self.dirs:
            self.ui.textBrowser.append(directory.__str__())
        if self.files and self.dirs:
            self.ui.cleanButton.setDisabled(False)
        else:
            self.ui.textBrowser.setText("Nothing was found")

    def on_clean_button_clicked(self):
        for file in self.files:
            try:
                if file.exists() and file.is_file():
                    file.unlink()
            except Exception as e:
                self.ui.textBrowser.append(str(e))
        for directory in self.dirs:
            if directory.exists() and directory.is_dir():
                shutil.rmtree(directory)
        self.ui.textBrowser.setText("Done")

    def on_options_button_clicked(self):
        self.options_window.show()