def sq_tables(m):
    for row in range(1,m+1):
        print(row,end="\t")
    print()
    print("----+-----+-----+------+------+\n")
    for column in range(2,m+1):
        for pro in range(1,m+1):
            print(column*pro,end="\t")
        print("\n")    
