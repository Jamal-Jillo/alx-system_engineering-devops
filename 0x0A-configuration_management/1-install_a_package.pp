# using Puppet install flask from pip3
# Requirements:
# install flask
# version must be 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
