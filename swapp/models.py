from django.db import models


class DownlodedFile(models.Model):
    filename = models.CharField(max_length=200)
    download_time = models.DateTimeField('date downloaded')

    def __str__(self) -> str:
        return self.filename
