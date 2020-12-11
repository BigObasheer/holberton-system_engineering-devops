# Install and configure an Nginx server using Puppet

package { 'nginx':
    ensure   => 'installed',
    provider => 'apt',
}

file { '/var/www/html/index.html':
    ensure  => 'file',
    content => 'Holberton School',
}

file_line { '/etc/nginx/sites-available/default':
    ensure   => 'present',
    multiple => 'true',
    after    => 'server_name',
    path     => '/etc/nginx/sites-available/default',
    line     => 'rewrite ^/redirect_me osama.basheer.me permanent;',
}

service { nginx:
    ensure => running,
}
