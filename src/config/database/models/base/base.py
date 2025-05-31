from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)