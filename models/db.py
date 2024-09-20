from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# строка подключения
SQLALCHEMY_DATABASE_URL = "sqlite:///app.db"

# создаем движок SqlAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
Base=declarative_base()
# создаем базовый класс для моделей


Session=sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


