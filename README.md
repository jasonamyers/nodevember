Nodevember
==========

Getting Started:

    pip install virtualenv
    virtualenv --no-site-packages nodevemberenv
    source nodevemberenv/bin/activate
    git clone git@github.com:nodevember/nodevember.git pytn
    cd nodevember
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py loaddata fixtures/*
    python manage.py runserver
