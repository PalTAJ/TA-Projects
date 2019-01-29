from Tkinter import *
import urllib2
from bs4 import BeautifulSoup
import docclass
# from collections import OrderedDict
from PIL import ImageTk, Image
import random

class BooksTool(Frame):
    def __init__(self, parent):
        self.parent=parent
        Frame.__init__(self,parent)
        self.initUI()

    def initUI(self):

        self.parent.config(bg="wheat2") ## Main Frame color
        # -------------------------- GUI Header
        self.frame1 = Frame(self.parent)  # frame 1 to containt Pictures and Headline
        self.frame1.grid(row=0,column=0,padx=5,pady=5)
        self.frame1.config(bg="White")

        self.img = Image.open('books.jpg')
        self.img = self.img.resize((150, 135), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)

        self.label1 = Label(self.frame1,image=self.img,bg="White")
        self.label1.grid(row=0,column=0)

        self.label2 = Label(self.frame1,text="Sehir Books Tool v1.01",bg ="White", font=("Helvetica", 16))
        self.label2.grid(row=0,column=1,padx=82,pady=5)

        self.label3 = Label(self.frame1, image=self.img, bg="White")
        self.label3.grid(row=0, column=2)

        # --------------------------- GUI Widgets

        self.frame2 = Frame(self.parent,bg='White')
        self.frame2.grid(row=1,column=0,padx=5,pady=5)

        self.label4 = Label(self.frame2, text = "Genres File Path: ",bg='White')
        self.label4.grid(row=0, column=0,padx=5,pady=5)

        self.entry =  Entry(self.frame2,width=50)
        self.entry.grid(row=0,column=1,padx=5,pady=5)
        self.entry.insert(0, "Genres.txt")

        self.fetch_des_button = Button(self.frame2, text="Fetch and Train", width=15,command=self.data_Fetch_Train)
        self.fetch_des_button.grid(row=1,column=0,padx=5,pady=5)

        self.label5 = Label(self.frame2, text = "< stopping >",fg='black',bg='red',height=1)
        self.label5.grid(row=1, column=1,padx=5,pady=5)




    ## this function reads the genres file return a list of names and urls of the genres.
    def GetgenresFromFile(self):
        filename = str(self.entry.get())
        liste = list()
        file = open(filename, 'r+')
        file = file.readlines()
        for i in file:
            line = i.split(',');
            name = line[0];
            url = line[1]  # name:Art,url:/genres/art
            name = name.split(':')[1];
            url = url.split(':')[1];
            url = url.strip('\n')
            liste.append([name, url])
            # print name," _ ",url
        return liste

    # self.GetgenresFromFile('Genres.txt')
    ## This Function takes Links and returns a dictionary that has ooutput such as below:
    #{Genre:[id,name of book], and so on for every genre}, we have 29 genre
    def Crawler(self,data):
        mainLink = "https://www.goodreads.com"
        # for i in data:
        Books = {}
        for i in data:
            genre = i[0];
            directory = i[1]
            fullLink = mainLink + directory
            print fullLink
            soup = BeautifulSoup(urllib2.urlopen(fullLink), "html.parser")
            depa = soup.findAll('body')
            # Books = {}
            BooksNames = []
            c = 1
            for part2 in depa:
                r2 = part2.findAll('div', {'class': 'content'})
                for part3 in r2:
                    r3 = part3.findAll('div', {'class': 'mainContentContainer'})
                    for part4 in r3:
                        r4 = part4.findAll('div', {'class': 'mainContentFloat '})
                        for part5 in r4:
                            r5 = part5.findAll('div', {'class': 'leftContainer'})
                            for part6 in r5:
                                r6 = part6.findAll('div', {'class': 'leftAlignedImage bookBox'})
                                for part7 in r6:
                                    r7 = part7.findAll('a')
                                    book = str(r7[0]).split('alt=')  # ; book = book[1].split('"')[0]
                                    book = book[1].split('class')[0].strip('"');
                                    book = book[:-2]
                                    book = book.strip("'")
                                    BooksNames.append([genre + str(c), book])
                                    c += 1
            Books[genre] = BooksNames
        return Books

    def data_Fetch_Train(self):
        self.parent.geometry("780x595+200+50")

        # GUI For Fetching and Training

        self.frame3 = Frame(self.parent,bg = 'wheat2')
        self.frame3.grid(row=2,column=0,sticky=W,stick=W)

        self.label6 = Label(self.frame3, text = "Individual Books",fg='black', font=("Helvetica", 12),bg="wheat2")
        self.label6.grid(row=0, column=0,padx=5,stick=S,sticky=S)

        self.label7 = Label(self.frame3, text = "Top 3 Estimates ",fg='black', font=("Helvetica", 12),bg="wheat2")
        self.label7.grid(row=0, column=1,padx=5,stick=S,sticky=S)


        self.listBox1 = Listbox(self.frame3, width=50, height=10, font=("Helvetica", 8))
        self.listBox1.grid(row=1,rowspan=5,column=0,pady=5,padx=140)
        self.listBox1.bind('<<ListboxSelect>>',self.listClicked)

        self.labelp1 = Label(self.frame3,text="one ",font=("Helvetica", 10))
        self.labelp1.grid(row=2,column=1,padx=5)

        self.labelp2 = Label(self.frame3,text=" Two",font=("Helvetica", 10))
        self.labelp2.grid(row=3,column=1,padx=5)

        self.labelp3 = Label(self.frame3,text=" Three",font=("Helvetica", 10))
        self.labelp3.grid(row=4,column=1,padx=5)

        ################# Analysis part GUI

        self.frame4 = Frame(self.parent,bg = 'wheat2')
        self.frame4.grid(row=3,column=0)

        self.l8 = Label(self.frame4,text = 'Accuracy analysis based \n on Genres: ',font=("Helvetica", 10),bg = 'wheat2')
        self.l8.grid(row=0,column=0)

        self.listbox2 = Listbox(self.frame4, height=8)
        self.listbox2.grid(row=1,column=0)
        self.listbox2.bind('<<ListboxSelect>>',self.analysis)

        self.text = Text(self.frame4, height=8, width=30)
        self.text.grid(row=1,column=1)


        # Fetching part

        self.clasifier = docclass.classifier(docclass.getwords)
        data = self.GetgenresFromFile()
        data = [data[0],data[1]]
        self.BooksDATA = self.Crawler(data)
        print self.BooksDATA



        # Training Part

        self.listboxinfo = []
        for key, value in self.BooksDATA.items():
            # print key
            self.listbox2.insert(END,key)
            for val in value:
                print key, " --> ", val[1]
                self.listboxinfo.append(val[0]+'- '+val[1]+'-'+key)
                self.clasifier.train(val[1], key)

        random.shuffle(self.listboxinfo, random.random)
        for i in self.listboxinfo:
            self.listBox1.insert(END,i)
        self.label5.config(text="< Trained >",fg='black',bg='Gold')

    def analysis(self,event):
        self.text.delete(1.0, END)
        index = self.listbox2.curselection()
        choice = self.listbox2.get(index); choice2 = "Genre: "+choice+'\n'
        GenresBooks = self.BooksDATA[choice] ; totalB = "Total Number Of Books: "+str(len(GenresBooks))
        self.text.insert(END, choice2)
        self.text.insert(END,totalB)

        predictedGenre = []
        Books = self.BooksDATA[choice]
        for i in Books:
            self.selectedBook = i[1]
        # categories = self.clasifier.categories()
            estimates = []
            for cat in self.clasifier.categories():
                prob = 0
                for word in docclass.getwords(self.selectedBook):
                    prob += self.clasifier.fprob(word, cat, default_prob=0)
                if prob != 0:
                    estimates.append([cat, prob])
            estimates = sorted(estimates, key=lambda x: x[1], reverse=True);estimates = estimates[0];predictedGenre.append(estimates)
        print predictedGenre

        c = len(self.BooksDATA[choice])
        wrong = 0

        for j in predictedGenre:
            if j[0] != choice:
                c-=1
                wrong +=1
        correct = '\nCorrectly predicted Books: '+str(c)+'\n'
        wrongg = 'Wrongly Predicted Books: '+str(wrong)+'\n'
        accuracy = 'Accuracy: '+str((float(c)/len(self.BooksDATA[choice]))*100)

        self.text.insert(END, correct)
        self.text.insert(END,wrongg);self.text.insert(END,accuracy)

    def listClicked(self,event):

        self.labelp1.config(text=' ',bg='wheat2');self.labelp2.config(text=' ',bg='wheat2');self.labelp3.config(text=' ',bg='wheat2')

        index= self.listBox1.curselection()
        temp = self.listBox1.get(index[0]);catt = temp.split('-')[2];temp = temp.split('-')[1] ; temp = temp[1:]

        self.selectedBook = temp
        # categories = self.clasifier.categories()
        estimates = []
        for cat in self.clasifier.categories():
            prob = 0
            for word in docclass.getwords(self.selectedBook):
                prob += self.clasifier.fprob(word, cat, default_prob=0)
            if prob != 0:
                    estimates.append([cat, prob])

        estimates = sorted(estimates, key=lambda x: x[1], reverse=True)
        if len(estimates) == 1:


            line = str(estimates[0][0])+" -->"+str(estimates[0][1])
            if estimates[0][0] == catt:
                self.labelp1.config(text=line,bg='green')
            else:
                print estimates
                self.labelp1.config(text=line,bg='red')

        elif len(estimates)==2 :


            line = str(estimates[0][0])+" -->"+ str(estimates[0][1])
            line2 = str(estimates[1][0])+" -->"+ str(estimates[1][1])
            if estimates[0][0] == catt:
                self.labelp1.config(text=line,bg='green')
            else:
                print estimates
                self.labelp1.config(text=line,bg='red')

            if estimates[1][0] == catt:
                self.labelp2.config(text=line2,bg='green')
            else:
                self.labelp2.config(text=line2,bg='red')

        elif len(estimates)==0:
            print 'wait what'

        else:

            line = str(estimates[0][0])+" -->"+ str(estimates[0][1])
            line2 = str(estimates[1][0])+" -->"+ str(estimates[1][1])
            line3 = str(estimates[2][0])+" -->"+ str(estimates[2][1])

            if estimates[0][0] == catt:
                self.labelp1.config(text=line,bg='green')
            else:
                print estimates
                self.labelp1.config(text=line,bg='red')

            if estimates[1][0] == catt:
                self.labelp2.config(text=line2,bg='green')
            else:
                self.labelp2.config(text=line2,bg='red')

            if estimates[2][0] == catt:
                self.labelp3.config(text=line3,bg='green')
            else:
                self.labelp3.config(text=line3,bg='red')

    # def analysis_function(self, event):
    #     try:
    #         self.analysis_text.delete(1.0, END)
    #     except:
    #         pass
    #     analysis_code = self.programs_textbox.get(self.programs_textbox.curselection())
    #     wrong_analysis_dict = {}
    #     analysis_counter = 0
    #     for course in self.courseData:
    #         course_code = course.split(' ')[0]
    #         if course_code == analysis_code:
    #             analysis_counter += 1
    #             estimates = []
    #             try_data = self.courseData[course]
    #             for cat in self.clasifier.categories():
    #                 prob = 0
    #                 for word in docclass.getwords(try_data):
    #                     prob += self.clasifier.fprob(word, cat, default_prob=0)
    #                 if prob != 0:
    #                     estimates.append((cat, prob))
    #             estimates = sorted(estimates, key=lambda x: x[1], reverse=True)
    #             print estimates
    #             if estimates[0][0] != analysis_code:
    #                 wrong_analysis_dict[course] = estimates[0]
    #     txt = ''
    #     accuracy = (1.0 * (analysis_counter - len(wrong_analysis_dict)) / analysis_counter) * 100
    #     txt += 'Accuracy: {}%  \n Total Number of Courses: {} \n Accurately Classified: {} \n Inaccurate Classification: {} \n' \
    #         .format("{0:.2f}".format(round(accuracy, 2)), analysis_counter, analysis_counter - len(wrong_analysis_dict),
    #                 len(wrong_analysis_dict))
    #     mistakes = wrong_analysis_dict.keys()
    #     mistakes.sort()
    #     for mistake in mistakes:
    #         txt += '	{} --> {} \n'.format(mistake, wrong_analysis_dict[mistake][0])
    #     self.analysis_text.insert(END, txt)



def main():
    root = Tk()
    root.title("Books Tool v1.01")
    # root.geometry("780x555+200+200")
    root.geometry("710x280+200+200")
    app = BooksTool(root)
    root.mainloop()
main()