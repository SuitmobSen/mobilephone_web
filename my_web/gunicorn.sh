source /home/myweb/venv/bin/activate
while :
do
    sleep 4
    gunicorn  -w 4 -b 127.0.0.1:8000  --access-logfile=/var/log/gunicorn.log my_web.wsgi:application
done
