import logging, sqlite3, datetime

class DatabaseHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)
        self.database = 'log.db'
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()

        mk_table_query = '''
            CREATE TABLE IF NOT EXISTS log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                insertTime TEXT,
                logLv TEXT,
                name TEXT,
                message TEXT
                )
        '''
        self.conn.execute(mk_table_query)
        self.conn.commit()

    def time_format(self, record):
        self.now = datetime.datetime.now()
        record.nowstr = self.now.strftime('%d/%b/%Y %H:%M:%S')

    def emit(self, record):
        self.format(record)
        self.time_format(record)
        aaa = record.name+str(record.lineno)
        insert_db_query = '''
            INSERT INTO log (
            insertTime, logLv, name, message) VALUES
            ('{}', '{}', '{}', '{}')
        '''.format(record.nowstr, record.levelname, aaa, record.message)

        self.conn.execute(insert_db_query)
        self.conn.commit()

    def __del__(self):
        try:
            self.conn.close()
        except:
            pass
        
if __name__ == '__main__':
    logger = logging.getLogger('lmppa')     # logger name 선언
    logger.setLevel(logging.DEBUG)              # logger level 설정
    sqliteHandler = DatabaseHandler()           # database handler 선언
    logger.addHandler(sqliteHandler)            # database hanlder 추가
    logger.info("----------")                   # info 메세지 작성           
    logger.info("$$$ start!!!")      
