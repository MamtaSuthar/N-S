from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    location = models.CharField(max_length=150, blank=True)
    description = models.TextField()

    cover_image = models.ImageField(
        upload_to='projects/covers/'
    )

    budget_range = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: 5–10 Lakhs"
    )

    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='projects/gallery/')
    is_before = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.project.title}"
