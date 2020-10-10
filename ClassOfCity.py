import xlsxwriter as xlwt
import xlrd
f=open(r"C:\Users\Admin\PycharmProjects\untitled3\线.txt","r+",encoding='utf-8')
w=open("NicerFormat.txt","w+")
line = f.readline()
q="城市"
while line:
    t=0
    skip1=0
    skip2=0
    l=line[:]
    if line[2:4]==q or line[3:5]==q:
        ll=line[:]
        w.write(ll)
        print(ll)
        line = f.readline()
        continue


    for i in range(len(l)):
        if line[i]=='：':
            ll=line[i+1:len(l)-2]+'\n'
            for e in ll:
                if e == '自':
                    skip1 = 1
                if e == '治':
                    skip2 = 1

            if skip1 == 1 and skip2 == 1:
                ll = line[i+1:]

            w.write(ll)
            print(ll)
            t=1
            break

    if t==0:
        ll=line[:len(l)-2]+'\n'
        w.write(ll)
        print(ll)

    line = f.readline()

f.close()
w.close()

fo=open("NicerFormat.txt","r")
dict={}
index=0
line=fo.readline()
while line:
    if line=="一线城市\n":
        dict[6]=[]
        index=6
    elif line=="新一线城市\n":
        dict[5]=[]
        index=5
    elif line=="二线城市\n":
        dict[4]=[]
        index=4
    elif line=="三线城市\n":
        dict[3]=[]
        index=3
    elif line=="四线城市\n":
        dict[2]=[]
        index=2
    elif line=="五线城市\n":
        dict[1]=[]
        index=1
    else:
        dict[index].append(line[:len(line)-1])
    line = fo.readline()
fo.close()
print(dict)

loc = ("NameOfCity.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

workbook = xlwt.Workbook('ClassOfCity.xlsx')
worksheet = workbook.add_worksheet()



for i in range(sheet.nrows):
    b = 0
    sheet.cell_value(i, 0)
    for j in range(1,7):
        for value in dict[j]:
            if value==sheet.cell_value(i, 0):
                worksheet.write(i, 1, j)
                b=1
                break
        if b==1:
            break
    if b==0:
        worksheet.write(i, 1, sheet.cell_value(i, 0))


workbook.close()











