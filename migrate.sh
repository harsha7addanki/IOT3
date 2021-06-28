echo "Running"
../eb-django/bin/python3.9 manage.py makemigrations
echo "Halfway!"
../eb-django/bin/python3.9 manage.py migrate
echo "Done"