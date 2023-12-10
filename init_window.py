import tkinter as tk
from PIL import ImageTk, Image  
import numpy as np
from matplotlib import pyplot as plt
import os
import run_all_classifiers as rac
import data_splitting as ds
import lbp_FeatureExtraction as lbp

class Window(tk.Tk):
  
    def __init__(self):
        super().__init__() 
        self.image = None #class attribute to store the input image
        self.image_copy = None
        self.resized_image = None
        self.tkimage = None #class attribute to store the display image
        self.rgb_color = (255,0,0) #attribute to store a RGB color (default=red)
        self.create_main_window()
        self.create_control_frame()
        self.create_image_canvas()       
        self.create_menubar()  
        #set a protocol to close all windows when main window is closed
        self.protocol('WM_DELETE_WINDOW', self.close_all_windows)

    def close_all_windows(self):
        plt.close('all')
        self.destroy()    
    
    def create_main_window(self):
        self.title('Filtragem de Imagem')
        self.width= self.winfo_screenwidth()               
        self.height= self.winfo_screenheight()   
        #set 80% of screen width and height            
        self.geometry("%dx%d" % (self.width*.8, self.height*.8))
        #maximize the window
        #self.state('zoomed')

    def create_control_frame(self):
        self.controls = tk.Frame(self)
        self.controls.pack(side=tk.TOP,expand=True,pady=(0,10))

    def clear_control_frame(self):
        # destroy all widgets from frame
        for widget in self.controls.winfo_children():
            widget.destroy()

    def create_menubar(self): 
        self.menu_bar = tk.Menu(self, tearoff="off")
        self.config(menu=self.menu_bar)
        file_menu = tk.Menu(self.menu_bar, tearoff="off")
        #self.menu_bar.add_cascade(label='Arquivo', menu=file_menu)
        #file_menu.add_command(label='Abrir...', command=self.load_image)
        file_menu.add_separator()
       
        self.create_lbp_menu()
        self.create_hu_moments_menu()
    
    def create_lbp_menu(self):
        lbp_menu = tk.Menu(self, tearoff="off")
        self.menu_bar.add_cascade(label='LBP', menu=lbp_menu, state='normal')
        lbp_menu.add_command(label='Introdução', command=self.lbp_about)
        lbp_menu.add_command(label='Aplicar modelo', command=self.lbp_apply)
        

    def create_hu_moments_menu(self):
        hu_moments_menu = tk.Menu(self, tearoff="off")
        self.menu_bar.add_cascade(label='Hu Moments', menu=hu_moments_menu, state='normal')

    def create_image_canvas(self):
        image_frame = tk.Frame(self)
        image_frame.pack()
        yscrollbar = tk.Scrollbar(image_frame, orient = tk.VERTICAL)
        yscrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        xscrollbar = tk.Scrollbar(image_frame, orient = tk.HORIZONTAL)
        xscrollbar.pack(side = tk.BOTTOM, fill = tk.X)
        self.image_canvas = tk.Canvas(image_frame, 
                                      width = self.width, 
                                      height = self.height,
                                      xscrollcommand = xscrollbar.set, 
                                      yscrollcommand = yscrollbar.set)
        self.image_canvas.bind("<Button-1>", self.get_color)
        self.image_canvas.pack()
        yscrollbar.config(command = self.image_canvas.yview)
        xscrollbar.config(command = self.image_canvas.xview)
    
    def activate_menus(self):
        self.menu_bar.entryconfig('Filtros',state='active')
        self.menu_bar.entryconfig('Imagem',state='active')
        self.menu_bar.entryconfig('Cores',state='active')
        self.menu_bar.entryconfig('Segmentação',state='active')

    def get_color(self, event):
        if (np.ndim(self.image) > 2): #if more than 2 dimensions then it is a color image
            x,y = event.x,event.y
            #print(f'clicked at: {x,y}')
            h,w = self.image.shape[:2]
            #print(w,h)
            if(x < w and y < h):
                img = Image.fromarray(self.image)
                self.rgb_color = img.getpixel((x,y))
                self.update_segmentation_controls()
    
    def lbp_about():
        print('lbp_about')


    def lbp_apply(self):
        self.clear_control_frame()

        nPoints_label = tk.Label(self.controls, text='Número de pontos da vizinhança:')
        nPoints_label.grid(row=0, column=0, sticky=tk.W, pady=20)

        nPoints_spinbox = tk.Spinbox(self.controls, from_=0, to=255)
        nPoints_spinbox.grid(row=0, column=1,  sticky=tk.W, padx= 20)

        radius_label = tk.Label(self.controls, text='Raio da vizinhança:')
        radius_label.grid(row=0, column=2,  sticky=tk.W, pady=20)

        radius_spinbox = tk.Spinbox(self.controls, from_=0, to=255)
        radius_spinbox.grid(row=0, column=3,  sticky=tk.W)

        iniciar_button = tk.Button(self.controls, text="Iniciar Treinamento", command=lambda: self.start_training(int(nPoints_spinbox.get()), int(radius_spinbox.get())))
        iniciar_button.grid(row=0, column=4, sticky=tk.W, padx=20)
        
    def start_training(self, nPoints_value, radius_value):
        try:
            ds.exec_split()
        except:
            print('Erro ao dividir as imagens')
        
        try:
            lbp.exec_lbp(nPoints_value, radius_value)
        except:
            print('Erro ao aplicar o modelo')

       
        results = rac.exec_all_classifiers()
        plotResults(self, results[0], results[1])
       
          
        

def plotResults(self,modelNames,results):
    fig, ax = plt.subplots()
    bar_container = ax.bar(modelNames, results,color=['red', 'green', 'blue', 'cyan'])
    ax.set_ylabel('Accuracy',weight='bold')
    ax.set_xlabel('Models',weight='bold')
    ax.set_title('Model comparison',fontsize=18,weight='bold')
    ax.bar_label(bar_container, fmt='{:,.2f}%')
    fileName = rac.getCurrentFileNameAndDateTime()
    plt.savefig('./results/' + fileName, dpi=300) 
    print(f'[INFO] Plotting final results done in ./results/{fileName}')
    print(f'[INFO] Close the figure window to end the program.')

    image = Image.open('./results/' + fileName + ".png")
    new_width = int(image.width * 0.6)
    new_height = int(image.height * 0.5)
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(resized_image)
    label1 = tk.Label(image=test)
    label1.image = test

    screen_width = self.winfo_screenwidth()
    image_width = resized_image.width 
    x = (screen_width - image_width) / 2  # Calculating x position for centering

    label1.place(x=x, y=100)

    


if __name__== '__main__':
    app=Window()
    app.mainloop()