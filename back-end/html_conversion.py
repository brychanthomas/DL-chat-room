#Converter Function
def conversion (tup1e):
    string=""
    for pengs in range (len(tup1e)):
        name=(tup1e[pengs][0])
        msg=(tup1e[pengs][1])
        time=(tup1e[pengs][2]) 
        string+=("\n<p>"+name+" at "+time+"</p>"+"\n<p>"+msg+"</p>"+"\n<br>")
    return string

