def create_data():
    print("\n Enter Candidate Details\n")
    name_of_candidate=input("Enter Name of the Candidate=")
    id_of_candidate=input("Enter Candidate ID=")
    email_of_candidate=input("Enter email_id of candidate=")
    college_of_candidate=input("Enter Candidate College=")
    track_of_candidate=input("Enter track of Candidate(Software,Embedded,Mechanical)=")

    f=open("data.txt","a")
    f.write(id_of_candidate+"-"+name_of_candidate+"-"+email_of_candidate+"-"+college_of_candidate+"-"+track_of_candidate+"\n")
    f.close()


