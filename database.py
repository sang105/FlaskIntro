from sqlalchemy import create_engine, text
import os
db_username = os.getenv("DATABASE_USERNAME")
db_password = os.getenv("DATABASE_PASSWORD")
db_server = os.getenv("DATABASE_SERVER")
db_name = os.getenv("DATABASE_NAME")

engine = create_engine(f"mysql+pymysql://{db_username}:{db_password}@{db_server}/{db_name}?charset=utf8mb4")

# with engine.connect() as conn:
#         sql_query = 'SELECT * FROM jobs'
#         results = conn.execute(text(sql_query))
#         result_all = results.all()
#         d = []
#         for column in result_all:
#             res = column._mapping
#             d.append(dict(res))
#         print(d)



def load_jobs_from_db():
    with engine.connect() as conn:
        sql_query = 'SELECT * FROM jobs'
        results = conn.execute(text(sql_query))
        result_all = results.all()

        result_dicts = []
        for row in result_all:
            res = row._mapping
            result_dicts.append(dict(res))
        return result_dicts            