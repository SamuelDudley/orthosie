#used this guide for deployment
#http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html

#need to be in orthosie root dir
python manage.py collectstatic
uwsgi --socket orthosie.sock --module orthosie.wsgi --chmod-socket=666&
sudo /etc/init.d/nginx restart

