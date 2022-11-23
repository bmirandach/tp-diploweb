La foto del hero es de [Annie Spratt](https://unsplash.com/@anniespratt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) en [Unsplash](https://unsplash.com/es/s/fotos/plantas-interiores?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
  

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
py ./app/app.py

cd app\
python\
from app import *\
db.create_all()\
python -m flask db init\
python -m flask db migrate -m "initial migration"\
python -m flask db upgrade