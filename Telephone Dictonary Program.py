import pickle

######################################## To Create the Binary File phone.dat
def Append():
    print("\n")
    Name=input("Enter name of the Person: ")
    RollNo=int(input("Enter Phone Number of the Person: "))
    Data=[Name,RollNo]
    while True:
        try:
            inFile=open("phone.dat","rb")
            List=pickle.load(inFile)
            inFile.close()
            break
        except:
            List=[]
            break
    List.append(Data)
    outFile=open("phone.dat","wb")
    pickle.dump(List,outFile)
    outFile.close()
  

####################### To Read and Display the Entire Binary File phone.dat    
def Display():
    print("\n")
    inFile=open("phone.dat","rb")
    List=pickle.load(inFile)
    inFile.close()
    print(List)


   
################### To Read and Search an Entry in the Binary File phone.dat        
def Search():
    Found=0
    print("\n\n<< SEARCH MENU >>\n\n")
    print("1. Search by Name.\n")
    print("2. Search by Phone Number.\n")
    Ch=int(input("Enter your choice: "))

    if(Ch==1):
        Name=input("Enter Name of the Person to be searched : ")
    else:
        RollNo=int(input("Enter Phone Number of the Person to be searched: "))

    while True:
        try:
            inFile=open("phone.dat","rb")
            List=pickle.load(inFile)
            inFile.close()
            break
        except:
            List=[]
            break


    print("\nSearched Result:")
    for L in List:
        if (Ch==1 and Name==L[0]):
            print(L)
            Found=1
        elif(Ch==2 and RollNo==L[1]):
            print(L)
            Found=1
            
    if(Found==0):
        print("No Match Found!")
                 

################# To Search and Modify an Entry in the Binary File phone.dat        
def Modify():

    FoundIndex=-1
    
    print("\n\n<< MODIFY MENU >>\n\n")
    print("1. Modify by Name.\n")
    print("2. Modify by Phone Number.\n")
    Ch=int(input("Enter your choice: "))

    if(Ch==1):
        Name=input("Enter Name of the Person to be modified: ")
    else:
        RollNo=int(input("Enter Phone Number of the Person to be modified: "))

    while True:
        try:
            inFile=open("phone.dat","rb")
            List=pickle.load(inFile)
            inFile.close()
            break
        except:
            List=[]
            break

    for i in range(len(List)):
        L=List[i]
        if (Ch==1 and Name==L[0]):
            FoundIndex=i
            RollNo=List[i][1]
            newRollNo=int(input("Enter the Modified Phone Number of the Person: "))
            List[i][1]=newRollNo
            print(RollNo," has been modified as ",newRollNo)
            break
        elif(Ch==2 and RollNo==L[1]):
            FoundIndex=i
            Name=List[i][0]
            newName=input("Enter the Modified Name of the Person: ")
            List[i][0]=newName
            print(Name," has been modified as ",newName)
            

            break


    if(FoundIndex==-1):
        print("No Match Found!")
    else:
        outFile=open("phone.dat","wb")
        pickle.dump(List,outFile)
        outFile.close() 
    

################# To Search and Delete an Entry in the Binary File phone.dat         
def Delete():

    FoundIndex=-1
    
    print("\n\n<< DELETE MENU >>\n\n")
    print("1. Delete by Name.\n")
    print("2. Delete by Phone Number.\n")
    Ch=int(input("Enter your choice: "))

    if(Ch==1):
        Name=input("Enter Name of the Person to be deleted: ")
    else:
        RollNo=int(input("Enter Phone Number of the Person to be deleted: "))

    while True:
        try:
            inFile=open("phone.dat","rb")
            List=pickle.load(inFile)
            inFile.close()
            break
        except:
            List=[]
            break

    for i in range(len(List)):
        L=List[i]
        if (Ch==1 and Name==L[0]):
            FoundIndex=i
            break
        elif(Ch==2 and RollNo==L[1]):
            FoundIndex=i
            break


    if(FoundIndex==-1):
        print("No Match Found!")
    else:
        Data=List.pop(FoundIndex)
        print(Data," has been deleted!")
        outFile=open("phone.dat","wb")
        pickle.dump(List,outFile)
        outFile.close()        


################################################### Main Menu with Choices
def Menu():
    Choice=0
    while(Choice!=6):
        print("\n\n\n")
        print("<<<<<<< BINARY FILE >>>>>>>\n")
        print("<< TELEPHONE DIRECTORY >>\n")
        print("<<<<<<< MAIN MENU >>>>>>>\n\n")
        print("1. Append a Fresh Entry.\n")
        print("2. Display Entire File.\n")
        print("3. Search an Entry.\n")
        print("4. Modify an Entry.\n")
        print("5. Delete an Entry.\n")
        print("6. Quit Program.\n\n")
        Choice=int(input("Enter your choice: "))
        if (Choice==1):
            Append()
        elif (Choice==2):
            Display()
        elif (Choice==3):
            Search()
        elif (Choice==4):
            Modify()
        elif (Choice==5):
            Delete()
        elif (Choice==6):
            print("\n\n\nThank you for using this software!\n\n\n")
        else:
            print("Invalid Input! Try AGain!")
    

############################################################# Main Program
Menu()
a=input()

            
    
        

    
    
