from google.appengine.api import urlfetch
from models import Status
from django.http import HttpResponseRedirect

def update(request):
    query = Status.objects.all()
    for result in query:
        check_and_update(result)
    return HttpResponseRedirect('/')

# helper method that parses the title out of the html recieved from a url
def parsetitle(url):
    # make sure we're not getting cached content
    fetch_headers = {'Cache-Control':'no-cache,max-age=0', 'Pragma':'no-cache'}

    # fetch the content
    response = urlfetch.fetch(url, headers=fetch_headers).content

    # parse the content
    [first, second] = response.split('<title>')
    [title, third] = second.split('</title>')

    # return the title
    return unicode(title)

# update a particular instance of Status
# according to the directions specified in its properties
def check_and_update(status_instance):
    # this update_type should be left alone
    if status_instance.update_type == u'none':
        return

    # check the status
    status = check(status_instance.update_url,
                   check_type=status_instance.update_type,
                   content=status_instance.update_content,
                   title=status_instance.update_title)

    # if the status has changed, update it
    # and write the new status instance to the datastore
    if status_instance.status != status:
        status_instance.status = status
        status_instance.save()

# checks the url with the parameters passed
def check(url, check_type=u'status', content=u'', title=u''):
    # make sure we're not getting cached content
    fetch_headers = {'Cache-Control':'no-cache,max-age=0', 'Pragma':'no-cache'}
    if check_type == u'status':
        try:
            response = urlfetch.fetch(url, headers=fetch_headers, deadline=60, validate_certificate=False)
            if response.status_code == 200:
                return u'online'
        except:
            pass
    elif check_type == u'title':
        try:
            parsedtitle = parsetitle(url)
            if title in parsedtitle:
                return u'online'
        except:
            pass
    elif check_type == u'content':
        try:
            response = urlfetch.fetch(url, headers=fetch_headers, deadline=60, validate_certificate=False).content
            if content in response:
                return u'online'
        except:
            pass
    return u'offline'
