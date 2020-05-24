# Find. Discover. Grow. by AfreAustin
#   Find plants around your neigborhood, discover what they are, and 
#       grow your own
# Made for BackyardHacks 

from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
import webbrowser as web
import sys

def main():
    root = Tk()
    root.geometry("900x720")
    
    app = Application(root)
    app.configure(bg = '#35db61')
    
    root.mainloop()

def callback(url):
    web.open_new(url)

# GUI Interface
class Application(Frame):

    # initializes window frame
    def __init__(self, master = None):              # master = None is default
        Frame.__init__(self, master)

        self.master = master
        self.plants = {"1": { "name" : "Magnolia" , 
                              "desc" : '''
                                       \n Kingdom: Plantae
                                       \n Clade: 	Tracheophytes, Angiosperms, Magnoliids
                                       \n Order: 	Magnoliales
                                       \n Family: 	Magnoliaceae
                                       \n Genus: 	Magnolia 
                                       \n
                                       \n Magnolias are spreading, evergreen or deciduous trees or shrubs, 
                                       \n characterised by large fragrant flowers which may be bowl-shaped 
                                       \n or star-shaped, in shades of white, pink, purple, green or yellow. 
                                       \n The blooms often appear before the leaves, in Spring. 
                                       \n Cone-like fruits are often produced in Autumn
                                       \n                                                    from Wikipedia
                                       '''},
                       "2": { "name" : "Ox-Eye Daisy" , 
                              "desc" : '''
                                       \n Kingdom: 	Plantae
                                       \n Clade: 	Tracheophytes, Angiosperms, Eudicots, Asterids
                                       \n Order: 	Asterales
                                       \n Family: 	Asteraceae
                                       \n Genus: 	Leucanthemum
                                       \n
                                       \n Leucanthemum vulgare is a perennial herb that grows to a height of 
                                       \n 60 cm (20 in) or more and has a creeping underground rhizome. The 
                                       \n lower parts of the stem are hairy, sometimes densely hairy but more 
                                       \n or less glabrous in the upper parts. The largest leaves are at the 
                                       \n base of the plant and are 4–15 cm (1.6–5.9 in) long, about 5 cm (2 in) 
                                       \n wide and have a petiole. These leaves have up to 15 teeth, or lobes 
                                       \n or both on the edges. The leaves decrease in size up the stem, the 
                                       \n upper leaves up to 7.5 cm (3 in) long, lack a petiole and are deeply 
                                       \n toothed.                                           from Wikipedia
                                       '''},
                       "3": { "name" : "Virginia Spring Beauty" , 
                              "desc" : '''
                                       \n Kingdom: 	Plantae
                                       \n Clade: 	Tracheophytes, Angiosperms, Eudicots
                                       \n Order: 	Caryophyllales
                                       \n Family: 	Montiaceae
                                       \n Genus: 	Claytonia
                                       \n
                                       \n Springbeauty is a perennial plant, overwintering through a tuberous 
                                       \n root. It is a trailing plant growing to 5–40 cm (2–16 in) long. 
                                       \n The leaves are slender lanceolate, 3–14 cm (1 1⁄4–5 1⁄2 in) long 
                                       \n and 0.5–1.3 cm (0.20–0.51 in) broad, with a 6–20 cm (2 1⁄4–7 3⁄4 in) 
                                       \n long petiole.
                                       \n                                                   from Wikipedia
                                       '''},
                       "4": { "name" : "Tuberous Vervain" ,
                              "desc" : '''
                                       \n Kingdom: 	Plantae
                                       \n Clade: 	Tracheophytes, Angiosperms, Eudicots, Asterids
                                       \n Order: 	Lamiales
                                       \n Family: 	Verbenaceae
                                       \n Genus: 	Verbena
                                       \n 
                                       \n Verbena rigida, known as slender vervain or tuberous vervain, 
                                       \n is a flowering herbaceous perennial plant. It is native to 
                                       \n Brazil and Argentina, and is not fully hardy in temperate 
                                       \n climates, where consequently it is grown from seed as an annual.
                                       \n                                                   from Wikipedia
                                       '''},
                       "5": { "name" : "Austin Tree" , 
                              "desc" : "This is the description of an Austin Tree. Coming Soon"}}
        
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
                p_desc.config(text = desc, anchor = 'nw', justify = LEFT)
        
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

            chg_lc = Button(self, text = "(change location)",
                            bg = '#329c4e', fg = 'white',
                            relief = FLAT)
            chg_lc.place(x = 630, y = 100)

            lctn_l = Label(self, text = 'Current Location: ',
                           font = ("Times", 16),
                           relief = RAISED)
            lctn_l.place(x = 500, y = 70)
            c_lctn = Label(self, text = "Censored for Demo",
                           font = ("Times", 16),
                           relief = RAISED)
            c_lctn.place(x = 660, y = 70)
            
            plnt_l = Label(self,text = 'Selected: ',
                           font = ("Times", 16),
                           relief = RAISED)
            plnt_l.place(x = 500, y = 130)
            c_plnt = Label(self, text = "Select a Plant",
                           font = ("Times", 16),
                           relief = RAISED) 
            c_plnt.place(x = 600, y = 130)
            
            pval_l = Label(self, text = "Growable in your area: ",
                           font = ("Times", 16),
                           relief = RAISED)
            pval_l.place(x = 500, y = 160)
            pvalid = Label(self, text = "HOPEFULLY :)",
                           font = ("Times", 16),
                           relief = RAISED) 
            pvalid.place(x = 720, y = 160)

            growng = Label(self, 
                           text = "SELECT PLANT",
                           relief = GROOVE)
            growng.place(x = 615, y = 200)

            # Plant Points
            def set_plant(name, desc):
                c_plnt.config(text = name)
                pvalid.config(text = desc)

                if name == 'Magnolia':
                    growng.config(text = "Learn how to grow this")
                    growng.bind("<Button-1>", 
                                lambda e: callback("https://todayshomeowner.com/how-to-grow-magnolias-in-your-yard/"))
                elif name == 'Ox-Eye Daisy':
                    growng.config(text = "Learn how to grow this")
                    growng.bind("<Button-1>", 
                                lambda e: callback("https://www.americanmeadows.com/wildflower-seeds/daisy-seeds/how-to-grow-daisies"))
                elif name == 'Virginia Spring Beauty':
                    growng.config(text = "Learn how to grow this")
                    growng.bind("<Button-1>", 
                                lambda e: callback("https://www.friendsofthewildflowergarden.org/pages/plants/springbeauty_virginia.html"))
                elif name == 'Tuberous Vervain':
                    growng.config(text = "Learn how to grow this")
                    growng.bind("<Button-1>", 
                                lambda e: callback("https://aggie-horticulture.tamu.edu/wildseed/41/41.1.html"))
                elif name == 'Austin Tree':
                    growng.config(text = "Sorry... You can't grow this :(")
                    growng.unbind("<Button-1>")
    
            plant1 = Button(self, text = 1,
                            command = lambda: set_plant(self.plants['1']['name'], 
                                                        'YES'),
                            bg = '#9f00da', 
                            font = font.Font(size = 5),
                            width = 1)
            plant1.place(x = 55 , y = 200)
            
            plant2 = Button(self, text = 2,
                            command = lambda: set_plant(self.plants['2']['name'], 
                                                        'YES'),
                            bg = '#9f00da', 
                            font = font.Font(size = 5),
                            width = 1)
            plant2.place(x = 80 , y = 600)

            plant3 = Button(self, text = 3,
                            command = lambda: set_plant(self.plants['3']['name'], 
                                                        'YES'),
                            bg = '#9f00da', 
                            font = font.Font(size = 5),
                            width = 1)
            plant3.place(x = 180, y = 300)

            plant4 = Button(self, text = 4,
                            command = lambda: set_plant(self.plants['4']['name'], 
                                                        'YES'),
                            bg = '#9f00da', 
                            font = font.Font(size = 5),
                            width = 1)
            plant4.place(x = 320, y = 120)

            plant5 = Button(self, text = 5,
                            command = lambda: set_plant(self.plants['5']['name'], 
                                                        'NO'),
                            bg = '#9f00da', 
                            font = font.Font(size = 5),
                            width = 1)
            plant5.place(x = 435, y = 420)

#----------------------------------------------------#

        # Home Screen
        find_screen()
        
main()