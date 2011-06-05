from fabric.api import local, env

def production():
    env['epioapp'] = 'wipkipvinder'

#def staging():
#    env['epioapp'] = 'wipkipvinder'

def epio(commandstring):
    local("epio {0} -a {1}".format(
        commandstring,
        env['epioapp']))

def deploy():
    """ An example deploy workflow """
    local("python manage.py collectstatic")
    epio('upload')
    epio('django syncdb')
    epio('django migrate')
    epio('django epio_flush_cache')