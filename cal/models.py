from django.db import models
from django.urls import reverse
from main.models import Program


        
class Meeting(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    program = models.ForeignKey(Program, blank=True, null=True, on_delete=models.SET_NULL)
    
    @property
    def get_html_url(self):
        url = reverse('home:program_detail', args=(self.program.pk,))
      
        return f'<a href="{url}"> {self.program.name} </a>'
