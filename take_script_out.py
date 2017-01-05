## writing VAIO
#reading script
src1s_f=open("C:/Users/14rt0/Documents/English/MENTALIST_script/seazon1/The Mentalist - 1x01 - Pilot.HDTV.0TV.en.srt")
data_s=src1s_f.readlines()


# left starting listnumber and English script
for d in data_s:
    if d[0]=="0" or d=="\n" :
        index_d=data_s.index(d)
        del data_s[index_d]


# remove listnumber's \n
for dd in data_s:
    if dd[0].isdigit() and len(dd)<=5:
        data_s[data_s.index(dd)]=data_s[data_s.index(dd)].replace("\n",":")

#  list number +script  Remove only script object
ii=0
for dd in data_s:
    if dd[0].isdigit():
        data_s[ii]=dd+data_s[ii+1]
        data_s.remove(data_s[ii+1])
    ii=ii+1


# if more than 2 gyou  -->one object
ii=0
for dd in data_s:
    if not dd[0].isdigit():
        data_s[ii-1]=data_s[ii-1].replace("\n"," ")
        data_s[ii-1]=data_s[ii-1]+dd
        data_s.remove(data_s[ii])
    ii=ii+1
print data_s
# write file
f=open("C:/Users/14rt0/Desktop/s/script.txt","w")
f.writelines(data_s)
f.close()
