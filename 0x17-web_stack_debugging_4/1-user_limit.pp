# Fixes OS configuration for su holberton
exec { 'Fix_Holberton_User':
  command => 'sed -i \'s/nofile 5/nofile 500000/g\' /etc/security/limits.conf; \
  sed -i \'s/nofile 4/nofile 500000/g\' /etc/security/limits.conf',
  path    => '/etc/'
}
