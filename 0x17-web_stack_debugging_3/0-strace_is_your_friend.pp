# Define the file path
$file_to_edit = '/var/www/html/wp-settings.php'

# Use the file resource to ensure the file exists and has the correct permissions
file { $file_to_edit:
  ensure => file,
  mode   => '0644', # Set the file permissions (read/write for owner, read for others)
  owner  => 'www-data', # Set the file owner (assuming Apache/Nginx runs as www-data)
  group  => 'www-data', # Set the file group (assuming Apache/Nginx runs as www-data)
}

# Use the file_line resource to replace the line containing "phpp" with "php"
file_line { 'replace_phpp_with_php':
  path  => $file_to_edit,
  match => 'phpp',
  line  => 'php',
}
