from PySide import QtGui
from user_template import Ui_Form

class UserView(QtGui.QWidget):

    def __init__(self, *args, **kwargs):
        super(UserView, self).__init__(*args, **kwargs)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

