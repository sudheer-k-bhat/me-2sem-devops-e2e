# Lifecycle mgt
vagrant init hashicorp/bionic64
vargant up
vagrant ssh
vagrant reload
vagrant reload --provision
vagrant destroy
vagrant suspend # hibernate
vagrant halt # shutdown
vagrant global-status

# Image management
vagrant box add hashicorp/bionic64
vagrant box list
vagrant box remove ubuntu/trusty64

#
vagrant plugin install vagrant-vbguest