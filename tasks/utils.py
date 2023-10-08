from django.core.mail import send_mail

def send_task_notification(task_id):
    """ Sends an email notification to the user when a task is due."""
    # Retrieve the task

    from .models import Task
    task = Task.objects.get(pk=task_id)

    subject = f"Task Reminder: {task.title}"
    message = f"Your task '{task.title}' is due on {task.due_date}."
    from_email = 'ibrahimmuhammad271@gmail.com'
    recipient_list = [task.user.email]

    # Send the email
    send_mail(subject, message, from_email, recipient_list)
