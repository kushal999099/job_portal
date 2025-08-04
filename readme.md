# Job Portal Flask App

This is a simple Job Portal web application built using Flask, SQLAlchemy, and Flask-Login. It allows employers to post jobs, and job seekers to apply for them.

## Project Structure

```
job_portal_project.zip
└── job_portal/
    ├── app/
    ├── instance/
    ├── run.py
    ├── requirements.txt
    └── README.md
```

## Setup Instructions

1. **Unzip the Project**

   Extract the contents of the zip file:

   ```bash
   unzip job_portal_project.zip
   cd job_portal
   ```

2. **Create a Virtual Environment**

   Create and activate a Python virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Requirements**

   Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   Run the Flask app:

   ```bash
   python3 run.py
   ```

5. **Access the Application in Browser**

   Open your browser and navigate to:

   ```
   http://127.0.0.1:5000/register
   ```

   This is the registration page to create your first user.

## Notes

- Make sure you have **Python 3.7+** installed.
- Database file will be created inside the `instance/` folder automatically on first run.
- You can register as:
  - `admin`
  - `employer`
  - `jobseeker`

