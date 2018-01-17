from charmhelpers.core.hookenv import (
    action_get,
    action_fail,
    action_set,
    status_set,
)
from charms.reactive import (
    remove_state as remove_flag,
    set_state as set_flag,
    when,
    when_not,
)
import charms.sshproxy


@when_not('simple.installed')
def install_simple_proxy_charm():
    set_state('simple.installed')
    status_set('active', 'Ready!')


@when('actions.touch')
def touch():
    err = ''
    try:
        filename = action_get('filename')
        cmd = 'touch {}'.format(filename)
        result, err = charms.sshproxy._run(cmd)
    except:
        action_fail('command failed:' + err)
    else:
        action_set({'outout': result})
    finally:
        remove_flag('actions.touch')
