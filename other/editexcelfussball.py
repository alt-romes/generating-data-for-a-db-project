import openpyxl

wb = openpyxl.load_workbook(filename="fsexcel.xlsx")
for (i, sheet) in enumerate(wb):
    if i > 1:
        print(sheet)
        for (j, cell) in enumerate(sheet["C"]):
            if j > 0 and j < len(sheet["C"])-1:
                n = cell.value
                n = (n if len(n.split(" "))<2 else (n.split(" ")[0][0]+". "+n.split(" ")[1]))
                print(j+1, ":", n)
                sheet["C"+str(j+1)] = n
            elif j == len(sheet["C"])-1:
                sheet["C"+str(j+1)] = ""

wb.save(filename="fsexcel.xlsx")