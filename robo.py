# pip install RoboBrowser
# apt-get install python3-tk
# http://robobrowser.readthedocs.io/en/latest/

# pyinstaller --onefile --windowed robo.py

import tkinter
from robobrowser import RoboBrowser
from requests import Session
import re
import sys
from collections import Counter


class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Quoi ?")

        button = tkinter.Button(self,text=u"Chercher !",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0, columnspan=2)

        self.labelInfoVariable = tkinter.StringVar()        
        label = tkinter.Label(self,textvariable=self.labelInfoVariable,
                              anchor="w",justify="left", fg="black",bg="grey")
        label.grid(column=0,row=2,columnspan=3,sticky='EW')
        self.labelInfoVariable.set(u"Annonces en Ille et Vilaine")
        
        self.listVariable = tkinter.StringVar();
        scrollbar = tkinter.Scrollbar(self, orient="vertical")        
        scrollbar.grid(row=3, column=2, sticky="NS")
        listbox = tkinter.Listbox(self, fg="white",bg="black", height=24, listvariable = self.listVariable, yscrollcommand=scrollbar.set)
        listbox.grid(row=3, column=0, columnspan=2, sticky='NESW')
        scrollbar["command"] = listbox.yview
        
        self.labelTitleResultVariable = tkinter.StringVar()        
        label = tkinter.Label(self,textvariable=self.labelTitleResultVariable,
                              anchor="w",justify="left", fg="black",bg="grey")
        label.grid(column=0,row=4,columnspan=3,sticky='EW')
        self.labelTitleResultVariable.set(u"Mots courants")
        
        self.labelResultVariable = tkinter.StringVar()        
        label = tkinter.Label(self,textvariable=self.labelResultVariable,
                              anchor="w",justify="left", fg="black")
        label.grid(column=0,row=5,columnspan=3,sticky='EW')
        self.labelResultVariable.set(u"...")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()      
        self.geometry("1000x500") 
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)       
     
    def SearchLbc(self, q):
     print("search : "+q)
     session = Session()
     browser = RoboBrowser(session=session, user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101  Firefox/40.1')
     browser.open("https://www.leboncoin.fr/annonces/offres/bretagne/ille_et_vilaine?th=1&q="+q+"&it=1&f=p")
     results = browser.find_all("section", attrs={"class":"item_infos"})
     i=0
     search_result=[]
     for result in results:
      if result.find("h2") != None:
       print("-----------"+str(result))
       i=i+1
       title = result.h2.text.strip()
       price=""
       if result.find("h3") != None: 
        price = result.h3.text.strip()
       location = str(result.findAll("p", attrs={"itemprop":"availableAtOrFrom"})[0].text.strip().replace(" ","").replace("\n",""))
       date = result.aside.p.text.strip()
       new_result = str(i) + " -|- " + title+" -|- "+price+" -|- "+location+" -|- "+date
       search_result.append(new_result)
     print("search done : "+str(i))
     return search_result
     
    def FindWordsCounts(self, results):
        words = []
        print("findSecondWord")
        for result in results:
         title = result.split(" -|- ")[1]
         print(result.split(" -|- ")[1])
         words.extend(title.split(" "))
        words.remove("-")
        words.remove("de")
        words.remove(str(self.entryVariable.get()))
        counts = Counter(words)        
        print("counts" + str(counts))
        return counts
     
    def OnButtonClick(self):
        print("onclick text = "+self.entryVariable.get())
        try:
            print("try to get results")
            results = self.SearchLbc(str(self.entryVariable.get()))
            if not results:
             results = "aucun resultat"
            else:
             for result in results:
              print(result)
        except:
            print("except")
            results = "error : " + str(sys.exc_info()[0])
        finally:
            print("finally")
            self.listVariable.set(results)
            self.labelResultVariable.set("done")
            self.entry.focus_set()
            self.entry.selection_range(0, tkinter.END)

    def OnPressEnter(self,event):
        print("onenter text = "+self.entryVariable.get())
        analyze = "done"
        try:
            print("try to get results")
            results = self.SearchLbc(str(self.entryVariable.get()))
            if not results:
             results = "aucun resultat"
            else:
             analyze = str(self.FindWordsCounts(results).most_common(8))
        except:
            print("except")
            results = "error : "+ str(sys.exc_info()[0])
        finally:
            print("finally")
            self.listVariable.set(results)
            self.labelResultVariable.set(analyze)            
            self.entry.focus_set()
            self.entry.selection_range(0, tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('mon appli leboncoin')
    app.mainloop()
    


