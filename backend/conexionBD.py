# instalar pip install pymysql
import sqlalchemy as sa

cfg = dict(
    host="localhost",
    port=3306,
    user="root",
    password="13mysql22",
    database="dashboard-bi",
)

def get_engine():
    return sa.create_engine(
        f"mysql+pymysql://{cfg['user']}:{cfg['password']}@{cfg['host']}:{cfg['port']}/{cfg['database']}"
    )
