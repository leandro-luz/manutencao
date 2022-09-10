if [ ! -d "venv" ]; then
    echo --------------------
    echo Creating virtualenv
    echo --------------------
    virtualenv venv
fi

source venv/Scripts/activate
pip install -r requirements.txt

if [ ! -d "migrations" ]; then
    echo --------------------
    echo INIT THE migrations folder
    echo --------------------
    export FLASK_APP=main.py
    flask db init
fi

echo --------------------
echo Generate migration
flask db stamp head
flask db migrate
flask db upgrade


