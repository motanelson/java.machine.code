import os
print("\033c\033[47;31m\ngive me the .java file to open ? \n")
a=input().strip()
#a="Hello.java"
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
u="nop\n"
for aaa in bb:
    aaa=aaa.strip()
    if aaa!="":
        g=aaa.find("private")
        gg=aaa.find("public")
        ggg=aaa.find(" static")
        gggg=aaa.find("void")
        if (g>-1 or gg>-1 or ggg>-1) and steps==0:
            f1=open("/tmp/output.txt","w")
            f1.write(u)
            f1.close()
            os.system("rasm2 -a java -B -f /tmp/output.txt -o output.bins")
            f1=open("output.bins","br")
            i=f1.read()
            f1.close()
            f1=open("output.bin","ba")
            f1.write(i)
            f1.close()

            
            u="nop\n"
            steps=steps+1
            if steps==5:
                exit(0)
        g=aaa.find(": ")
        if g>-1:
            
            aaa=aaa[g+2:]
            u=u+aaa+"\n"
        g=aaa.find("}")
        if g>-1:
            f1=open("/tmp/output.txt","w")
            f1.write(u)
            f1.close()
            os.system("rasm2 -a java -B -f /tmp/output.txt -o output.bins")
            f1=open("output.bins","br")
            i=f1.read()
            f1.close()
            f1=open("output.bin","ba")
            f1.write(i)
            f1.close()

os.system("rasm2 -a java -b 16 -D -B -f output.bin")


