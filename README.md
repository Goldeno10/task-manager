# Task Manager API

Task Manager API is a Django-based web application that allows users to manage their tasks. This API provides endpoints for creating, listing, updating, and deleting tasks, with user authentication and authorization in place. It also uses background job processing to send email notifications to users when task due dates are approaching.

## Features

- User registration and login.
- CRUD (Create, Read, Update, Delete) operations on tasks.
- List all tasks (with permissions).
- Background job processing for task notification emails.
- Authentication and authorization checks for API endpoints.

## Getting Started

### Prerequisites

- Python 3.7+
- Django 3.x
- Django REST framework
- Celery (for background job processing)
- Redis (for Celery message broker)

## Installation

### 1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/task-manager-api.git
   ```
### 2 - Navigate to the project directory:

   ```
     cd task-manager-api
   ```
### 2- Install the required Python packages:
```
pip install -r requirements.txt
```
Configure the Django project settings in task_manager/settings.py. Ensure you have the database settings, secret key, and email settings properly configured.

#### 3 - Migrate the database:
```
python manage.py migrate
```
### 4 - Create a superuser for admin access:
```
python manage.py createsuperuser
```
Start the Django background job processing:
   ```
   python manage.py process_tasks
   ```

Start the Django development server:
   ```
   python manage.py runserver
   ```

## Usage
Access the Django admin panel to add more users and manage tasks:
   ```
   http://localhost:8000/admin/
   ```
### Use the API endpoints to interact with tasks:

Create a task: POST /api/tasks/
List all tasks: GET /api/tasks/

Retrieve, update, and delete tasks by ID: GET, PUT, DELETE /api/tasks/{task_id}/

Register and log in to access tasks associated with your user account.

Background job processing will automatically send email notifications for approaching task due dates.

### API Authentication
The API uses session-based authentication. To access protected endpoints, you must be authenticated. You can log in or register a new user account.

### Error Handling
The API handles errors gracefully and returns appropriate status codes and error messages for invalid requests or unauthorized actions.

### Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and create a pull request.

### Acknowledgments
This project was created as a learning exercise for Django and Django REST framework.

Special thanks to the Django and its excellent documentation and resources.

### Support
If you encounter any issues or have questions, please open an issue on the [GitHub](https://github.com/Goldeno10/task-manager-api/issues) repository.

