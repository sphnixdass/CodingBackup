# -*- coding: utf-8 -*-
import random
from django.db import models
from webcam.fields import CameraField
from webcam.tests import temp_storage


class DemoModel(models.Model):
    photo = CameraField('CameraPictureField', format='jpeg', null=True, blank=True, upload_to='pictures')

    class Meta:
        app_label = 'webcam'
