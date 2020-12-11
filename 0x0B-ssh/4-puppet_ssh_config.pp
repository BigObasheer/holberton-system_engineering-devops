# connect to a server without typing a password
file_line {'Disable Password':
	  ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}
file_line {'Update Key':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/holberton',
}
