from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:////tmp/flask_template.db", echo=True)
Session = sessionmaker(bind=engine)

sess = Session()
