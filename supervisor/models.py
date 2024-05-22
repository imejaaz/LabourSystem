from django.db import models
from django.utils import timezone
from labor.models import Labor

class Application(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    labor = models.ForeignKey(Labor, on_delete=models.CASCADE, related_name="applications")
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    def __str__(self):
        return f"{self.labor} - {self.title} - {self.get_status_display()}"

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
