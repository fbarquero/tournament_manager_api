# coding: utf8
# try something like
__author__ = 'Mordigan'
import sys
import utils

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
    response.headers["Access-Control-Allow-Origin"] = "*"
    #response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    #response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    #if request.env.request_method == 'OPTIONS':
        #if request.env.http_access_control_request_method:
           # response.headers['Access-Control-Allow-Methods'] = request.env.http_access_control_request_method
        #if request.env.http_access_control_request_headers:
         #   response.headers['Access-Control-Allow-Headers'] = request.env.http_access_control_request_headers
    #response.headers["Allow"] = "GET, POST, PUT, DELETE"
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
             utils.format_fighers_data(vars['athlete'], db().select(db.belt.ALL), db().select(db.weight_category.ALL), db().select(db.age_category.ALL))
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
            "/color/{belt.id}/:field"
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
def weight_division_info():
    """
    Return, add, update, delete information regarding Taekwondo belts,
    using GET, POST, PUT, DELETE verbs
    """
    response.view = 'generic.json'
    def GET(*args,**vars):
        patterns = [
            "/weight_division[weight_category]",
            "/weight_division[weight_category]/:field",
            "/weight_division/{weight_category.id}/:field"
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
                db(db.weight_category.id == row['id']).validate_and_update(description = row['description'])
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def DELETE(**vars):
        try:
            for row in vars:
                db(db.weight_category.id == row['id']).delete()
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0], )
    return locals()

@request.restful()
def age_division_info():
    """
    Return, add, update, delete information regarding Taekwondo belts,
    using GET, POST, PUT, DELETE verbs
    """
    response.view = 'generic.json'
    def GET(*args,**vars):
        patterns = [
            "/age_division[age_category]",
            "/age_division[age_category]/:field",
            "/age_division/{age_category.id}/:field"
        ]
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status,parser.error)
    def POST(**vars):
        try:
             var = dict(message = db.age_category.bulk_insert(vars['content']))
             db.commit()
             return var
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def PUT(**vars):
        try:
            for row in vars['content']:
                db(db.age_category.id == row['id']).validate_and_update(description = row['description'])
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def DELETE(**vars):
        try:
            for row in vars:
                db(db.age_category.id == row['id']).delete()
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0], )
    return locals()

@request.restful()
def tournament_info():
    """
    Return, add, update, delete information regarding Taekwondo belts,
    using GET, POST, PUT, DELETE verbs
    """
    response.view = 'generic.json'
    def GET(*args,**vars):
        patterns = [
            "/info[tournament]",
            "/info[tournament]/:field",
            "/info/{tournament.id}/:field",
            "/info/{tournament.name}/:field"
        ]
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status,parser.error)
    def POST(**vars):
        try:
             var = dict(message = db.tournament.bulk_insert(vars['content']))
             db.commit()
             return var
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def PUT(**vars):
        try:
            for row in vars['content']:
                db(db.tournament.id == row['id']).validate_and_update(description = row['description'])
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def DELETE(**vars):
        try:
            for row in vars:
                db(db.tournament.id == row['id']).delete()
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0], )
    return locals()


@request.restful()
def bracket():
    """
    Return, add, update, delete information regarding Taekwondo belts,
    using GET, POST, PUT, DELETE verbs
    """
    response.view = 'generic.json'
    def GET(*args,**vars):
        patterns = [
            "/bracket_info[bracket]",
            "/bracket_info[bracket]/{bracket.weight_category_id}/{bracket.age_category_id}/{bracket.gender}/{bracket.belt_id}/{bracket.tournament_id}/:field"
            #"/bracket_info/{bracket.id}/:field"
        ]
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(bracket = parser.response)
        else:
            if parser.error == 'no record found' and len(args) == 7:
                content = db((db.fighter.weight_category_id == args[1])&
                                         (db.fighter.age_category_id == args[2])&
                                         (db.fighter.gender == args[3]) &
                                         (db.fighter.belt_belt_id == args[4]) &
                                         (db.fighter.id == db.tournament_fighter.fighter_fighter_id) &
                                         (db.tournament_fighter.tournament_tournament_id == db.tournament.id) &
                                         (db.tournament.id == args[5])).select()
                if len(content) == 0:
                    raise HTTP(parser.status,parser.error)
                else:
                    return dict(bracket = utils.single_elimination_bracket_generation(content))
            else:
                raise HTTP(parser.status,parser.error)
    def POST(**vars):
        try:
             var = dict(message = db.tournament.bulk_insert(vars['content']))
             db.commit()
             return var
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def PUT(**vars):
        try:
            for row in vars['content']:
                db(db.tournament.id == row['id']).validate_and_update(description = row['description'])
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0])
    def DELETE(**vars):
        try:
            for row in vars:
                db(db.tournament.id == row['id']).delete()
            db.commit()
        except:
            db.rollback()
            raise HTTP (400, "Unexpected error: %s" % sys.exc_info()[0], )
    return locals()
