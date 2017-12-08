from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default= 'zbim3364)kh6qk0j2i(p%ctu*f&xp=8qt^!viam_#=gmrcn^%f')


DEBUG = env.bool('DJANGO_DEBUG',default=True)
