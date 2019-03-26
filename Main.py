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
        self.consumer_key =0
        self.consumer_secret =0
        self.access_token =0
        self.access_token_secret =0
        # Secret key variable !

        # User info
        self.user_id = 0
        self.user_location = 0
        self.username = 0


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
        if os.path.isfile('usrdata.cache'):
            with open("usrdata.cache",'r') as file:
                e, lines = [entry1, entry2, entry3, entry4], file.readlines()
                [self.set_text(e[l], lines[l][:-1]) for l in range(len(lines))]



        # Enter button
        button5 = tk.Button(self, text="Verify info",
                            command=lambda: self.pfeed([entry1.get(), entry2.get(), entry3.get(), entry4.get()]), self.controller)
        button5.grid(row=6, column=0, columnspan=3, sticky='EW')

    def pfeed(self, lin, controller):
        confirmation = self.verify(lin, controller)
        if confirmation:
            with open("usrdata.cache",'w') as file:
                [file.write(line+'\n') for line in lin[:-1]]
            controller.consumer_key = lin[0]
            controller.consumer_secret = lin[1]
            controller.access_token = lin[2]
            controller.access_token_secret = lin[3]
            controller.user_id = confirmation["id"]
            controller.user_location = confirmation["location"]
            controller.username = confirmation["name"]
            messagebox.showinfo('Confirmation validated', "Your information was validated!")
            self.controller.show_frame("PageTwo")
        else:
            messagebox.showwarning("Warning","Credientials not valid please try again.")



    def verify(self, lin, controller):
        # Test data
        return {"id": 16133, "location": "Philadelphia", "name": "bear"}
        '''
        try:
            controller.api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)
            return controller.api.VerifyCredentials()

        except Exception as ex:
            messagebox.showwarning("Warning","Exception occured \n Trace:\n %s"%ex)
        '''

class PageTwo(Page):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.wm_title("Selection of post details file")

    def load(self):

        # Row 1:
        label1 = tk.Label(self, text="The excel file (.xlsx)",
                          anchor='w')
        entry1 = tk.Entry(self)
        button1 = tk.Button(self, text="Browse",
                            command=lambda: self.set_text(entry1,
                                                          self.frequest()))
        # Attach
        label1.grid(row=2, column=0, sticky='EW')
        entry1.grid(row=2, column=1, sticky='EW')
        button1.grid(row=2, column=2, sticky='EW')

        # load defaults
        if os.path.isfile('data.txt'):
            with open("data.txt",'r') as file:
                e, lines = [entry1], file.readlines()
                [self.set_text(e[l], lines[l][:-1]) for l in range(len(lines))]
                    
        self.controller.bot = Excel_bot(self.controller.argv)
        self.controller.ebot = self.controller.bot.wb
        label = ttk.Label(self,
            text="Please select one the available sheets to pull data from:",
            anchor='w')
        self.listbox = ttk.Combobox(self,
            values=self.controller.ebot.get_sheet_names(),
            state='readonly')


        button = tk.Button(self, text="continue",
                            command=lambda: self.contincheck())
        

        button.grid(row=3, column=1, sticky='EW')
        label.grid(row=1, column=0, sticky='EW', columnspan=3)
        self.listbox.grid(row=2, column=0, sticky='EW', columnspan=3)

    def contincheck(self):
        if self.listbox.get():
            self.controller.sheetname = self.listbox.get()
            self.controller.show_frame("PageThree")
        else:
            messagebox.showwarning("Warning","No sheet specified")

    def pfeed(self, lin):
        if all([os.path.isfile(l) for l in lin[:-1]]):
            with open("data.txt",'w') as file:
                [file.write(line+'\n') for line in lin[:-1]]
            self.controller.argv = lin
            self.controller.show_frame("PageTwo")
        else:
            messagebox.showwarning("Warning","A file was not present")



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

