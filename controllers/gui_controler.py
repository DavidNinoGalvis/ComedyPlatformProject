from controllers.gestion_controler import  GestionController
from view.main_view import main_admin
from view.main_view import main_event_page

class GUIController:
    def __init__(self):
        self.run_page = 'main'
        self.gestion_controler = GestionController()


    def main(self):
        if self.run_page == 'main':
            #main_admin()
            main_event_page()