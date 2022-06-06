


def parameters(l,para2) :
    if para2 =="asc":
        l.sort()
        return(l)
    elif para2 == "dsc":
        l.sort(reverse = True)
        return(l)
    else :
        return(l)

   
print(parameters([1,2,3],"dsc"))



