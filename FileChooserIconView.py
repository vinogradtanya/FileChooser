from kivy.app import App
from  kivy.uix.filechooser import FileChooserIconView

class FileChooser(App):
    def build(self):
        fc = FileChooserIconView()
        return fc

if __name__ == '__main__':
    FileChooser().run()