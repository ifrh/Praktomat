from praktomat.tasks.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect 
from django.views.generic.list_detail import object_detail
from django.template.context import RequestContext
from datetime import datetime
from django import forms
from django.core import urlresolvers


@login_required
def taskList(Request):
	now = datetime.now()
	upcoming_tasks = Task.objects.filter(publication_date__lte = now).filter(submission_date__gt = now).order_by('-submission_date')
	expired_tasks = Task.objects.filter(publication_date__lte = now).filter(submission_date__lte = now).order_by('submission_date')
	tutors = Request#.user.userprofile_set.all()[0].tutorial.tutors.all()
	return render_to_response('tasks/task_list.html',{'upcoming_tasks':upcoming_tasks, 'expired_tasks':expired_tasks, 'tutors':tutors}, context_instance=RequestContext(Request))
	#return object_list(Request, Task.objects.all(), template_object_name='tasks')

@login_required
def taskDetail(Request,task_id):
	my_solutions = Task.objects.get(pk=task_id).solution_set.filter(author = Request.user)
	return object_detail(Request, Task.objects.all(), task_id, extra_context={'solutions': my_solutions}, template_object_name='task')

class ImportForm(forms.Form):
	file = forms.FileField()

@staff_member_required
def import_tasks(request):
	""" View in the admin """
	if request.method == 'POST': 
		form = ImportForm(request.POST, request.FILES)
		if form.is_valid(): 
			try:
				Task.import_Tasks(form.files['file'])
				request.user.message_set.create(message="The import was successfull.")
				return HttpResponseRedirect(urlresolvers.reverse('admin:tasks_task_changelist'))
			except:
				#raise
				from django.forms.util import ErrorList
				msg = "An Error occured. The import file was propably malformed."
				form._errors["file"] = ErrorList([msg]) 			
	else:
		form = ImportForm()
	return render_to_response('admin/tasks/task/import.html', {'form': form, 'title':"Import Task"  }, RequestContext(request))