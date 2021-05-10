from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    #deleted = False

    @property
    def get_html_url(self):
        '''
        if self.deleted==False:
            url = reverse('calen:event_edit', args=(self.id,))
        elif self.deleted==True:
            '''
        url = reverse('calen:event_edit', args=(self.id,))
        return f'<a href="{url}">{self.title}</a>'

    def get_expired_event(self):
        return self.title

'''
    @property
    def get_html_url(self):
        url = reverse('calen:delete_event', args=(self.id,))
        return f'<a href="{url}">{self.title}</a>'
        '''
    
