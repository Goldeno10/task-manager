from django.db.models.signals import post_save
from django.dispatch import receiver
from background_task.models import Task
from .utils import send_task_notification
from .models import Task as TaskModel


@receiver(post_save, sender=TaskModel)
def schedule_task_notification(sender, instance, created, **kwargs):
    if created:
        # Schedule the task notification to run in the background
        task = Task()
        task.task_name = 'tasks.utils.send_task_notification'
        task.task_params = f'[{instance.id}]'
        task.run_at = instance.due_date
        task.save()
