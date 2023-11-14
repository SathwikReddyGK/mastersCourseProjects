from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttkb
import shortestPathAlgorithms as algoLogic
from ttkbootstrap.dialogs import Messagebox

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
        self.inputSizeEntry.insert(0,"100")

        # Input Size Range field label
        self.inputSizeRangeLabel = ttkb.Label(self.mainFrame,text="INPUT SIZE INTERVAL",font=("Poppins",15))
        self.inputSizeRangeLabel.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.inputSizeRangeLabel.grid_remove()
        
        # Input Size Range Low field entry
        self.inputSizeRangeLowEntry = ttkb.Entry(self.mainFrame)
        self.inputSizeRangeLowEntry.grid(row=2, column=1, sticky="W",padx=10,pady=5)
        self.inputSizeRangeLowEntry.insert(0,"100")
        self.inputSizeRangeLowEntry.grid_remove()

        # Input Size Range High field entry
        self.inputSizeRangeHighEntry = ttkb.Entry(self.mainFrame)
        self.inputSizeRangeHighEntry.grid(row=2, column=2, sticky="W",padx=10,pady=5)
        self.inputSizeRangeHighEntry.insert(0,"100")
        self.inputSizeRangeHighEntry.grid_remove()

        # Input Size Range Interval Step Size Label
        self.inputSizeRangeStepSizeLabel = ttkb.Label(self.mainFrame,text="STEP SIZE",font=("Poppins",15))
        self.inputSizeRangeStepSizeLabel.grid(row=2, column=3, sticky="w", padx=10, pady=5)
        self.inputSizeRangeStepSizeLabel.grid_remove()

        # Input Size Range Interval Step Size entry
        self.inputSizeRangeStepSizeEntry = ttkb.Entry(self.mainFrame)
        self.inputSizeRangeStepSizeEntry.grid(row=2, column=4, sticky="W",padx=10,pady=5)
        self.inputSizeRangeStepSizeEntry.insert(0,"10")
        self.inputSizeRangeStepSizeEntry.grid_remove()

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

        # Checkbox to provide input size range
        self.inputRangeVar = ttkb.BooleanVar()
        self.inputRange = ttkb.Checkbutton(self.mainFrame,text="Size Range",variable=self.inputRangeVar,command=self.activateInputRange)
        self.inputRange.grid(row=5, column=1, columnspan=2, sticky="w", padx=10, pady=5)

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

    # Hide/Display fields based on compare checkbox
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

    # Hide/Display fields based on Size Range Checkbox
    def activateInputRange(self):
        if self.inputRangeVar.get():
            self.inputSizeRangeLowEntry.grid()
            self.inputSizeRangeHighEntry.grid()
            self.inputSizeRangeLabel.grid()
            self.inputSizeRangeStepSizeLabel.grid()
            self.inputSizeRangeStepSizeEntry.grid()
            self.inputSizeLabel.grid_remove()
            self.inputSizeEntry.grid_remove()
        else:
            self.inputSizeRangeLowEntry.grid_remove()
            self.inputSizeRangeHighEntry.grid_remove()
            self.inputSizeRangeLabel.grid_remove()
            self.inputSizeRangeStepSizeLabel.grid_remove()
            self.inputSizeRangeStepSizeEntry.grid_remove()
            self.inputSizeLabel.grid()
            self.inputSizeEntry.grid()

    def runButton(self):
        # Validations
        if self.inputRangeVar.get() and (self.inputSizeRangeLowEntry.get() == "" or self.inputSizeRangeHighEntry.get() == "" or self.inputSizeRangeStepSizeEntry.get() == ""):
            Messagebox.show_warning("Please enter the input size range and step size!")
        elif self.compareAlgoVar.get() and ((self.algorithmCombobox1.get() == "" and self.algorithmCombobox2.get() == "") or (self.algorithmCombobox1.get() == "" and self.algorithmCombobox3.get() == "") or (self.algorithmCombobox2.get() == "" and self.algorithmCombobox3.get() == "")):
            Messagebox.show_warning("Please enter atleast two algorithms to compare!")
        elif ( self.compareAlgoVar.get() == False and self.algorithm.get() not in ["Breadth For Search", "Bellman Ford", "Dijkstra"] ) or ( self.compareAlgoVar.get() == True and (self.algorithm1.get() not in ["Breadth For Search", "Bellman Ford", "Dijkstra"] or self.algorithm2.get() not in ["Breadth For Search", "Bellman Ford", "Dijkstra"] or self.algorithm3.get() not in ["Breadth For Search", "Bellman Ford", "Dijkstra"])):
            Messagebox.show_warning("Please enter valid Algorithm")
        else:
            # Trigger the logic of Shortest Path Algorithms
            algoLogic.main(int(self.inputSizeEntry.get()),int(self.sourceVertexEntry.get()),self.algorithm.get(),self.compareAlgoVar.get(),self.algorithm1.get(),self.algorithm2.get(),self.algorithm3.get(),int(self.inputSizeRangeLowEntry.get()),int(self.inputSizeRangeHighEntry.get()),int(self.inputSizeRangeStepSizeEntry.get()),self.inputRangeVar.get())
        
if __name__ == "__main__":
    root = ttkb.Window(themename="cyborg")
    shortestPathAlgorithmsApp(root)
    root.mainloop()