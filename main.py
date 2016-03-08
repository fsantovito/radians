import sys
from PySide import QtGui


from models import User
from user_view import UserView
from radians.views.document_view import DocumentView

import logging
logging.basicConfig()

from mongoengine import *
connect('miniluv')


    
def main():

    app = QtGui.QApplication(sys.argv)

    model = User()    
    model.first_name = "Filippo"
    model.last_name = "Santovito"
    model.email = "filippo.santovito@gmail.com"
    
    w = DocumentView(UserView(), model)
    w.show()

    sys.exit(app.exec_())
    
    # model.comments.append(model2)
    # model.save()
    
if __name__ == "__main__":
    main()
