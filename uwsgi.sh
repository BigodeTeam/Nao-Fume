#!/bin/bash
set -e
LOGFILE=/var/log/naofume.log
LOGDIR=$(dirname $LOGFILE)
test -d $LOGDIR || mkdir -p $LOGDIR


exec /var/www/bigode/bin/uwsgi \
--chdir=/var/www/bigode/naofume/ \
--module='naofume.wsgi:application' \
--socket=/var/tmp/naofume.sock \
--processes=5 \
--master --pidfile=/var/run/naofume.pid \
--home=/var/www/bigode \
--daemonize=$LOGFILE
