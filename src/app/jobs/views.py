'''
Created on 25 Nov 2013

@author: michael
'''
from django.views import generic as generic_views
from django.core.urlresolvers import reverse

from tunobase.core import utils as core_utils, mixins as core_mixins

from app.jobs import models

class JobList(generic_views.ListView):
    
    def get_queryset(self):
        return models.JobPost.objects.permitted()

class JobDetail(generic_views.DetailView):
    
    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            models.JobPost, 
            slug=self.kwargs['slug']
        )

class PostJob(core_mixins.LoginRequiredMixin, generic_views.CreateView):

    def get_success_url(self):
        return reverse('success')

class PostJobSuccess(generic_views.TemplateView):
    pass
