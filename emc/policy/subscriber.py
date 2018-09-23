#-*- coding: UTF-8 -*-
from zope.component import getMultiAdapter
from zope.site.hooks import getSite
from Products.CMFCore.utils import getToolByName
from Products.PluggableAuthService.interfaces.events import IUserLoggedInEvent

def DeleteMemberEventHandler(event):
    """the system administrator delete specify user handler"""
    from emc.kb.interfaces import IAdminLogLocator
    from zope.component import getUtility
    
    values = {'adminid':event.adminid,'userid':event.userid,'datetime':event.datetime,
              'ip':event.ip,'type':0,'level':4,'result':1,'description':u''}                
    values['description'] = u"管理员%s删除了%s" % (event.adminid,event.userid)
   
    locator = getUtility(IAdminLogLocator)
    locator.add(values)
    
    
def PrincipalDeletedHandler(event):
    """the pluggableAuthService delete member event's handler"""
    
#     import pdb
#     pdb.set_trace()
    print event.principal
    

def userLoginedIn(event):
    """Redirects  logged in users to getting started wizard"""  

    portal = getSite() 
    user = event.object
    # admin by pass
    if user.getUserName() == "admin":return
    # check if we have an access to request object
    request = getattr(portal, 'REQUEST', None)
    if not request:
        return  
    # now complile and render our expression to url

    try:
        member_url_view = getMultiAdapter((portal, request),name=u"member_url") 
        url = member_url_view()
    except Exception, e:
        logException(u'Error during user login in redirect')
        return
    else:
        # check if came_from is not empty, then clear it up, otherwise further
        # Plone scripts will override our redirect
        if request.get('came_from'):
            request['came_from'] = ''
            request.form['came_from'] = ''
        request.RESPONSE.redirect(url) 