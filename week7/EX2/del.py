from models2 import Base,Member
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime 

db_uri = 'sqlite:///Ex.2.db'
engine = create_engine(db_uri,echo=False)

#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = Member(
    name = 'Fast',
    description = 'im testing this',
    vip = True,
    join_date = datetime.datetime.now(),
    number = 45.0
)

obj = session.query(Member).filter(Member.id==2).first()
session.delete(obj)
session.commit()
print(user) 