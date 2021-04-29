def Display_record():
    print("\n\n List of Present Records\n\n")
    f=open("data.txt","r")
    while(True):
        d=f.readline()
        l=len(d)
        if(l==0):
            break
        print(d.strip())
    f.close()