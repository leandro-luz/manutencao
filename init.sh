if [ ! -d "venv" ]; then
    echo --------------------
    echo Creating virtualenv
    echo --------------------
    virtualenv venv
fi
sleep 5s

source venv/Scripts/activate
sleep 5s

pip install -r requirements.txt
sleep 5s

set FLASK_APP=main.py
sleep 5s

if [ ! -d "migrations" ]; then
    echo --------------------
    echo INIT THE migrations folder
    echo --------------------
    export FLASK_APP=main.py; flask db init
fi
sleep 5s

echo --------------------
echo Generate migration DDL code
echo --------------------
flask db migrate
sleep 5s

echo --------------------
echo Run the DDL code and migrate
echo --------------------
echo --------------------
echo This is the DDL code that will be run
echo --------------------
flask db upgrade
sleep 5s

echo --------------------
echo Show database tables
echo --------------------
export FLASK_APP=manange.py
sleep 5s

flask shell
sleep 5s

db.engine.table_names()
sleep 30s

echo --------------------