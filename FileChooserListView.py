from kivy.app import App
from  kivy.uix.filechooser import FileChooserListView

class FileChooser(App):
    def build(self):
        fc = FileChooserListView()
        return fc

if __name__ == '__main__':
    FileChooser().run()