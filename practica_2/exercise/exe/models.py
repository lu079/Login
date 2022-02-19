from app import db

class Usuarios(db.Model):
    cod_usuario=db.Column(db.String(4),primary_key=True)
    username=db.Column(db.String(20))
    email=db.Column(db.String(15))
    password=db.Column(db.String(8))