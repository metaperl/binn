#!/usr/bin/env python


import  shutil
import datetime


def new_filename():
    return 'timesheet-{0}.xls'.format(datetime.date.today().isoformat())


shutil.copy(
    'default.xls', new_filename())

from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook(new_filename(), formatting_info=True)
wb = copy(rb)
s = wb.get_sheet(0)
print s

s.write(3, 4, 'Terrence Brannon')

wb.save('hah.xls')
