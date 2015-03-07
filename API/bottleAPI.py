from bottle import route, run, request
from DBClient import DBClient
from bson.json_util import dumps
@route('/recipes/')
def recipes_list():
    return "LIST"

@route('/recipes/<name>', method='GET')
def recipe_show( name="Mystery Recipe" ):
    # return "SHOW RECIPE " + name
    client=DBClient()
    # print name
    return str(dumps(client.get(name)))
    # return name

@route('/recipes/<name>', method='DELETE' )
def recipe_delete( name="Mystery Recipe" ):
    return "DELETE RECIPE " + name

@route('/recipes/<name>', method='PUT')
def recipe_save( name="Mystery Recipe" ):
    return "SAVE RECIPE " + name

run(host='localhost', port=8080, debug=True)