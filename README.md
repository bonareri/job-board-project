# Job Board Project

This is a job board web application I built using Django, designed to allow users to create, view, and submit job listings. It helps demonstrate my skills in backend web development with Python and Django, as well as my understanding of models, views, templates, and forms.

## Features

- **Job Listings:** View a list of job openings including details like the job title, company, description, and salary.
- **Create Job Listings:** Users can add new job listings via a form, providing essential details about the job.
- **Job Details:** Users can click on individual job listings to view more detailed information.

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite (used by default in Django)
- **Deployment:** Local development server or you can deploy it to platforms like Heroku.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/job-board-project.git
   ```
2. Navigate into the project folder:
   ```bash
   cd job-board-project
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run migrations:
   ```bash
   python manage.py migrate
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```
### Link to the Website
If you want to access the project online, you can deploy it to platforms like Heroku. For now, you can view it locally at http://127.0.0.1:8000/.

## Future Improvements
- Add search functionality for job seekers
- Add email notifications for new job listings
- Integrate with an external job API

## License
This project is licensed under the MIT License.
