import cherrypy

def token_set(key, value):
    cherrypy.session[key] = value

def token_get(key):
    return cherrypy.session[key]

def token_out():
    cherrypy.lib.sessions.expire()

def token_check(key, redirect):
    if cherrypy.session.get(key) == None:
        raise cherrypy.HTTPRedirect(redirect)
