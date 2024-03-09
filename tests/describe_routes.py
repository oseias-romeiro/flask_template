
routes = {
    '/':                {'authRequired': False, 'adminRequired': False},
    '/account/signin':  {'authRequired': False, 'adminRequired': False},
    '/account/create':  {'authRequired': False, 'adminRequired': False},
    '/account/home':    {'authRequired': True,  'adminRequired': False},
    '/account/profile': {'authRequired': True,  'adminRequired': False},
}

