import tkinter
#import tkinter.messagebox

class mygui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        #frame and label
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.label1 = tkinter.Label(self.main_window, 
                                   text = 'FakeSheron')
        self.label2 = tkinter.Label(self.main_window, 
                                   text = 'Blah')
        self.label1.pack(side = 'top')
        self.label2.pack(side = 'top')
        
        self.label3 = tkinter.Label(self.main_window,
                                    text = 'bottom')
        self.label4 = tkinter.Label(self.main_window,
                                    text = 'wow')
        self.label3.pack(side = 'left')
        self.label4.pack(side = 'left')
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        #botton and info box
        self.my_button = tkinter.Button(self.main_window,
                                        text = 'Click me!',
                                        command = self.do_something)
        self.quit_button = tkinter.Button(self.main_window,
                                          text = 'Quit',
                                          command = self.main_window.destroy)
        self.my_button.pack()
        self.quit_button.pack()
        tkinter.mainloop()
    def do_something(self):
        tkinter.messagebox.showinfo('Response',
                                    'Thanks for clicking the button')
myg = mygui()