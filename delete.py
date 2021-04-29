import os
def delete_record():
    delete=input("Enter Candidate ID to be Deleted=")
    f=open("data.txt","r")
    temp=open("temp.txt","w")
    h=1
    flag=0
    while True:
        t=f.readline()
        l=len(t)
        if l==0:
            break
        g=t.split('-')
        if g[0]!=delete:
            temp.write(t)
        if g[0]==delete:
            h=1
    f.close()
    temp.close()
    if h==1:
        print("Record Deleted Sucessfully")
        os.remove("data.txt")
        os.rename("temp.txt","data.txt")
    elif h==0:
        print("Record Not Found!! Deletion Failed")