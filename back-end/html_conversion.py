from datetime import datetime

#Converter Function
def conversion (tup1e):
    string=""
    for pengs in range (len(tup1e)):
        name=(tup1e[pengs][0])
        msg=(tup1e[pengs][1])
        time=datetime.utcfromtimestamp(tup1e[pengs][2]).strftime('%Y/%m/%d %H:%M:%S')
        string+=("\n<p>"+name+" at "+time+"</p>"+"\n<p>"+msg+"</p>"+"\n<br>")
    return string

