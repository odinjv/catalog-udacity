#coding: utf-8

def load_controllers(app):
    '''Defines the controllers for the catalog module.

    The controllers definitions have to be called explicitly, and don't run
    when the module is imported. This allow us to use the app decorators to
    define the routes.
    '''

    @app.route('/')
    @app.route('/catalog')
    def show_catalog():
        '''Returns the html with the full catalog.

        Read the database and obtain the item catalog, then loads it into the
        catalog template.
        '''
        return 'This will be the catalog'
