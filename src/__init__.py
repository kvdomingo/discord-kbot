import os, sys
sys.path.append('.')

from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = create_engine(os.environ['DATABASE_URL'])
Session = sessionmaker(bind=db)
