from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd

def home(request):
    if request.method == 'POST' and request.FILES.get('schedule'):
        excel_file = request.FILES['schedule']
        fs = FileSystemStorage()
        filename = fs.save(excel_file.name, excel_file)
        file_path = fs.path(filename)

        # Read the Excel file
        df = pd.read_excel(file_path)

        # Convert to HTML (you’ll later make this a nicer timetable)
        table_html = df.to_html(classes='table table-striped', index=False)

        return render(request, 'timetable/timetable.html', {'table': table_html})

    return render(request, 'timetable/home.html')