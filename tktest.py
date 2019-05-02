import tkinter
#import tkinter.messagebox

class mygui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        #frame and label
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.label1 = tkinter.Label(self.top_frame, 
                                   text = 'Enter a distance in kilo')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width = 10)
        
        self.label1.pack(side = 'left')
        self.kilo_entry.pack(side = 'top')
        
        self.label3 = tkinter.Label(self.main_window,
                                    text = 'bottom')
        self.label4 = tkinter.Label(self.main_window,
                                    text = 'wow')
        self.label3.pack(side = 'left')
        self.label4.pack(side = 'left')
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        #botton and info box
        self.calc_button = tkinter.Button(self.bottom_frame,
                                        text = 'Convert',
                                        command = self.convert)
        self.quit_button = tkinter.Button(self.main_window,
                                          text = 'Quit',
                                          command = self.main_window.destroy)
        self.my_button.pack()
        self.quit_button.pack()
        tkinter.mainloop()
    def convert(self)
    def do_something(self):
        tkinter.messagebox.showinfo('Response',
                                    'Thanks for clicking the button')
myg = mygui()