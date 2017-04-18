# -*- coding: utf-8 -*-

from pizza_project.celery_app import app
# from pizza_app.models import PizzaOrder

__author__ = 'akinash'


@app.task
def user_registered():
    print('task user registered')
    return 'background result of user registered'
