"""
Provide a programatic way to manipulate git repos for a scenario
"""

import logging
import os
import subprocess


logger = logging.getLogger(__name__)


class GitRepo(object):
    def __init__(self, path):
        self.path = os.path.expanduser(path)

    def _run(self, *args, **kwargs):
        """Run a git command"""

        if kwargs.get('show', False):
            print '$ git ' + ' '.join(list(args))

        cmd = ['/usr/bin/git'] + list(args)
        env = os.environ

        logger.info(' '.join(cmd))
        p = subprocess.Popen(cmd, shell=False, cwd=self.path, env=env,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout, stderr = p.communicate()
        return_code = p.wait()
        logger.debug(stdout)
        logger.debug(stderr)
        return (return_code, stdout, stderr)

    def init(self):
        """git init a repo"""
        if not os.path.exists(self.path):
            logger.info('Creating %s', self.path)
            os.makedirs(self.path)
        self._run('init')

    def config(self, key, value=None):
        """Get or Set a config value"""
        pass

    def commit(self, message, show=None):
        self._run('commit', '-m', message, show=show)

    def random(self, filename):
        path = os.path.join(self.path, filename)
        logger.info('Creating file %s', path)
        print 'Working on', filename
        with open(path, 'a+') as f:
            f.write('foo')

    def add(self, filename, show=None):
        self._run('add', filename, show=show)

    def add_random(self, filename, show=None):
        self.random(filename)
        self.add(filename, show=show)

    def status(self, show=None):
        r, o, e = self._run('status', show=show)
        print o

    def clone(self, remote, show=None):
        self._run('clone', remote, self.path, show=show)
