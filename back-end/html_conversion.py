#Converter Function
def conversion (tup1e):
    string=("\n<p>"+tup1e[0][0]+" at "+tup1e[0][2]+"</p>"+"\n<p>"+tup1e[0][1]+"</p>"+"\n<br>")
    for pengs in range (len(tup1e)-1):
        name=(tup1e[pengs+1][0])
        msg=(tup1e[pengs+1][1])
        time=(tup1e[pengs+1][2]) 
        string+=("\n<p>"+name+" at "+time+"</p>"+"\n<p>"+msg+"</p>"+"\n<br>")
    return string

#Tuple Input
inputA=[("B******", "Peng ting", "20/04/69"), ("H***", "peng ting", "20/04/69"), ("H***", "peng ting", "20/04/69"), ("H***", "peng ting", "20/04/69"), ("H***", "peng ting", "20/04/69")]

#Conversion Output
print(conversion(inputA))

