python manage.py migrate
python manage.py loaddata api/master_data/god.json
python manage.py read_card
python manage.py init_partner_data
./scripts/update-cdn.sh
python manage.py collectstatic