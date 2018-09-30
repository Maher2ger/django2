def give_id(typ):
    if typ == 1:
        def read_id():
            f = open("firstApp/static/id_file_c.txt", "r")
            id = int(f.read())

            print("Id wurde abgelesen")
            return id

        id = read_id()

        def write_id():
            f = open("firstApp/static/id_file_c.txt", "w")
            f.write(str(id+1))
            print()
            print("Id wurde um 1 erhoeht")




        write_id()
        print("c"+str(id))
        return("c"+str(id))

    elif typ ==2:

        def read_id():
            f = open("firstApp/static/id_file_q.txt", "r")
            id = int(f.read())

            print("Id wurde abgelesen")
            return id

        id = read_id()

        def write_id():
            f = open("firstApp/static/id_file_q.txt", "w")
            f.write(str(id+1))
            print()
            print("Id wurde um 1 erhoeht")




        write_id()
        print("c"+str(id))
        return("c"+str(id))

    else:
        return 0
