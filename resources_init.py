def add_resources():
    from app import api
    from app.resources import translation

    api.add_resource(user.CrudAPI, '/users/', '/users/<int:id>/')