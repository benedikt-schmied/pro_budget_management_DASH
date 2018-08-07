#!/usr/bin/python 
# coding=latin-1

import sys
import mysql.connector as mariadb

sys.path.append('./')


''' database definitions
first, there comes a namedtuple in order to ease data retrivals
second, there is a dictionary which holds the data types for each column
'''

class c_bm_database():
    ''' database classes
    '''
    def __init__(self):
        self.conn = None
        self.cursor = None
        return
    
    def connect(self):
        '''    connect to the database
        '''
        self.conn = mariadb.connect(user="python_test_1", password="2015@pYthon_test_1", database="python_test_1")
        self.cursor = self.conn.cursor()
        return (self.conn, self.cursor)
    
    def disconnect(self):
        ''' disconnect from the database
        '''
        self.cursor.close()
        return 
        
    def manual_db_command(self, _text):
        self.cursor.execute(_text)
        self.conn.commit


class c_app():
    ''' application, does not really do anything
    
    child classes of c_logging
    '''
    
    def __init__(self):
        ''' constructor
        '''
        return
    
    def run(self):
        ''' runs the main 
        '''
        self.logger.debug("application running")
        
        bm_database = c_bm_database()
        (conn, cursor) =  bm_database.connect()
        
        bm_database.disconnect()
    
if __name__ == "__main__":
    # execute only if run as a script
    app = c_app()
    app.run()
