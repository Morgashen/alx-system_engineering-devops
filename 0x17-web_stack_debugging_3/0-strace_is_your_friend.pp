# This Puppet manifest fixes the Apache 500 error caused by incorrect file permissions
file { '/var/www/html':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
  recurse => true,
}

service { 'apache2':
  ensure => running,
  enable => true,
  subscribe => File['/var/www/html'],
}
