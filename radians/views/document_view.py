# encoding: utf-8

from PySide import QtGui
from miniluv.viewmodel import ViewModel
from document_template import Ui_MainWindow

class DocumentView(QtGui.QMainWindow):

    def __init__(self, view, model, *args, **kwargs):
        super(DocumentView, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(view)
        
        self.ui.action_salva_documento.triggered.connect(self.salva_documento)
        self.ui.action_elimina_documento.triggered.connect(self.elimina_documento)
        
        self.model = model
        self.view_model = ViewModel(model)
        self.view = view
        self.view_model.add_view(self.view)

    def salva_documento(self):
        try:
            self.model.save()
        except Exception as e:
            QtGui.QMessageBox.critical(self, "salvataggio documento", e.args[0])
        else:
            QtGui.QMessageBox.information(self, "salvataggio documento", u"il documento è stato salvato correttamente")
   
    def elimina_documento(self):
        raise NotImplementedError()        
