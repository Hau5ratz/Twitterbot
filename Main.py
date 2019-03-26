#!/usr/bin/env python

#!/usr/bin/env python

import twitter
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox, filedialog
from tkinter import ttk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #Secret key variable !
        # self.consumer_key
        # self.consumer_secret
        # self.access_token
        # self.access_token_secret
        #Secret key variable !
        self.args = []
        #self.iconbitmap('mc_vrt_opt_pos_63_1x.ico')
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageHelp):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.resizable(width=False, height=False)
        self.show_frame("StartPage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        #print(self.winfo_height())
        #print(self.winfo_width())
        frame = self.frames[page_name]
        frame.tkraise()
        frame.load()
        if page_name == 'StartPage':
            self.geometry('{}x{}'.format(340, 85))
        elif page_name == 'PageOne':
            self.geometry('{}x{}'.format(388, 184))
        elif page_name == 'PageTwo':
            self.geometry('{}x{}'.format(295, 70))
        elif page_name == 'PageThree':
            self.geometry('{}x{}'.format(350, 70))
        elif page_name == 'PageFour':
            self.geometry('{}x{}'.format(150, 90)) # need to adjust dimensions

        elif page_name == 'PageHelp':
            self.geometry('{}x{}'.format(685, 465))
        
class Page(tk.Frame):

    def set_text(self, e, text=''):
        e.delete(0, 'end')
        e.insert(0, text)

    def frequest(self, message=None):
        if message:
            messagebox.showinfo('File request', message)
        filepath = filedialog.askopenfilename()
        if filepath == '':
            messagebox.showwarning("Warning",
                                   "No File path specified")
        else:
            return filepath

class StartPage(Page):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def load(self):
        label = tk.Label(self, text="Welcome to the twitter manager",
                         font=self.controller.title_font)
        label.grid(row=0, column=0, sticky="N")


        button1 = tk.Button(self, text="Start up",
                            command=lambda: self.controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Help",
                            command=lambda: self.controller.show_frame("PageHelp"))
        button1.grid(row=2, column=0, sticky='EW')
        button2.grid(row=1, column=0)



class PageOne(Page):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.wm_title("Twitter account info Form")

    def load(self):
        boolvar = tk.BooleanVar()
        boolvar.set(False)
        # Title
        title = tk.Label(self, text="Please fill out the following account information:",
                         font=self.controller.title_font)
        title.grid(row=0, column=0, sticky="N", columnspan=3)

        # Info label
        label = tk.Label(self, text="Lori ipsum:",
                         anchor='w')
        label.grid(row=1, column=0, sticky='EW', columnspan=3)

        # Row 1:
        label1 = tk.Label(self, text="The consumer key",
                          anchor='w')
        entry1 = tk.Entry(self)

        # Attach
        label1.grid(row=2, column=0, sticky='EW')
        entry1.grid(row=2, column=1, sticky='EW')

        # Row 2:
        label2 = tk.Label(self, text="The consumer secret)", anchor='w')
        entry2 = tk.Entry(self)
        # Attach
        label2.grid(row=3, column=0, sticky='EW')
        entry2.grid(row=3, column=1, sticky='EW')

        # Row 3:
        label3 = tk.Label(self, text="The access token",
                          anchor='w')
        entry3 = tk.Entry(self)
        # Attach
        label3.grid(row=4, column=0, sticky='EW')
        entry3.grid(row=4, column=1, sticky='EW')


        # Row 4:
        label4 = tk.Label(self, text="access_token_secret",
                          anchor='w')
        entry4 = tk.Entry(self)
        # Attach
        label4.grid(row=5, column=0, sticky='EW')
        entry4.grid(row=5, column=1, sticky='EW')

                # load defaults
        if os.path.isfile('data.txt'):
            with open("data.txt",'r') as file:
                e, lines = [entry1, entry2, entry3], file.readlines()
                [self.set_text(e[l], lines[l][:-1]) for l in range(len(lines))]

        # Row 4 w/ Check mark
        label5 = tk.Label(self,
                          text="Assume Group names contain desired number? : ",
                          anchor='w')
        #Check = tk.Checkbutton(self, text='Assume?', variable=boolvar)
        #Check.select()

        #Check.grid(row=5, column=2, sticky='E')
        label5.grid(row=5, column=0, columnspan=2, sticky='EW')

        # Enter button
        button5 = tk.Button(self, text="Enter info",
                            command=lambda: self.pfeed([entry1.get(), entry2.get(), entry3.get(), boolvar.get()]))
        button5.grid(row=6, column=0, columnspan=3, sticky='EW')


'''
consumer_key
consumer_secret
access_token
access_token_secret
api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)

'''

