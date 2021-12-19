import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_IP = str(os.environ['DATABASE_IP'])

DATABASE_USER = "root"
DATABASE_PASS = "root"

DATABASE="tutorial_1"
PORT=3306

#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://my-api:my-api-password@127.0.0.1:3306/tutorial1"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@"+DATABASE_IP+":3306/tutorial_1"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
