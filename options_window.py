from PyQt6.QtWidgets import QWidget

from config import JUNK_RULES
from generated.options import Ui_Dialog

class OptionsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setup_checkbox(self.ui.checkBox, JUNK_RULES["files_exact"], ".DS_Store")
        self.setup_checkbox(self.ui.checkBox_2, JUNK_RULES["files_prefix"], "._")
        self.setup_checkbox(self.ui.checkBox_3, JUNK_RULES["dirs_exact"], ".Spotlight-V100")
        self.setup_checkbox(self.ui.checkBox_4, JUNK_RULES["dirs_exact"], ".Trashes")
        self.setup_checkbox(self.ui.checkBox_5, JUNK_RULES["dirs_exact"], ".fseventsd")

        self.ui.closeButton.clicked.connect(self.on_close_button_clicked)

    def setup_checkbox(self, checkbox, rule, key):
        checkbox.setChecked(rule.get(key, False))
        checkbox.stateChanged.connect(lambda state: self.update_rule(rule, key, state))

    def update_rule(self, rule_dict, key, state):
        rule_dict[key] = bool(state)

    def on_close_button_clicked(self):
        self.close()