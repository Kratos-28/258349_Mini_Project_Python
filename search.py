def search_record_by_candidate_ID():
    search_candidate_id=input("Enter Candidate ID=")
    f=open("data.txt","r")
    flag=0
    while True:
        t=f.readline()
        l=len(t)
        if l==0:
            break
        g=t.split('-')
        if(g[0]==search_candidate_id):
            print("\n Record Found ")
            print("Candidate_ID =",g[0])
            print("Candidate Name =",g[1])
            print("Email_ID =",g[2])
            print("Candidate College =",g[3])
            print("Candidate Track =",g[4])
            flag=1
            break
    if flag==0:
        print("Record Not Found")
    f.close()
            