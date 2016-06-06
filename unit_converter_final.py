from tkinter import *

class Unit_Converter():
    '''
    This class creates and grids all widgets and frames and allows the switching between them. 
    The user is able to enter a data value which is sent to the Calculations class to be converted.
    '''

    def __init__(self, parent):

        '''
        This method creates all the frames and buttons used within the
        program and then grids the widgets displayed by defult and the
        instructions text
        '''
        
        #Creates the labels to display in each frame 
        self.lgth_labels = ['Millimeters','Centimeters', 'Miles', 'Inches', 'Meters', 'Kilometers', 'Feet', 'Yards']
        self.temp_labels = ['°C','°F', 'K']
        self.wght_labels = ['Metric Tons','Kilograms','Pounds', 'Ounces', 'Grams', 'Tons']
        self.prss_labels = ['bar','Kg/cm^2', 'Psi']
        self.vlme_labels = ['Milliliters','Liters', 'Fluid Oz', 'Pints', 'Cups', 'Quarts', 'Gallons', 'Barrels']

        #Creates a top, middle, and bottom frame
        f_top = Frame(parent, padx = 2, pady = 2, bg = 'slategrey')
        self.f_mid = Frame(parent, width = 420, height = 175)
        f_btm = Frame(parent, padx = 2, pady = 2, bg = 'slategrey')
        
        #Creates the buttons displayed in the top frame which change the middle frame
        btn_lgth = Button(f_top, text = 'Length', width = 10, height = 2, command = lambda: self.set_frame(self.lgth_frame, self.lgth_labels, 'medium spring green', 4, 4, 14, 'lgth'))
        btn_temp = Button(f_top, text = 'Temperature', width = 10, height = 2, command = lambda: self.set_frame(self.temp_frame, self.temp_labels, 'orange', 2, 3, 30, 'temp'))
        btn_wght = Button(f_top, text = 'Weight', width = 11, height = 2, command = lambda: self.set_frame(self.wght_frame, self.wght_labels, 'cornflower blue', 4, 3, 14, 'wght'))
        btn_prss = Button(f_top, text = 'Pressure', width = 10, height = 2, command = lambda: self.set_frame(self.prss_frame, self.prss_labels, 'violet', 2, 3, 20, 'prss'))
        btn_vlme = Button(f_top, text = 'Volume', width = 10, height = 2, command = lambda: self.set_frame(self.vlme_frame, self.vlme_labels, 'salmon', 4, 4, 15, 'vlme'))

        #Creates the 5 different conversion frames displayed in the middle frame
        self.lgth_frame = Frame(parent, bg = 'medium spring green')
        self.temp_frame = Frame(parent, bg = 'orange')
        self.wght_frame = Frame(parent, bg = 'cornflower blue')
        self.prss_frame = Frame(parent, bg = 'violet')
        self.vlme_frame = Frame(parent, bg = 'salmon')
        
        #Creates the instructions text
        self.instructions = []
        instructions_text = ['Select type of conversion above i.e. length','Enter value for conversion less than 10 digits then press calculate or return','Press clear to delete all entries',
                             'NOTE:  Value will be calculated from entry box which contains the cursor','','']
        self.instructions_l1 = Label(self.f_mid, text = '')
        self.instructions_l2 = Label(self.f_mid, text = 'Instructions:', font = ('times', '15'))

        for i in range (len(instructions_text)):
            self.instructions.append(Label(self.f_mid, text = instructions_text[i]))
            
        #Creates buttons displayed on the bottom frame
        btn_inst = Button(f_btm, text = 'Instructions', width = 13, pady = 2, padx = 10, command = self.view_instructions)
        self.btn_clr = Button(f_btm, text = 'Clear', padx = 10, pady = 2, width = 13, command = self.clr_check_empty, state = DISABLED)
        self.btn_calc = Button(f_btm, text = 'Calculate', padx = 10, pady = 2, width = 13, command = self.calc_check_empty, state = DISABLED)

        #Gridding top buttons 
        btn_lgth.grid(row = 0, column = 0, padx = 1)
        btn_temp.grid(row = 0, column = 1, padx = 1)
        btn_wght.grid(row = 0, column = 2, padx = 1)
        btn_prss.grid(row = 0, column = 3, padx = 1)
        btn_vlme.grid(row = 0, column = 4, padx = 1)
        
        #Gridding bottom buttons
        btn_inst.grid(row = 0, column = 0, padx = 10, pady = 3, sticky = S)
        self.btn_clr.grid(row = 0, column = 1, padx = 10, pady = 3, sticky = S)
        self.btn_calc.grid(row = 0, column = 2, padx = 10, pady = 3, sticky = S)
        
        #Gridding top, middle, and bottom frame
        f_top.grid(row = 0, column = 0)
        self.f_mid.grid(row = 1, column = 0)
        f_btm.grid(row = 2, column = 0)

        #Creates a key binding to the return key
        parent.bind("<Return>", self.return_press)
        
        #Runs module displaying instructions
        self.view_instructions()

    def calc_check_empty(self):
        '''
        This method along with the 'clr_check_empty' method check if values are entered
        into the entry boxes before the calculation or clear methods are run. This is
        done in order to prevent and error
        '''
        for i in range(len(self.entries)):
            if len(self.entries[i].get()) != 0:
                self.check_focus()

    def clr_check_empty(self):
        for i in range(len(self.entries)):
            if len(self.entries[i].get()) != 0:
                self.clear()

    def return_press(self, event):
        #Runs check_focus method after return key is pressed
        self.calc_check_empty()

    def view_instructions(self):
        '''
        This method clears the middle frame, set background colour
        to default and then displays the instructions
        '''
        self.entries = []
        #Clearing middle frame
        self.frame_forget()
        #Setting middle frame to default colour
        self.f_mid.configure(bg = '#F0F0F0')
        #Packs and diplays the instructions text
        self.instructions_l1.pack()
        self.instructions_l2.pack()
        for i in range (len(self.instructions)):
            self.instructions[i].pack()

        self.btn_calc.configure(state = DISABLED)
        self.btn_clr.configure(state = DISABLED)

    def set_frame(self, frame, labels, colour, row, column, size, current_frame):
        '''
        This method is run when one of the top buttons is press and takes values
        using a lambda function. The values for each different frame is passed
        through and then that frame is gridded
        '''
        #Setting variables
        self.frame = frame
        self.current_frame = current_frame
        #Clearing middle frame
        self.frame_forget()
        #Setting background colour passed through lambda
        self.f_mid.configure(bg = colour)
        
        #Creating variables used in gridding labels and entry boxes
        labels_list = []
        self.entries = []
        
        i=0
        e=0

        #Gridding Labels and entry boxes based on specification passed through lambda
        for r in range(row):
            for c in range(column):
                if (r==0) or (r==3):
                    labels_list.append(Label(self.frame, text = labels[i], bg = colour, font = ('times', size)))
                    labels_list[i].grid(row = r, column = c)
                    i += 1
                if (r==1) or (r==2):
                    self.entries.append(Entry(self.frame, width = 16))
                    self.entries[e].grid(row = r, column = c, padx = 2, pady = 2)
                    e += 1
                    
        #Grids the frame to the middle frame        
        self.frame.grid(row = 1, column = 0)
        
        self.btn_calc.configure(state = NORMAL)
        self.btn_clr.configure(state = NORMAL)

    def frame_forget(self):
        '''
        This method clears any frames currently displayed in the middle frame
        '''

        #Clears instructions
        self.instructions_l1.pack_forget()
        self.instructions_l2.pack_forget()
        for i in range (len(self.instructions)):
            self.instructions[i].pack_forget()

        #Clears conversion frames
        self.lgth_frame.grid_forget()
        self.temp_frame.grid_forget()
        self.wght_frame.grid_forget()
        self.prss_frame.grid_forget()
        self.vlme_frame.grid_forget()

    def clear(self):
        #Clears all entry boxes currently displayed
        for i in range (len(self.entries)):
            self.entries[i].delete(0, END)

    def check_focus(self):
        '''
        This method checks which entry box has focus and passes the
        value onto the Calculations class
        '''
        #Creating variables
        self.entry = ''
        #Finding the focus
        self.entry = self.frame.focus_get()
        
        for i in range (len(self.entries)):
            if self.entry.get() == self.entries[i].get():
                #finding the entry position
                self.entry_pos = i
                self.check_entry(len(self.entries[i].get()))

    def check_entry(self, len_entry):
        '''
        This method checks that the entry value is valid before the conversion begins
        '''
        check1 = True

        #Checking if the entered value is a number
        try:
            choice = float(self.entries[self.entry_pos].get())
        except ValueError:
            check1 = False
            self.clear()
            self.entries[self.entry_pos].insert(0, 'Enter a Number')
        
        #Checking if the value is below the maximum length
        if check1 == True:
            if len_entry >= 10:
                check1 = False
                self.clear()
                self.entries[self.entry_pos].insert(0, 'Value Too Long')

        #Checking if the value is negative in cases where it is impossible
        if check1 == True:
            if (self.current_frame == 'lgth') or (self.current_frame == 'wght') or (self.current_frame == 'vlme'):
                if float(self.entries[self.entry_pos].get()) < 0:
                    check1 = False
                    self.clear()
                    self.entries[self.entry_pos].insert(0, 'Must be Positive')
            #Checking temperature values are not below absolute zero
            if (self.current_frame == 'temp'):
                if (self.entry_pos == 0):
                    if float(self.entries[self.entry_pos].get()) < -273.15:
                        check1 = False
                        self.clear()
                        self.entries[self.entry_pos].insert(0, 'Not Possible')
                if (self.entry_pos == 1):
                    if float(self.entries[self.entry_pos].get()) < -459.67:
                        check1 = False
                        self.clear()
                        self.entries[self.entry_pos].insert(0, 'Not Possible')
                if (self.entry_pos == 2):
                    if float(self.entries[self.entry_pos].get()) < 0:
                        check1 = False
                        self.clear()
                        self.entries[self.entry_pos].insert(0, 'Must be Positive')

        #If all checks are passed the values are sent to the Calculations class to be converted
        if check1 == True:
            Calculations(self.entry.get(), self.entry_pos, self.current_frame)

    def display_values(self, units, frame):
        '''
        This method displays the converted values that
        have been passed from the Calculations class
        '''
        #Sets desired frame
        if frame == 'lgth':
            self.set_frame(self.lgth_frame, self.lgth_labels, 'medium spring green', 4, 4, 14, 'lgth')
        if frame == 'temp':
            self.set_frame(self.temp_frame, self.temp_labels, 'orange', 2, 3, 30, 'temp')
        if frame == 'wght':
            self.set_frame(self.wght_frame, self.wght_labels, 'cornflower blue', 4, 3, 14, 'wght')
        if frame == 'prss':
            self.set_frame(self.prss_frame, self.prss_labels, 'violet', 2, 3, 20, 'prss')
        if frame == 'vlme':
            self.set_frame(self.vlme_frame, self.vlme_labels, 'salmon', 4, 4, 15, 'vlme')

        #Clears all entry boxes
        self.clear()

        #Displays converted values in entry boxes
        for i in range (len(self.entries)):
            self.entries[i].insert(0, units[i])


class Calculations():
    '''
    This class recieves data from the Unit_Converter class entered by the user. The value it is
    checked and converted into other units and set in a list. That list is then sent back to the
    Unit_Converter class and displayed on screen
    '''

    def __init__(self, entry, entry_pos, frame):
        '''
        This method instagates all the variables sent from the Unit_Converter
        class and chooses which conversion method to run
        '''
        #Creating variables
        self.entry = entry
        self.entry_pos = entry_pos
        self.frame = frame

        #Choosing which conversion method to run
        if self.frame == 'temp':
            converter.display_values(self.temp_convert(), self.frame)
        else:
            converter.display_values(self.convert(), self.frame)

    def convert(self):
        '''
        This method convertes values of length, weight, pressure, and
        volume into other units
        '''

        #Setting up variables
        unit_in_standard = 0
        converted_units = []

        #If the entered value is a length it is converterd to meters then to the other values of length
        if self.frame == 'lgth':
            #Value of 1 unit in meters
            standard = [0.001, 0.01, 1609.347218694, 0.0254, 1, 1000, 0.3048, 0.9144]
            #Number of units per meter
            units_per_standard = [1000, 100, 0.00062137, 39.3700, 1, 0.0010, 3.2808, 1.0936]

        #If the entered value is a weight it is converterd to kilograms then to the other values of weight
        if self.frame == 'wght':
            #Value of 1 unit in kg
            standard = [1000, 1, 0.45359237, 0.028349523125, 0.001, 1016.05]
            #Number of units per kg
            units_per_standard = [0.001, 1, 2.2046226218, 35.27396195, 1000, 0.0010]

        #If the entered value is a pressure it is converterd to Psi then to the other values of pressure
        if self.frame == 'prss':
            #Value of 1 unit in Psi
            standard = [14.503773801, 14.223343334, 1]
            #Number of units per Psi
            units_per_standard = [0.0689475783, 0.07030695783, 1]

        #If the entered value is a volume it is converterd to liters then to the other values of volume
        if self.frame == 'vlme':
            #Value of 1 unit in liters
            standard = [0.0010, 1, 0.029573529563, 0.4732, 0.2500, 0.9464, 3.7854, 119.2404712]
            #Number of units per liters
            units_per_standard = [1000, 1, 33.814022701, 2.1133, 4, 1.0566, 0.2641, 0.0083864143603]

        #The converted values are calculated, formatted to 2dp, and put in a list
        unit_in_standard = float(self.entry) * float(standard[self.entry_pos])
        for i in range(len(standard)):
            converted_value = unit_in_standard*units_per_standard[i]
            converted_units.append("{0:.3f}".format(converted_value))

        #The list is returned to the __init__ method which sends it back to the Unit_Converter method
        return converted_units

    def temp_convert(self):
        '''
        This method convertes temperature values and sends them back to be displayed. Due to the
        non-linear nature of the conversion of temperature values, the conversion equations had
        to be hard coded
        '''

        #Creating variables
        converted_units = [0,0,0]
        rounded_values = []
        
        #Runs conversion based on the position of entry
        if self.entry_pos == 0:
            converted_units[0] = self.entry
            converted_units[1] = (((float(self.entry)*9)/5)+32)
            converted_units[2] = float(self.entry) + 273.15
        if self.entry_pos == 1:
            converted_units[0] = (((float(self.entry) - 32)*5)/9)
            converted_units[1] = self.entry
            converted_units[2] = (((float(self.entry) - 32)*5)/9) + 273.15
        if self.entry_pos == 2:
            converted_units[0] = float(self.entry) - 273.15
            converted_units[1] = ((float(self.entry) - 273.15)*1.8) + 32
            converted_units[2] = self.entry
            
        #Rounds the values and puts them in a list
        for i in range(len(converted_units)):
            rounded_values.append("{0:.3f}".format(float(converted_units[i])))

        #Sends the list of converted values back to be displayed
        return rounded_values
            

if __name__ == "__main__":
    root = Tk()
    root.title("Unit Converter")
    root.geometry("420x255")
    converter = Unit_Converter(root)
    root.mainloop()
    
