from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pathlib

PATH = pathlib.Path(__file__).parent.resolve()

engine = create_engine(f"sqlite:///{PATH}/flask_template_db.sqlite", echo=True)
Session = sessionmaker(bind=engine)

sess = Session()
