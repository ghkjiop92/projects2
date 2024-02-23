from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

import os
#import pandas as pd
#df = pd.read_csv('inventory.csv', encoding='cp949')

#def download_csv(request):
    # Update the path to reflect the correct directory structure
    #file_path = os.path.join('C:\\projects', 'inventory.csv')

    #with open(file_path, 'rb') as file:
        #response = HttpResponse(file.read(), content_type='text/csv')
        #response['Content-Disposition'] = 'attachment; filename="inventory.csv"'
        #return response
import csv

file =open("inventory.csv", newline='')
reader = csv.reader(file)
for i, line in enumerate(reader):
    if i ==2:
        break
    print(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],sep='/')
    print('데이터출력')
def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")




