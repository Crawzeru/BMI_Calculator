from tkinter import *

#window
window =Tk()
window.title("BMI calculator")
window.minsize(200,200)
def calculate_button():
    global result_label
    weight=(weight_entry.get())
    height=(height_entry.get())
    if weight=="" or height == "":
        result_label.config(text="Enter both weight and height")
    else:
        try:
            bmi=float(weight)/((float(height)/100)**2)
            result_bmi=round(bmi,2)
            if bmi<=18.4:
                condution="Underweight"
            elif bmi >18.4 and bmi <24.9:
                condution="Normal"
            elif bmi >24.9 and bmi <40:
                condution="Overweight"
            else:
                condution="Obese"
            result_label.config(text=f"Your BMI is:{result_bmi}.You are {condution}. ")
        except:
            result_label.config(text="Enter valid number!")


#label-Weight

weight_label=Label(text="Enter your weight(kg)")
weight_label.pack()

#entry-weight
weight_entry=Entry()
weight_entry.pack()

#label-Height
height_label=Label(text="Enter your height(cm)")
height_label.pack()
#entry-height
height_entry=Entry()
height_entry.pack()
#button
calculate_button=Button(text="Calculate",command=calculate_button)
calculate_button.pack()
#result-label
result_label = Label(text=" ")
result_label.pack(side=BOTTOM)


window.mainloop()