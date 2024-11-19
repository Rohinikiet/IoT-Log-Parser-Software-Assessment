# IoT-Log-Parser-Software-Assessment

Here’s a thorough and professional README.md file template for your IoT Log Parser project, including all necessary sections with clear explanations:

---

# IoT Log Parser - Smart City Living Lab

This project implements an IoT log parser for the Smart City Living Lab, designed to process logs from various sensors and devices, extract meaningful data, decode Base64 images, and visualize results. The log parser handles web server logs (Apache/Nginx), structured data, and Base64 encoded images, providing a comprehensive dashboard for monitoring and analyzing the parsed data.

---

## Table of Contents

- [Installation Instructions/Setup](#installation-instructionssetup)
- [How to Run](#how-to-run)
- [Screenshots](#screenshots)
- [Assumptions](#assumptions)
- [Error Handling](#error-handling)
- [Performance Analysis](#performance-analysis)

---

## Installation Instructions/Setup

To set up and run the IoT log parser project, follow these instructions:

### Prerequisites:
- Python 3.8 or higher
- Django 3.x or higher
- Matplotlib
- Other Python dependencies listed below

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/iot-log-parser.git
cd iot-log-parser
```

### 2. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install all required dependencies using pip:
```bash
pip install -r requirements.txt
```

**`requirements.txt` should include:**
- Django
- Matplotlib
- pandas
- Any other libraries you’re using (e.g., for Base64 parsing)

Example `requirements.txt`:
```
Django>=3.0
matplotlib>=3.0
pandas>=1.0
```

### 4. Set Up the Database
Run Django migrations to set up the database:
```bash
python manage.py migrate
```

### 5. Configure Settings
Ensure the following settings are configured in your `settings.py`:

- `MEDIA_ROOT`: Define the path for uploaded files.
- `STATIC_ROOT`: Define the path for storing generated static files like images.

Example:
```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

---

## How to Run

### 1. Start the Django Development Server
To start the Django server, run the following command:
```bash
python manage.py runserver
```

The server should now be running at `http://127.0.0.1:8000/`.

### 2. Upload a Log File
Navigate to the log upload page in your browser:
```
http://127.0.0.1:8000/upload/
```

- Upload a log file via the form on the page.
- The log file can contain any type of sensor data, web server logs, or Base64 encoded images.
- After submission, the parser processes the file and displays the following:
  - A table of parsed JSON data.
  - A table of extracted Base64 encoded images.
  - Any error logs encountered during parsing.
  - A bar chart visualization of event distribution.

### 3. View the Processed Results
Once the log file is processed, you'll be redirected to the dashboard page where you can:
- View the parsed log data in tabular format.
- View Base64 decoded images.
- View event distribution graphs.
- View performance metrics (e.g., file ingestion time, parsing time).

---

## Screenshots

### 1. Log File Upload Form
![Log File Upload Form](screenshots/upload_form.png)

This screenshot shows the form used to upload log files.

### 2. Data Visualization Dashboard
![Event Distribution Graph](screenshots/dashboard_event_distribution.png)

The dashboard displays a bar chart of event distribution based on the uploaded log data.

### 3. Parsed Log Data
![Parsed Log Data](screenshots/parsed_log_data.png)

This shows the first few rows of parsed JSON data from the log file in a table format.

---

## Assumptions

During the development of this project, the following assumptions were made:

1. **Log File Format:**
   - The log file contains structured key-value pairs.
   - The log may also include Base64 encoded images and web server logs (Apache/Nginx).
   - The expected key for event data is "event," which is critical for generating visualizations.

2. **Data Integrity:**
   - The log file is expected to have a consistent structure for key-value pairs.
   - The logs may have missing or malformed entries, which will be handled gracefully by the parser.

3. **Static Files:**
   - The static files (such as images) are saved in the location defined by `STATIC_ROOT` in `settings.py`.
   - You have configured `STATIC_ROOT` to a valid location to store visualizations like the event distribution plot.

4. **Performance:**
   - For large log files, the parser may take time to process and visualize the data. It's assumed that the parser will handle these operations sequentially (i.e., it does not process data asynchronously by default).

5. **Log File Size:**
   - While large log files are supported, the system may experience performance degradation with files that are excessively large (e.g., hundreds of MBs). For optimal performance, logs should be reasonably sized.

---

## Error Handling

The parser has robust error handling in place:

1. **Invalid Log Format:**
   - If the log file contains unexpected formats or missing values, the parser will handle these gracefully, skipping invalid entries and reporting errors.

2. **Missing Columns:**
   - If the expected `event` column is missing from the log data, an error message is returned, specifying which columns are found.

3. **File Path Issues:**
   - If the `MEDIA_ROOT` or `STATIC_ROOT` directories are not set, the parser will raise an appropriate exception with a helpful error message.

---

## Performance Analysis

The performance of the parser is measured for various steps, including:

1. **File Ingestion Time:** Time taken to save the uploaded log file to the server.
2. **Parsing Time:** Time spent parsing the log file into structured data.
3. **Plot Generation Time:** Time taken to generate visualizations.
4. **Total Time:** Cumulative time for file ingestion, parsing, and visualization.

These times are displayed on the dashboard and are useful for performance monitoring, especially with large log files.

### Performance Example:
```
File Ingestion Time: 2.34 seconds
Log Parsing Time: 3.56 seconds
Plot Generation Time: 1.45 seconds
Total Processing Time: 7.35 seconds
```

---

## Conclusion

This IoT log parser is a comprehensive tool for analyzing and visualizing log data from various devices and sensors in a smart city. The parser handles complex log formats, including Base64 images and web server logs, and provides insightful visualizations to help understand the data. By following the installation and usage instructions, users can easily integrate this tool into their workflow for real-time data processing and monitoring.

For any questions or issues, feel free to open an issue on the GitHub repository.

---

**GitHub Repository:** [https://github.com/yourusername/iot-log-parser](https://github.com/yourusername/iot-log-parser)

---

This README provides a detailed overview of the project setup, execution, and additional considerations. You can adjust the instructions, especially the installation and screenshots, based on your actual project files and output.
