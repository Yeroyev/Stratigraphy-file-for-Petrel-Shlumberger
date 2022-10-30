# -*- coding: utf-8 -*-

import xlrd
import xlwt
import sys
from datetime import datetime, date, time

file = xlrd.open_workbook('Example.xls', formatting_info=True) #Название загружаемого файла
sheet = file.sheet_by_index(0)

with open(r'Example_out.txt', 'a', encoding='utf-8') as out: #Название выгружаемого файла
    out.write('Well' + '\t' + 'Surface' + '\t' + 'MD' + '\t' + 'missing' + '\t' + 'Type' + '\n')
    for i in range(1, sheet.ncols):
        for j in range(1, sheet.nrows):
            well = sheet.row_values(0)[i]
            strt = sheet.row_values(j)[0]
            number = sheet.row_values(j)[i]
            if number != '':
                out.write(str(well) + '\t' + str(strt) + '\t' + str(number) + '\t' + str(-999) + '\t' + 'HORIZON' + '\n')
            else:
                continue
out.close()