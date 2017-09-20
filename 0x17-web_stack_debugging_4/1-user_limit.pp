# Fixes OS configuration for su holberton
exec { 'change-os-configuration-for-holberton-user':
  command => 'sed -i \'/nofile 5/d\' /etc/security/limits.conf; \
  sed -i \'/nofile 4/d\' /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games'
}
