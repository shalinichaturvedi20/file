f=open("people4.txt","r")
for i in f:
    if "delhi" in i:
        f=open("delhi.txt","a")
        f.write(i)
    elif "shimla" in i:
        f=open("shimla.txt","a")
        f.write(i)
    else:
        f=open("others.text","a") 
        f.write(i) 



# f=open("people4.txt","r")
# i=0
# while i<len(f):
#     if "delhi" in i:
#         f=open("delhi.txt","a")
#         f.write(i)
#     elif "shimla" in i:
#         f=open("shimla.txt","a")
#         f.write(i)
#     else:
#         f=open("others.text","a") 
#         f.write(i) 
#     i=i+1                          