#Para que funcione el formulario en Contacto\
En app.py asignar un valor para app.config['MAIL_USERNAME'] y app.config['MAIL_PASSWORD'], esta es la cuenta desde la que se envían los mensajes. La cuenta debe ser de outlook y la contraseña es con la que se inicia sesión. Luego pasarle un mail a recipients (actualmente línea 193 en app.py), esta es la cuenta que recibe el mensaje.

\
#En la terminal

python -m venv venv\
./venv/Scripts/activate

pip install flask\
pip install flask-bootstrap\
pip install -U Flask-WTF\
pip install flask-sqlalchemy\
pip install flask-migrate\
pip install email_validator\
pip install flask-login\
pip install flask-mail\
py ./app/app.py

cd app\
python\
from app import *\
db.create_all()\
python -m flask db init\
python -m flask db migrate -m "initial migration"\
python -m flask db upgrade
