import os

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import testModel, testModel2


@csrf_exempt
def index(request):
    tm = testModel.objects.first()
    if not tm:
        tm = testModel(testField='', testField2=0)
        tm.save()
    fileValue = readFile()
    tm2 = testModel2.objects.count()
    if request.method == 'POST':
        if 'file' in request.POST:
            writeFile(fileValue + 1)
            fileValue = readFile()
        elif 'DB' in request.POST:
            tm.testField2 = tm.testField2 + 1
            tm.save()
        elif 'HRW' in request.POST:
            for x in range(100):
                heavy_read_write()
    context = {
        "HeavyReadWriteCount": int(tm2),
        "DBValue": int(tm.testField2),
        "FileValue": int(fileValue),
        "FilePath": str(os.environ.get("TEXTFILE_URL", './DjangoTestWriteFile.txt'))
    }
    return render(request, 'index.html', context)


def heavy_read_write():
    newData = testModel2(
        testField="TESTING 12" * 1000, # 10 * 1000
        testField2="TESTING" * 10000,
        testField3=(f"" * 1000).encode('utf-8')
    )
    newData.save()

def readFile():
    filePath = os.environ.get("TEXTFILE_URL", './DjangoTestWriteFile.txt')
    if os.path.exists(filePath):
        with open(filePath, 'r') as file:
            val = file.readline()
    else:
        val = 0
    return int(val)

def writeFile(val):
    filePath = os.environ.get("TEXTFILE_URL", './DjangoTestWriteFile.txt')
    with open(filePath, 'w+') as file:
        file.write(str(val))



