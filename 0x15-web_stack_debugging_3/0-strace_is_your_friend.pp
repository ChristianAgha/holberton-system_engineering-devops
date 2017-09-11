# Fixes a typo in wordpress settings file
exec { 'sed -i s/phpp/php/ /var/www/html/wp-settings.php':
  command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games'
}
