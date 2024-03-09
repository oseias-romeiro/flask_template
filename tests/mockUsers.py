from datetime import datetime
from models.User import User, Role

def getSimpleUser():
    simpleUser = User()
    simpleUser.username = 'simple'
    simpleUser.email = 'simple@test.com'
    simpleUser.password = 'Simple#1234'
    simpleUser.role = Role.USER
    simpleUser.createAt = datetime.now()
    simpleUser.updateAt = datetime.now()

    return simpleUser

def getAdminUser():
    adminUser = User()
    adminUser.username = 'admin'
    adminUser.email = 'admin@test.com'
    adminUser.password = 'Admin#1234'
    adminUser.role = Role.ADMIN
    adminUser.createAt = datetime.now()
    adminUser.updateAt = datetime.now()

    return adminUser

