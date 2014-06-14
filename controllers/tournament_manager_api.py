# coding: utf8
# try something like

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@service.json
def service():
    belt = db().select(db.belt.ALL)
    #db().select(db.person.ALL)
    return(dict(belt=belt))
