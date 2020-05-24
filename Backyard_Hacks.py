# Find. Discover. Grow. by AfreAustin
#   Find plants around your neigborhood, discover what they are, and 
#       grow your own
# Made for BackyardHacks 

# 33°27'14.3"N 88°47'27.4"W
# Enter into Coord

from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

def main():
    root = Tk()
    root.geometry("900x720")
    
    app = Application(root)
    app.configure(bg = '#35db61')
    
    root.mainloop()

# GUI Interface
class Application(Frame):

    # initializes window frame
    def __init__(self, master = None):              # master = None is default
        Frame.__init__(self, master)

        self.master = master
        self.plants = {"1": { "name" : "Plant 1" , "desc" : "Desc 1"},
                       "2": { "name" : "Plant 2" , "desc" : "Desc 2"},
                       "3": { "name" : "Plant 3" , "desc" : "Desc 3"},
                       "4": { "name" : "Plant 4" , "desc" : "Desc 4"},
                       "5": { "name" : "Austin Tree" , "desc" : "This is the description of an Austin Tree"}}
        
        self.pack()
        self.init_window()
        self.init_labels()
        self.init_progrm()
        
    # creates main window
    def init_window(self):

        self.master.title(" Find. Discover. Grow. ")
        self.pack(fill = BOTH, expand = 1)

    # creates labels
    def init_labels(self):
        
        # Title
        title = Label(self, text = " Find. Discover. Grow. ",
                     bg = '#5dd97e', 
                     borderwidth = 5, relief = RIDGE)
        title.config( font = ('CopperplateGothicLight', '25', 'bold') )
        title.place(relx = 0.28, rely = 0.01)

        # Credits
        credits = Label(self, text = ("_" * 173) 
                                   + "\n created by AfreAustin",
                      bg = '#35db61')
        credits.place(relx = 0.015, rely = 0.90)

    # creates program
    def init_progrm(self):
        
        # Background Settings
        def background_set():
            background = Label(self,
                               bg = '#329c4e', 
                               width = 125, height = 38,
                               borderwidth = 3, relief = RIDGE)
            background.place(x = 10, y = 60)
        
        # Action Buttons
        def actions():
            # Find Button
            FindButton = Button(self, text = " FIND ", 
                            bg = '#f0f590', fg = 'black',
                            command = find_screen)
            FindButton.place(relx = 0.71, rely = 0.015)

            # Discover Button
            DiscoverButton = Button(self, text = " DISCOVER ", 
                            bg = '#f2bd77', fg = 'black',
                            command = discover_screen)
            DiscoverButton.place(relx = 0.77, rely = 0.015)

            # Grow Button
            GrowButton = Button(self, text = " GROW ", 
                            bg = '#f07d7d', fg = 'black',
                            command = grow_screen)
            GrowButton.place(relx = 0.86, rely = 0.015)

            # Exit Button
            ExitButton = Button(self, text = " EXIT ", 
                            bg = '#f44040', fg = 'black',
                            command = self.master.destroy )
            ExitButton.place(relx = 0.93, rely = 0.015)

        # Map Setting
        def set_map():
            load = Image.open('Map.png')
            img = ImageTk.PhotoImage( load.resize((450,550)) )

            map = Label(self, image = img,
                        relief = SUNKEN)
            map.image = img
            map.place(x=20,y=70)

        # Plants Information
        def plants():
            # Plant Labels
            p_name = Label(self, text = 'Plant Name',
                           height = 2, width = 25,
                           font = ("Times", 20),
                           relief = RAISED)
            p_name.place(x = 500, y = 70)

            p_desc = Label(self, text = 'Plant Description',
                           width = 53, height = 31,
                           relief = GROOVE,anchor = 'nw')
            p_desc.place(x = 500, y = 150)
        
            # Plant Points
            def set_plant(name, desc):
                p_name.config(text = name)
                p_desc.config(text = desc)
        
            plant1 = Button(self, text = 1,
                            command = lambda: set_plant(self.plants['1']['name'], 
                                                        self.plants['1']["desc"]),
                            bg = '#9f00da', 
                            font = font.Font(size = 5),
                            width = 1)
            plant1.place(x = 55 , y = 200)
    
            plant2 = Button(self, text = 2,
                            command = lambda: set_plant(self.plants['2']['name'], 
                                                        self.plants['2']["desc"]),
                            bg = '#9f00da', 
                            font = font.Font(size = 5),
                            width = 1)
            plant2.place(x = 80 , y = 600)

            plant3 = Button(self, text = 3,
                            command = lambda: set_plant(self.plants['3']['name'], 
                                                        self.plants['3']["desc"]),
                            bg = '#9f00da', 
                            font = font.Font(size = 5),
                            width = 1)
            plant3.place(x = 180, y = 300)

            plant4 = Button(self, text = 4,
                            command = lambda: set_plant(self.plants['4']['name'], 
                                                        self.plants['4']["desc"]),
                            bg = '#9f00da', 
                            font = font.Font(size = 5),
                            width = 1)
            plant4.place(x = 320, y = 120)

            plant5 = Button(self, text = 5,
                            command = lambda: set_plant(self.plants['5']['name'], 
                                                        self.plants['5']["desc"]),
                            bg = '#9f00da', 
                            font = font.Font(size = 5),
                            width = 1)
            plant5.place(x = 435, y = 420)

#----------------------------------------------------#
        
        # Action Screens Settings
        def find_screen():
            background_set()
            actions()
            set_map()
            plants()

        def discover_screen():
            background_set()
            actions()
            set_map()
            
            name_l = Label(self, text = 'Plant Name: ',
                           font = ("Times", 16),
                           relief = RAISED)
            name_l.place(x = 500, y = 70)

            d_name = Entry(self,
                           font = ("Times", 16),
                           relief = RAISED)
            d_name.place(x = 620, y = 70)

            plce_l = Label(self, text = 'Plant Coord:',
                           font = ("Times", 16),
                           relief = RAISED)
            plce_l.place(x = 500, y = 100)

            d_plce = Entry(self,
                           font = ("Times", 16),
                           relief = RAISED)
            d_plce.place(x = 620, y = 100)


            def set_image():
                load = Image.open('tree.jpg')
                img = ImageTk.PhotoImage(load.resize((300,400)))
                
                d_imag = Label(self, image = img)
                d_imag.image = img
                d_imag.place(x = 530, y = 210)

            d_upld = Button(self, text = "upload image",
                            command = set_image)
            d_upld.place(relx = 0.71, y = 170 )

            d_warn = Label(self, 
                           text = "Please upload image for verification",
                           relief = GROOVE)
            d_warn.place(x = 585, y = 140)

        def grow_screen():
            background_set()
            actions()
            set_map()
            
#----------------------------------------------------#

        # Home Screen
        find_screen()
        
main()
