# Creates a file called holberton in /tmp
file { '/tmp/holberton':
  ensure  => file,
  content => 'I love Puppet',
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data'
}
