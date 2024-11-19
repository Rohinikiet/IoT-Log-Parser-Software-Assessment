import re
import base64
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def parse_logs(file_path):
    error_logs = []
    json_logs = []
    base64_logs = []

    error_pattern = re.compile(r"Exception|ERROR")
    base64_pattern = re.compile(r"^BASE64:")
    json_pattern = re.compile(r"^\{.*\}$")

    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if error_pattern.search(line):
            error_logs.append(line)
        elif base64_pattern.match(line):
            base64_logs.append(line.split("BASE64:")[1])
        elif json_pattern.match(line):
            json_logs.append(json.loads(line))

    decoded_base64_logs = []
    for entry in base64_logs:
        try:
            decoded = base64.b64decode(entry).decode("utf-8")
            decoded_base64_logs.append(json.loads(decoded))
        except (base64.binascii.Error, json.JSONDecodeError):
            error_logs.append(f"Error decoding Base64: {entry}")

    json_df = pd.DataFrame(json_logs)
    base64_df = pd.DataFrame(decoded_base64_logs)

    return json_df, base64_df, error_logs

def plot_event_distribution(df, output_path):
    sns.countplot(data=df, x='event', order=df['event'].value_counts().index, palette='viridis')
    plt.title("Event Distribution")
    plt.savefig(output_path)
    plt.close()
