
import logging
from tutor.git import GitRepo

logging.basicConfig(level=logging.INFO)

local = GitRepo('~/Desktop/local', nuke=True)
remote = GitRepo('~/Desktop/remote', nuke=True)

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
print 'and push it'
local.push()
local.graph()

print 'But what if someone has made changes since we pulled?'
remote.add_random('baz.txt')
remote.add_random('panda.txt')
remote.commit("Someone else's work")

local.add_random('cat.txt')
local.commit('The work we did')

local.graph()
remote.graph()
