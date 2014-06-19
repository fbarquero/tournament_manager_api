# coding: utf8
# try something like
__author__ = 'Mordigan'
import sys
from gluon.debug import qdb_debugger

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@request.restful()
def athlete():
    """
    Return, add, update, delete information regarding Athletes,
    using GET, POST, PUT, DELETE verbs
    """
    response.view = 'generic.json'
    def GET(*args,**vars):
        patterns = [
            "/athletes[fighter]",
            "/athlete[fighter]/:field",
            "/athletes[fighter]/{fighter.weight_category_id}/{fighter.age_category_id}/{fighter.gender}/:field"
        ]
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status,parser.error)
    def POST(**vars):
        try:
             ids = dict(values = db.fighter.bulk_insert(vars['athlete']))
             for fighter in ids['values']:
                 db.tournament_fighter.insert(tournament_tournament_id = vars['tournament']['number'], fighter_fighter_id = fighter)
             db.commit()
             return ids
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def PUT(**vars):
        try:
            for row in vars['athlete']:
                db(db.fighter.id == row['id']).validate_and_update(description = row['description'])
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def DELETE(**vars):
        try:
            for row in vars:
                db(db.fighter.id == row['athlete']).delete()
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0], )
    return locals()


@request.restful()
def belt_info():
    """
    Return, add, update, delete information regarding Taekwondo belts,
    using GET, POST, PUT, DELETE verbs
    """
    response.view = 'generic.json'
    def GET(*args,**vars):
        patterns = [
            "/colors[belt]",
            "/colors[belt]/:field",
            "/color/{belt.description}/:field"
        ]
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status,parser.error)
    def POST(**vars):
        try:
             var = dict(message = db.belt.bulk_insert(vars['content']))
             db.commit()
             return var
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def PUT(**vars):
        try:
            for row in vars['content']:
                db(db.belt.id == row['id']).validate_and_update(description = row['description'])
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def DELETE(**vars):
        try:
            for row in vars:
                db(db.belt.id == row['id']).delete()
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0], )
    return locals()

@request.restful()
def weight_category_info():
    """
    Return, add, update, delete information regarding Taekwondo belts,
    using GET, POST, PUT, DELETE verbs
    """
    response.view = 'generic.json'
    def GET(*args,**vars):
        patterns = [
            "/weight[weight_category]",
            "/weight[weight_category]/:field",
            "/weight/{weight_category.id}/:field"
        ]
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status,parser.error)
    def POST(**vars):
        try:
             var = dict(message = db.weight_category.bulk_insert(vars['content']))
             db.commit()
             return var
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def PUT(**vars):
        try:
            for row in vars['content']:
                db(db.belt.id == row['id']).validate_and_update(description = row['description'])
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def DELETE(**vars):
        try:
            for row in vars:
                db(db.belt.id == row['id']).delete()
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0], )
    return locals()

@request.restful()
def age_cat_info():
    """
    Return, add, update, delete information regarding Taekwondo belts,
    using GET, POST, PUT, DELETE verbs
    """
    response.view = 'generic.json'
    def GET(*args,**vars):
        patterns = [
            "/colors[belt]",
            "/colors[belt]/:field",
            "/color/{belt.description}/:field"
        ]
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status,parser.error)
    def POST(**vars):
        try:
             var = dict(message = db.belt.bulk_insert(vars['content']))
             db.commit()
             return var
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def PUT(**vars):
        try:
            for row in vars['content']:
                db(db.belt.id == row['id']).validate_and_update(description = row['description'])
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def DELETE(**vars):
        try:
            for row in vars:
                db(db.belt.id == row['id']).delete()
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0], )
    return locals()
