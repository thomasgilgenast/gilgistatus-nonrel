from django.db import models

# Create your models here.
class Status(models.Model):
    class Meta:
        verbose_name_plural = 'statuses'
    
    # short description of the site
    description = models.CharField(max_length=200)

    # comment about the site
    comment = models.CharField(max_length=200)
    
    # link to the site
    link_url = models.CharField(max_length=200)

    # link display text
    link_text = models.CharField(max_length=200)

    # update information
    # should we check the status, title, or contents of the webpage?
    TYPE_CHOICES = (
        (u'none', u'none'),
        (u'status', u'status'),
        (u'title', u'title'),
        (u'content', u'content'),
    )
    update_type = models.CharField(max_length=8,
                                   default=u'none',
                                   choices=TYPE_CHOICES)

    # if not none, what url should we use to check the service?
    update_url = models.CharField(max_length=200,
                                  blank=True)

    # if contents, what should we look for in the contents?
    update_content = models.CharField(max_length=200,
                                      blank=True)

    # if title, what should we look for in the title
    update_title = models.CharField(max_length=200,
                                    blank=True)

    # the status of the site
    status = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description
