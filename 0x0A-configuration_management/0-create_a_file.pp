# using puppet, create a file in /tmp.
# Requirements:
# file path is /tmp/school
# file permission is 0744
# file owner is www-data
# file group is www-data
# File content is I love Puppet
file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
