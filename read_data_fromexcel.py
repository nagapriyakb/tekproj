from xlrd import open_workbook
def readdata(sheetname):
    wb=open_workbook("c:/objectn.xlsx")
    ws=wb.sheet_by_name(sheetname)
    used_rows=ws.nrows
    data={}
    for index in  range(used_rows):
        row=ws.row_values(index)
        data[row_value[0]]=(row(1),row(2))
    return data


