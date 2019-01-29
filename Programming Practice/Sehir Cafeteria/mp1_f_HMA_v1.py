
#Check and set your current directory
import os
cwd=os.getcwd()
print cwd

import os



class FileCreater:

    def __init__(self,var2,mylist,c):

        self.var2 = var2
        self.mylist = mylist
        self.c = c

    def CreateFile(self):
        if self.var2.get() in [1,2]:
            if self.var2.get() == 1:
                file = open("My_Food_Choices.txt","w")
                for i in range(0,self.mylist.size()):
                    # data = self.mylist.get(i)+"\n"
                    data2 =self.mylist.get(i).split(", ")
                    data3 = []
                    for l in data2:
                        data6 = l.split("\n")
                        data3.append(data6)
                    data4 = "You ordered "+data3[0][0].encode('utf-8')+" Price: "+data3[1][0].encode('utf-8')+data3[1][1].encode("utf-8")+" Calories: "+str(data3[2][0])+'\n'
                    file.write(str(data4))

                file.write("-----------------------------------\n")
                file.write("Total Calories : "+str(self.c))
                file.close()
            elif  self.var2.get() == 2:

                with open('My_Food_Choices.csv', mode='w') as file2:
                    writer = csv.writer(file2, quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    data3 =  ["You Order "," Price ", "Calories" ,"Total Calories"]
                    writer.writerow(data3)
                    for i in range(0,self.mylist.size()):
                        data2 =self.mylist.get(i).split(", ")
                        data7 = []
                        for l in data2:
                            data6 = l.split("\n")
                            data7.append(data6)
                        data4 = ([data7[0][0].encode('utf-8'),data2[1][0].encode('utf-8')+data7[1][1].encode('utf-8'),data7[2][0].encode('utf-8'),str(self.c)])
                        writer.writerow(data4)
        else:
            raise Exception('You Didnt Choose a file format.')


class GUI(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        self.root=root
        self.initUI()
    def initUI(self):
        # self.theme_bg="peach puff" # the Frames background color
        self.theme_bg='white'
    #Background
        self.root.config(bg='white') # the main background color
    #Frames
        self.label_1=Label(self.root,text='Sehir Cafeteria ',fg='red',bg='navy blue',font = ("Helvetica 9 bold italic"),width=90,height = 5)
        self.label_1.grid(row=0,column=0,pady=2,sticky=W)

        self.secondFrame = Frame(self.root)#Frame 2
        self.thirdFrame = Frame(self.root) #Frame 3

    #Frame 1
        self.firstFrame = Frame(self.root)#Frame 1
        self.firstFrame.grid(row= 2,column =0,columnspan=2,padx=2,pady=2,sticky=EW) #Frame one

        self.path= Label(self.firstFrame,text = "File path: ")
        self.path.grid(row = 1,column=0,pady=2,sticky=W)

        r = StringVar()
        r.set('FoodDB.csv')
        self.Entry1 = Entry(self.firstFrame,width=50, textvariable=r)
        self.Entry1.grid(row =1 ,column =0,padx = 70,sticky=W)

        self.diet = Label(self.firstFrame,text="Choose your Diet: ")
        self.diet.grid(row = 2,column=0,pady=5,sticky=W)

        self.var = IntVar()
        self.R1 = Radiobutton(self.firstFrame, text="1300 kcal", variable=self.var, value=1)
        self.R2 = Radiobutton(self.firstFrame, text="1800 kcal", variable=self.var, value=2)
        self.R3 = Radiobutton(self.firstFrame, text="2300 kcal", variable=self.var, value=3)
        self.R1.grid(row=2,column =0,padx =150,pady=5,sticky=W)
        self.R2.grid(row=2,column =0,padx =250,pady=5,sticky=W)
        self.R3.grid(row=2,column =0,padx =350,pady=5,sticky=W)

        self.button1 = Button(self.firstFrame,text='Continue',bg='red',command=self.Change1)
        self.button1.grid(row=5,column =0,pady=2,sticky=W)


    def Change1(self):
        # else:
        #     self.select = "Your Did not Choose a Diet"
        self.temp_choice = self.var.get()
        if self.temp_choice in  [1,2,3]:

            ### Diet part
            self.calories = " "
            if self.var.get() == 1:
                self.select = "Your Diet Choice is 1300 kcal"
                self.calories = 1300
            elif  self.var.get() == 2:
                self.select = "Your Diet Choice is 1800 kcal"
                self.calories = 1800
            elif self.var.get() == 3:
                self.select = "Your Diet choice is 2300 kcal"
                self.calories = 2300







            #### New Frame part
            self.diet2 = Label(self.firstFrame,text = self.select)
            self.diet2.grid(row=3,column =0,pady=5,sticky=W)

            ## Frame 2
            self.secondFrame.grid(row= 3,column =0,pady=2,sticky=W) #Frame one

            self.myfood = Label(self.secondFrame,text = "My Food ")
            self.myfood.grid(row =1,column=0,pady =5,padx=500,sticky=W)

            self.FoodMenu = Label(self.secondFrame,text="Food Menu")
            self.FoodMenu.grid(row =1,column=0,pady =5,padx=80,sticky=W)


            self.label_2=Label(self.secondFrame,text='Choose Your Food ',width=90)
            self.label_2.grid(row=0,column=0,pady=2,sticky=W)


            self.foodlist = Listbox(self.secondFrame,width = 40)
            self.foodlist.grid(row=2,column=0,pady=5,padx=10,sticky =W)



            self.mylist = Listbox(self.secondFrame,width = 30)
            self.mylist.grid(row=2,column=0,padx =440,pady=5,sticky=W)


            self.button3 = Button(self.secondFrame,text='Add Food',bg='red',command=self.addfood)
            self.button3.grid(row= 2,column =0,padx =315,pady=30,sticky=SW)

            self.button4 = Button(self.secondFrame,text='Remove Food',bg='red',command=self.removefood)
            self.button4.grid(row= 2,column =0,padx =305,pady=2,sticky=SW)

            self.button2 = Button(self.secondFrame,text='Continue',bg='red',command=self.Change2)
            self.button2.grid(row= 5,column =0,pady=2,sticky=W)

            self.root.geometry("635x475+300+30")

            ##Data Part
            self.path = self.Entry1.get()
            file = open(self.path, 'r+')
            file2 = file.readlines()
            liste = []
            for i in file2:
                data = i.split(","); liste.append(data)


            self.diet = {}
            self.foodadded = {}
            headline = "Choice - Price  - Calorie"
            self.foodlist.insert(END,headline)
            for i in range(1,len(liste),1):
                t = liste[i][1]+', '+str(liste[i][2])+"TL "+', '+str(liste[i][0])+" kcal"
                self.foodlist.insert(END, t)
        else:
            self.select = "Your Did not Choose a Diet"
            print "Please Choose a a Diet. "

            raise Exception('You Didnt Choose a Diet.')


    def removefood(self):
        data2 = []
        current_selection = self.mylist.curselection()
        self.mylist.delete(current_selection)



    def addfood(self):
        if self.foodlist.curselection()[0] != 0 :
            data2=self.foodlist.get(self.foodlist.curselection())
            self.mylist.insert(END,data2)
        else:
            raise Exception("That is not a valid selection.")


    def Change2(self):
        self.temp_check = self.mylist.size()
        if self.temp_check != 0:
            ## Frame 3
            Grid.columnconfigure(self.thirdFrame, 0, weight=1)
            Grid.columnconfigure(self.thirdFrame, 1, weight=1)
            self.thirdFrame.grid(row= 4,column =0,columnspan=2,padx=2,pady=2,sticky=EW) #Frame 3


            self.label_2=Label(self.thirdFrame,text='Summary and Data Saving ',width=90)
            self.label_2.grid(row=0,column=0,pady=2,sticky=W)


            self.label_3=Label(self.thirdFrame,text=self.select)
            self.label_3.grid(row=1,column=0,pady=2,sticky = W)


            self.c = 0
            for i in range(self.mylist.size()):
                data2 = self.mylist.get(i).split(", ")
                print data2
                print data2[2]
                data3 = data2[2].split(" kcal")
                print data3
                self.c= int(data3[0])+self.c
            color = 'green'

            if self.c > self.calories:
                DietChoice=''
                color = "red"
                DietChoice = 'Your Chosen Food Menu-Amount of Calories: ' + str(self.c)+ ' kcal above daily limit'
            elif self.c < self.calories:
                DietChoice = ''
                color = "green"
                DietChoice = 'Your Chosen Food Menu-Amount of Calories: ' + str(self.c) +" kcal"
            self.label_4=Label(self.thirdFrame,text=DietChoice,bg=color, width=80)
            self.label_4.grid(row=2,column=0,pady=2,padx=0,sticky = W)


            self.label_5=Label(self.thirdFrame,text='Choose File Type')
            self.label_5.grid(row=3,column=0,pady=2,sticky = W)

            self.var2 = IntVar()
            self.RR1 = Radiobutton(self.thirdFrame, text="Txt File", variable=self.var2, value=1)
            self.RR2 = Radiobutton(self.thirdFrame, text="CSV File", variable=self.var2, value=2)
            self.RR1.grid(row=3,column =0,padx =120,pady=5,sticky=W)
            self.RR2.grid(row=3,column =0,padx =200,pady=5,sticky=W)


            temp_class = FileCreater(self.var2,self.mylist,self.c)
            self.button2 = Button(self.thirdFrame,text='Save File',bg='red',command=temp_class.CreateFile)
            self.button2.grid(row= 3,column =0,padx =280,pady=2,sticky=W)

            self.root.geometry("635x585+300+20")
        else:
            raise Exception('You Didnt Choose any Food.')


def main():
     root = Tk()
     root.geometry("635x175+300+100")
     root.title("Cafeteria")
     app = GUI(root)
     root.mainloop()
main()


