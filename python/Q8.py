def summation(sentence):
    sum_digit  =0
    for x in sentence:
        if x.isdigit()== True:
            Z = int(x)
            sum_digit=sum_digit +Z
    return sum_digit
print(summation("123ab cd45"))            
