Create virtualenv

    cd /var/envs && mkvirtualenv --python=/usr/bin/python3 short_url
    pip install mysqlclient
    
Install requirements for a project.

    cd /var/www/short_url && pip install -r requirements.txt

##Database creation
###For psql

    sudo su - postgres
    psql
    DROP DATABASE IF EXISTS short_url;
    CREATE DATABASE short_url;
    CREATE USER short_url_user WITH password 'root';
    GRANT ALL privileges ON DATABASE short_url TO short_url_user;
    
    
##For add data fake users
    
    python manage.py create_fake_users (users_count)
    
    example:
        python manage.py create_fake_users 100
        
