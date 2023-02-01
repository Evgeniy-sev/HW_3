from django.db import models
from django.utils import timezone
from tasks.managers import AnnotatedManager


class Tasks(models.Model):

    objects = AnnotatedManager()
    title = models.CharField(
        max_length=200, null=False, help_text="(Наименование задачи)"
    )
    created_time = models.DateTimeField(
        auto_now_add=True, help_text="(Время создания задачи)"
    )
    completed = models.BooleanField(
        default=False, null=False, help_text="(Отметка о выполнении)"
    )
    completed_time = models.DateTimeField(
        default=None, blank=True, null=True, help_text="(Время завершения задачи)"
    )

    def save(self, *args, **kwargs) -> None:
        """Переопределение сохранения.
        ставится дата завершения задачи, если есть отметка о завершении.
        """
        if self.completed:
            self.completed_time = timezone.now()
        else:
            self.completed_time = None
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
