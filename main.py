import os
from create import create_data
from display import Display_record
from search import search_record_by_candidate_ID
from delete import *
from update import update_candidate_data
while True:
    print("\n 1. Add Record of Step_In Candidate")
    print("\n 2. Display Record of Step_In Candidate")
    print("\n 3. Search Record of Step_In Candidate by Candidate_ID")
    print("\n 4. Delete Record of Step_In Candidate by Candidate_ID")
    print("\n 5. Update Candidate Record")
    print("\n 6. Exit")


    n=int(input("Enter your Choice:"))
    if n==6:
        break
    elif n==1:
        create_data()
    elif n==2:
        Display_record()
    elif n==3:
        search_record_by_candidate_ID()
    elif n==4:
        delete_record()
    elif n==5:
        update_candidate_data()
    elif n==6:
        break

        
            
    
    