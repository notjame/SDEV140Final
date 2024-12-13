'''
Name: Calorie Calculator
Author: James Rogers
Version: 1.0
Summary: This is a basic calculator that can be used to calculate calories burned during a workout, with a encouraging image to show what the
user looks like after their workout.
'''
from breezypythongui import EasyFrame
from tkinter import PhotoImage

class CalorieCalculator(EasyFrame):
    def __init__(self):#setting the window and buttons up
        #setting Frame up
        EasyFrame.__init__(self, title="Calorie Calculator") #adding a title and initializing the window
        self.setResizable(True)
        self.setSize(600,700)

        #initializing the logo
        imageLabel1 = self.addLabel(text="",row=0,column=1,sticky="NSEW") #making photo lavel
        self.image1 = PhotoImage(file="logo.png") 
        imageLabel1["image"] = self.image1 #putting the image in where there label is
        
        #initializing all labels and input boxes (fields)
        self.addLabel(text="Weight (in pounds):", row=1, column=0) #weight label
        self.addLabel(text="Intensity (1, 2, or 3):", row=2, column=0) #intensity label
        self.addLabel(text="Calories Burned: ", row=4, column=0) #calories burned label
        self.addLabel(text="Time (in minutes):", row=3, column=0) #time label
        self.WeightBox = self.addIntegerField(value=0, row=1, column=2)#weight inputbox
        self.IntensityBox = self.addIntegerField(value=0, row=2, column=2) #intensity inputbox
        self.TimeBox = self.addIntegerField(value=0, row=3, column=2) #time inputbox
        self.CaloriesBox = self.addFloatField(value=0.0, row=4, column=2, precision=2, state="readonly") #calories burned outputbox
        
        #initializing image label and image
        imageLabel2 = self.addLabel(text="",row=5,column=1,sticky="NSEW") #making photo lavel
        self.image2 = PhotoImage(file="arnold.png") 
        imageLabel2["image"] = self.image2 #putting the image in where there label is

        #initializing buttons
        self.addButton(text="Calculate", row=6, column=0, columnspan=2, command=self.convert) #conversion button
        self.addButton(text="Reset", row=6, column=1, columnspan=2, command=self.reset) #reset button
        self.addButton(text="Exit", row=6, column=2, columnspan=2, command=self.closeWindow) #Exit button
    
    def convert(self): 
        #conversion function

        MET = 0 #initializing MET variable (MET is the Metabolic rate. It is the rate of energy expended per unit of time.) Later used in Calories burned calc
        try:
            pounds = self.WeightBox.getNumber() #gets the number from the weightbox and turns it into an accessible variable
        except:
            self.messageBox(title="ERROR", message="Weight input must be a whole number.") #error window pops up incase of inproper input
        if pounds > 0:
            kilos = pounds * 0.4535924
        else:
            self.messageBox(title="Error", message="Please enter a weight greater than 0") #input validation for weight (noone can weigh negative pounds)
            return
        
        try:
            intensity = self.IntensityBox.getNumber() #gets the number from the intensity box and turns it into an accessible variable
        except:
            self.messageBox(title="ERROR", message="Intensity input must be 1, 2, or 3.")#error window pops up incase of inproper input
        
        try:
            time = self.TimeBox.getNumber() #gets the number from the time box and turns it into an accessible variable
        except:
            self.messageBox(title="ERROR", message="Time input must be a whole number.") #input validation
        if time <= 0:
            self.messageBox(title="Error", message="Please enter a time greater than 0") #error window pops up incase time is negative
            return


        if intensity == 1: #converting intensity to MET for formula
            MET = 3
        elif intensity == 2:
            MET = 4.5
        elif intensity == 3:
            MET = 6
        else:
            self.messageBox(title="Error", message="Please enter a valid intensity (1, 2, or 3).") #input validation
            return 

        calories_burned = MET * kilos * (time / 60) #formula for calories burned
        

        self.CaloriesBox.setNumber(calories_burned) #setting the calories burned box to calories_burned variable
        if calories_burned < 300: #this process changes the image displayed depending how many calories burned
            self.image2["file"] = "cbum.png" 
        elif calories_burned > 300 and calories_burned < 600:
            self.image2["file"] = "samsulek.png"
        elif calories_burned >= 600:
            self.image2["file"] = "ronnie.png"
        else:
            self.image2["file"] = "arnold.png"
        

    def reset(self):
        # Reset all fields to default values
        self.WeightBox.setNumber(0)
        self.IntensityBox.setNumber(0)
        self.TimeBox.setNumber(0)
        self.CaloriesBox.setNumber(0.0)
        self.image2["file"] = "arnold.png"
    
    def closeWindow(self):
        # Close the window
        exit()

    
    
if __name__ == "__main__":
    CalorieCalculator().mainloop()
