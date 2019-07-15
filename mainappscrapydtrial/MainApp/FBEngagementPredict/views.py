from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.utils import timezone
from scrapyd_api import ScrapydAPI
from FBEngagementPredict.models import * 
from uuid import uuid4
from urllib.parse import urlparse
from django.shortcuts import redirect
import time 

scrapyd = ScrapydAPI('http://localhost:6800')
def home(request):
	return render(request, 'FBEngagementPredict/home.html', context=None)
	# return HttpResponse("Hello, world. You're at the Bakakaka index.")

def process(request):
	mainurl=Mainsite(siteurl=request.POST['mainurl'])
	flag=True
	domain = urlparse(mainurl.siteurl).netloc # parse the url and extract the domain
	# unique_id = str(uuid4()) # create a unique ID.
	for i in Mainsite.objects.all():
		if i.siteurl==mainurl.siteurl and i.crawled:
			flag=False
			break

	if flag:
		mainurl.save()
		unique_id=mainurl.id
		settings = {
			'unique_id': mainurl.id, # unique ID for each record for DB
			'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
		} 

		task = scrapyd.schedule('default', 'icrawler',settings=settings, url=mainurl.siteurl, domain=domain)
		# return HttpResponse("Processing site %s" % mainurl.siteurl)
		return redirect('results/?task_id='+str(task)+'&unique_id='+str(unique_id))

	else:
		# return HttpResponse("Site has already been processed on %s" % i.lastcrawled)
		main=i
		return render(request, 'FBEngagementPredict/final.html', context={'main':main})


def results(request):
	task_id = request.GET.get('task_id', None)
	unique_id = request.GET.get('unique_id', None)

	status = scrapyd.job_status('default', task_id)
	while(status!='finished'):
		time.sleep(1)
		status = scrapyd.job_status('default', task_id)

	print(status)

	if status=='finished':
		return redirect('/FBEngagementPredict/process/final?unique_id='+str(unique_id))
		mainurl.crawled=True
		mainurl.save()
	return HttpResponse(str(status)+" "+str(task_id)+" "+str(unique_id))

def final(request):
	unique_id = request.GET.get('unique_id', None)
	main=Mainsite.objects.get(id=unique_id)
	context={
	'main':main
	}
	return render(request, 'FBEngagementPredict/final.html', context=context)








