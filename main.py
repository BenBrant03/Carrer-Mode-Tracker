#Veriables
newSave = True
save = 0
#Functions
def setup(): 
  NewOrOld = input("Do you want to continue with a previous save (Y/N)")
  if NewOrOld == "y" or "Y" or "Yes" or "yes":
    print("Okay")
    newSave = False
    return newSave
  elif:
    print("Okay starting new save")
    newSave = True
    return newSave
  else
  print("There has been an error please check that you have typed in either Y or N")

def loadsave():
  f = open("savesIndex.txt","r")
  print(f.read())
  f.close()
  saveRequested = int(input("Enter the number of the save that you would like"))
  if saveRequested == 1:
    save = 1
    return save
  elif saveRequested == 2:
    save = 2
    return save
  elif saveRequested == 3:
    save = 3
    return save
  elif saveRequested == 4:
    save = 4
    return save
  elif saveRequested == 5:
    save = 5
    return save
  elif saveRequested == 6:
    save = 6
    return save
  elif saveRequested == 7:
    save = 7
    return save
  elif saveRequested == 8:
    save = 8
    return save
  else:
    print("please enter a number between 1 and 8")
#Logic
setup()

if newSave == True:
  NewSaveSetup()
elif newSave == False:
  loadSave()
else
print("There has been an error please report it to me on Github so that I can fix it")
    
    