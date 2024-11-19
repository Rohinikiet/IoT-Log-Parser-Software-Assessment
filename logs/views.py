import os
import time
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .forms import LogFileForm
from .parser import parse_logs
import matplotlib.pyplot as plt
import io

def upload_log(request):
    if request.method == 'POST':
        form = LogFileForm(request.POST, request.FILES)
        if form.is_valid():
            start_time = time.time()

            file = request.FILES['file']
            if not settings.MEDIA_ROOT:
                raise ValueError("MEDIA_ROOT is not set in settings.")
            file_path = os.path.join(settings.MEDIA_ROOT, file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            file_ingestion_time = time.time() - start_time

            parse_start_time = time.time()
            json_df, base64_df, error_logs = parse_logs(file_path)
            parse_time = time.time() - parse_start_time

            json_df.columns = json_df.columns.str.strip()

            if 'event' not in json_df.columns:
                return HttpResponse(f"Error: 'event' column not found in the log data. Found columns: {json_df.columns.tolist()}", status=400)

            if not settings.STATIC_ROOT:
                raise ValueError("STATIC_ROOT is not set in settings.")
            event_dist_path = os.path.join(settings.STATIC_ROOT, 'images', 'event_distribution.png')
            os.makedirs(os.path.dirname(event_dist_path), exist_ok=True)  

            plot_start_time = time.time()
            plot_event_distribution(json_df, event_dist_path)
            plot_time = time.time() - plot_start_time

            total_time = time.time() - start_time

            print(f"File Ingestion Time: {file_ingestion_time:.2f} seconds")
            print(f"Log Parsing Time: {parse_time:.2f} seconds")
            print(f"Plot Generation Time: {plot_time:.2f} seconds")
            print(f"Total Processing Time: {total_time:.2f} seconds")

            data_to_visualization_time = plot_time + parse_time  

            return render(request, 'logs/dashboard.html', {
                'json_table': json_df.head().to_html(classes="table table-striped"),
                'base64_table': base64_df.head().to_html(classes="table table-striped"),
                'error_logs': error_logs[:10],
                'event_dist_path': f'/static/images/event_distribution.png',
                'file_ingestion_time': f"{file_ingestion_time:.2f} seconds",
                'parse_time': f"{parse_time:.2f} seconds",
                'plot_time': f"{plot_time:.2f} seconds",
                'total_time': f"{total_time:.2f} seconds",
                'data_to_visualization_time': f"{data_to_visualization_time:.2f} seconds",
            })

    else:
        form = LogFileForm()

    return render(request, 'logs/upload.html', {'form': form})


def plot_event_distribution(data, save_path):
    plt.figure(figsize=(10, 6))
    data['event'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Event Distribution')
    plt.xlabel('Event Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
