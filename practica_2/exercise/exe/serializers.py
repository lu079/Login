from exe import app

from exe.models import Usuarios
from flask_marshmallow import Marshmallow

ma=Marshmallow(app)

class UserSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Usuarios
        fields=('cod_usuario','username','email','password')

user_schema=UserSerializer()
users_schema=UserSerializer(many=True)
