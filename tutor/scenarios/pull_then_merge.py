
import logging
from tutor.git import GitRepo

logging.basicConfig(level=logging.INFO)

local = GitRepo('~/Desktop/local')
remote = GitRepo('~/Desktop/remote')

# Setup a remote repository for our example
remote.init()
remote.add_random('foo.txt')
remote.add_random('bar.txt')
remote.commit('Our remote repo')


print 'Lets clone our remote repository'
local.clone(remote.path, show=True)
print 'and then lets add some text'
local.add_random('foo.txt')
local.status()
print 'and commit'
local.commit('First foo')

