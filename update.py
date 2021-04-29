import os
def update_candidate_data():
    h=0
    search=input("Enter Candidate ID to be Updated=")
    f=open("data.txt","r")
    temp=open("temp.txt","w")
    while True:
        t=f.readline()
        l=len(t)
        if l==0:
            break
        g=t.split('-')
        if(g[0]==search):
            h=1
            print("Current Detail is\n",t)
            print("----------------------")
            new_id=input("Want to Update Candidate ID? Ente new Details or Press Enter to Continue")
            new_name=input("Want to Update Candidate Name? Ente new Details or Press Enter to Continue")
            new_email=input("Want to Update Candidate email? Ente new Details or Press Enter to Continue")
            new_track=input("Want to Update Candidate Track? Ente new Details or Press Enter to Continue")

            if len(new_id)==0:
                new_id=g[0]
            if len(new_name)==0:
                new_name=g[1]
            if len(new_email)==0:
                new_email=g[2]
            if len(new_track)==0:
                new_track=g[4]
            temp.write("\n"+new_id+"-"+new_name+"-"+new_email+"-"+new_track)
           
        else:
            temp.write(t)
    f.close()
    temp.close()
    if(h==1):
        print("Updation Sucessful")
        os.remove("data.txt")
        os.rename("temp.txt","data.txt")
    elif(h==0):
        print("No such Record Exist: For Updation process")