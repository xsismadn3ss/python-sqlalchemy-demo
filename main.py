from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
dburl = os.getenv("DB_URL_MYSQL")
engine = create_engine(dburl, echo=True)
Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))

    def __str__(self):
        return f"{self.id} {self.title}"


session = sessionmaker(engine)
s = session()

if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    m = Movie(title="The Godfather")
    s.add(m)
    s.commit()
    print(m)
    print("done")
