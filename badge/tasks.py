mport os
import StringIO
import zipfile

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings

from celery.decorators import task
from BadgeGen import createBadges

@task
