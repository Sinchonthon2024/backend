from django.db import models
from auths.models import MutsaUser

class Verify(models.Model):
    user = models.ForeignKey(MutsaUser, on_delete = models.CASCADE)
    verify_code = models.CharField(max_length = 125)

    class Meta:
        db_table = 'verify'
