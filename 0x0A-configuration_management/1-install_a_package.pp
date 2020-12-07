# Installs puppet-lint on a machine
package { 'puppet-lint':
  ensure   => '2.1.0',
  provider => 'gem',
}
