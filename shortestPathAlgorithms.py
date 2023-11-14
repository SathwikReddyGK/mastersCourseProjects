from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttkb
import graph as algoLogic

class shortestPathAlgorithmsApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Shortest Path Algorithms")
        self.root.geometry('1080x650')
        self.initializeGUI()

    def initializeGUI(self):
        
        # Creating a Frame
        self.mainFrame = ttkb.Frame(self.root,width=500)
        self.mainFrame.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        # Overall box label
        self.boxLabel = ttkb.Label(text="Shortest Path Algorithms",font=("Poppins",20))
        self.boxLabel.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        # Input Size field label
        self.inputSizeLabel = ttkb.Label(self.mainFrame,text="INPUT SIZE",font=("Poppins",15))
        self.inputSizeLabel.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        
        # Input Size field entry
        self.inputSizeEntry = ttkb.Entry(self.mainFrame)
        self.inputSizeEntry.grid(row=2, column=1, sticky="W",padx=10,pady=5)

        # Source Vertex field label
        self.sourceVertexLabel = ttkb.Label(self.mainFrame,text="SOURCE VERTEX",font=("Poppins",15))
        self.sourceVertexLabel.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        
        # Source Vertex field entry
        self.sourceVertexEntry = ttkb.Entry(self.mainFrame)
        self.sourceVertexEntry.grid(row=3, column=1, sticky="W",padx=10,pady=5)
        self.sourceVertexEntry.insert(0,"0")

        # Algorithm drop down label
        self.algorithmLabel = ttkb.Label(self.mainFrame,text="ALGORITHM",font=("Poppins",15))
        self.algorithmLabel.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        # Algorithm drop down Combobox
        self.algorithm = ttkb.StringVar()
        self.algorithmCombobox = ttkb.Combobox(self.mainFrame,textvariable=self.algorithm, values = ["Breadth For Search", "Bellman Ford", "Dijkstra"])
        self.algorithmCombobox.grid(row=4, column=1, sticky="w", padx=10, pady=5)

        # Checkbox to compare Algorithms
        self.compareAlgoVar = ttkb.BooleanVar()
        self.compareAlgo = ttkb.Checkbutton(self.mainFrame,text="Compare",variable=self.compareAlgoVar,command=self.compareVisible)
        self.compareAlgo.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        # Algorithms to be selected for comparision
        # Algorithm1 Label
        self.algorithmLabel1 = ttkb.Label(self.mainFrame,text="ALGORITHM1",font=("Poppins",15))
        self.algorithmLabel1.grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.algorithmLabel1.grid_remove()
        # Algorithm1 Dropbox
        self.algorithm1 = ttkb.StringVar()
        self.algorithmCombobox1 = ttkb.Combobox(self.mainFrame,textvariable=self.algorithm1, values = ["Breadth For Search", "Bellman Ford", "Dijkstra"])
        self.algorithmCombobox1.grid(row=6, column=1, sticky="w", padx=10, pady=5)
        self.algorithmCombobox1.grid_remove()

        # Algorithm2 Label
        self.algorithmLabel2 = ttkb.Label(self.mainFrame,text="ALGORITHM2",font=("Poppins",15))
        self.algorithmLabel2.grid(row=7, column=0, sticky="w", padx=10, pady=5)
        self.algorithmLabel2.grid_remove()
        # Algorithm2 Dropbox
        self.algorithm2 = ttkb.StringVar()
        self.algorithmCombobox2 = ttkb.Combobox(self.mainFrame,textvariable=self.algorithm2, values = ["Breadth For Search", "Bellman Ford", "Dijkstra"])
        self.algorithmCombobox2.grid(row=7, column=1, sticky="w", padx=10, pady=5)
        self.algorithmCombobox2.grid_remove()

        # Algorithm3 Label
        self.algorithmLabel3 = ttkb.Label(self.mainFrame,text="ALGORITHM3",font=("Poppins",15))
        self.algorithmLabel3.grid(row=8, column=0, sticky="w", padx=10, pady=5)
        self.algorithmLabel3.grid_remove()
        # Algorithm3 Dropbox
        self.algorithm3 = ttkb.StringVar()
        self.algorithmCombobox3 = ttkb.Combobox(self.mainFrame,textvariable=self.algorithm3, values = ["Breadth For Search", "Bellman Ford", "Dijkstra"])
        self.algorithmCombobox3.grid(row=8, column=1, sticky="w", padx=10, pady=5)
        self.algorithmCombobox3.grid_remove()

        # Custom Style for Run button
        self.buttonStyle = ttkb.Style()
        self.buttonStyle.configure('dark.TButton',font=("Poppins",20))

        # Run button
        # bootstyle="dark", style="dark.TButton, outline",
        self.runButton = ttkb.Button(self.mainFrame,text="Run", style="outline",command=self.runButton)
        self.runButton.grid(row=9, column=0, sticky="w", padx=10, pady=5)

    def compareVisible(self):
        if self.compareAlgoVar.get():
            self.algorithmLabel1.grid()
            self.algorithmCombobox1.grid()
            self.algorithmLabel2.grid()
            self.algorithmCombobox2.grid()
            self.algorithmLabel3.grid()
            self.algorithmCombobox3.grid()
            self.algorithmLabel.grid_remove()
            self.algorithmCombobox.grid_remove()
        else:
            self.algorithmLabel1.grid_remove()
            self.algorithmCombobox1.grid_remove()
            self.algorithmLabel2.grid_remove()
            self.algorithmCombobox2.grid_remove()
            self.algorithmLabel3.grid_remove()
            self.algorithmCombobox3.grid_remove()
            self.algorithmLabel.grid()
            self.algorithmCombobox.grid()

    def runButton(self):
        algoLogic.main(int(self.inputSizeEntry.get()),int(self.sourceVertexEntry.get()),self.algorithm.get(),self.compareAlgoVar.get(),self.algorithm1.get(),self.algorithm2.get(),self.algorithm3.get())
            
if __name__ == "__main__":
    root = ttkb.Window(themename="cyborg")
    shortestPathAlgorithmsApp(root)
    root.mainloop()