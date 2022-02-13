# from server import db
# class PhoneNumber(db.Model):
#     __tablename__ = '_phoneNumbers'
#     id = db.Column("id", db.Integer, primary_key=True)
#     name = db.Column("name", db.String(100), nullable=False)  # unique=True
#     phone = db.Column("phonenumber", db.String(100),unique=True, nullable=False)

#     def __init__(self, name: str, phone: str):
#         self.name = name
#         self.phone = phone