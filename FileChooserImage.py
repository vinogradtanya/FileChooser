from kivy.app import App
from  kivy.uix.filechooser import FileChooserIconView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        filechooser = GridLayout(cols = 2)
        fc = FileChooserIconView()
        im = Image()
        def selected(instance, filename):
            try:
                im.source = filename[0]
            except:
                pass
        fc.bind(selection = selected)
        filechooser.add_widget(fc)
        filechooser.add_widget(im)
        return filechooser

if __name__ == '__main__':
    MyApp().run()