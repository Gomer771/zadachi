input_data = open("input.txt","r")
data=input_data.read()
data=data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
if a>=b>=c or a>=b>=c:
    a = str(a)
    data_output= open("output.txt", "w")
    data_output.write(a)
    data_output.close()
elif b>=c>=a or b>=a>=c:
    b = str(b)
    data_output= open("output.txt", "w")
    data_output.write(b)
    data_output.close()
elif c>=a>=b or c>=b>=a:
    c = str(c)
    data_output= open("output.txt", "w")
    data_output.write(c)
    data_output.close()
    input_data.close()
    