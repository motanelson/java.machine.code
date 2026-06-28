import os
print("\033c\033[47;31m\ngive me the .java file to open ? \n")
a=input().strip()
a="Hello.java"
b=a.find(".")
c=a
if b>-1:
    c=a[:b]+".class"

os.system("javac --release 25 "+a)
os.system("javap -c -private "+c+" >/tmp/output.txt")
f1=open("/tmp/output.txt","r")
aa=f1.read()
f1.close()
bb=aa.split("\n")
steps=0
for aaa in bb:
    aaa=aaa.strip()
    if aaa!="":
        g=aaa.find("private")
        gg=aaa.find("public")
        ggg=aaa.find(" static")
        gggg=aaa.find("void")
        if (g>-1 or gg>-1 or ggg>-1) and steps==0:
            aaa=aaa.replace("private","")
            aaa=aaa.replace("public","")
            aaa=aaa.replace("static","")
            aaa=aaa.replace("class","")
            aaa=aaa.replace("void","")
            aaa=aaa.replace("{","")
            aaa=aaa.strip()
            print("\n--------------------\n")
        g=aaa.find(": ")
        if g>-1:
           
            aaa=aaa[g+2:]
            print(aaa)
        g=aaa.find("}")
        if g>-1:
            print("\n---------------------\nend")

