#!/usr/bin/python3

def main():
    ## create an empty list
    emptylist = []

    emptylist.extend("192.168.102.55")

    print(emptylist)


    myotherlist = []

    myotherlist.append("192.168.102.55")

    print(myotherlist)

    networklist = ["cisco", "juniper"]
    emptylist.extend(networklist)

    #get more focus on how extend works
    print(emptylist)



if __name__== "__main__":
    main()
