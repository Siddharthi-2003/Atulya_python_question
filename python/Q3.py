def parameters(int1 , operators ,int2):
    if operators == "*"  :
        return int1*int2
    elif operators == "+" :
        return int1+int2
    elif operators == "-" :
        return  int1-int2
    elif operators == "/" :
        return int1/int2
    else :
        return int1 or int2
print(parameters(int1=3,operators= "or", int2=2))      
         
         
        
     