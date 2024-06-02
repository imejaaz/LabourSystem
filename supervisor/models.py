from django.db import models
from django.utils import timezone
from labor.models import Labor
class Application(models.Model):
    STATUS_CHOICES = [
        ('save', 'Saved'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    labor = models.ForeignKey(Labor, on_delete=models.CASCADE, related_name="applications")
    title = models.CharField(max_length=255)
    app_id = models.CharField(max_length=10,  verbose_name="Application ID")
    description = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='save')
    def __str__(self):
        return f"{self.labor} - {self.title} - {self.get_status_display()}"

    def save(self, *args, **kwargs):
        if not self.app_id:
            self.app_id = self.generate_application_id()
        super(Application, self).save(*args, **kwargs)

    def generate_application_id(self):
        prefix = 'LAPID-'
        last_application = Application.objects.filter(app_id__startswith=prefix).order_by('-app_id').first()
        if last_application:
            last_id = int(last_application.app_id[len(prefix):])
            new_id = f"{prefix}{last_id + 1:04d}"
        else:
            new_id = f"{prefix}0001"
        return new_id


    class Meta:
        verbose_name_plural = "Applications"

class ReviewerComment(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="comments")
    commentator = models.ManyToManyField(Labor, blank=True)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.application.title} by {self.application.labor}"

    class Meta:
        verbose_name_plural = "Reviewer Comments"

class ApplicationDocument(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="documents")
    document = models.FileField(upload_to='application_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.application.title} by {self.application.labor}"

    class Meta:
        verbose_name_plural = "Application Documents"
