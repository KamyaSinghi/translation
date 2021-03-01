from app.models import *


class Translate(Base):

    __tablename__ = 'translate'
    source = Column(String(10), nullable=False)
    destination = Column(String(10), nullable=False)
    text = Column(String(100), nullable=False)



    # def __repr__(self):
    #     return "User(id: {}, name: {}, mobile: {}, email: {})"\
    #         .format(self.id, self.name, self.mobile, self.email)
