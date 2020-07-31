import xlsxwriter as xlwt
import xlrd
### Generate dummy variables from catagoriacal data
### output as xlsx 

""""input file forbids label, only allow one column
    dict={dummy_var_name:[list of possible values for the value 1
                                    (other values correspond to 0)]}"""
def dummy_gen(dict):
    
    wb = xlrd.open_workbook("input.xlsx")
    sheet = wb.sheet_by_index(0)
    workbook = xlwt.Workbook('output.xlsx')
    worksheet = workbook.add_worksheet()
    o_col=0
    for i in dict:
        worksheet.write(0, o_col, i)
        o_col+=1
    for i in range(sheet.nrows):
        index=-1
        for j in dict:
            index+=1
            for k in dict[j]:
                if sheet.cell_value(i, 0)==k:
                    worksheet.write(i+1, index, 1)
                    break
                else:
                    worksheet.write(i+1, index, 0)
    workbook.close()
    return

dict={"WANTHK":[1,4]}
dummy_gen(dict)

