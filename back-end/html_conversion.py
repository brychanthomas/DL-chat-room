import time

#Converter Function
def conversion (tup1e):
    string=""
    for pengs in range (len(tup1e)):
        name=(tup1e[pengs][0])
        msg=(tup1e[pengs][1])
        local_time = time.localtime(tup1e[pengs][2])
        timestring=time.strftime('%Y/%m/%d %H:%M:%S', local_time)
        string+=("\n<p>"+name+" at "+timestring+"</p>"+"\n<p>"+msg+"</p>"+"\n<br>")
    return string


