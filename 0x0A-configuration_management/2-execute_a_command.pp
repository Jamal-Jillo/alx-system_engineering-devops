# using puppet, create a manifest that kills a process named killmenow
# Requirements:
# Must use the exec puppet resource
# Must use pkill to kill the process
exec {'killmenow':
    path => '/usr/bin',
    command => 'pkill -f killmenow',
}