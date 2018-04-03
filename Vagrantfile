# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  #config.vm.box = "ubuntu/xenial64" # official ubuntu box
  config.vm.box = "bento/ubuntu-16.04"

  config.vm.network :private_network, ip: "192.168.10.10"
  config.vm.hostname = "smreka"

  config.vm.network :forwarded_port, guest: 80, host: 80
  config.vm.network :forwarded_port, guest: 8080, host: 8080

  config.vm.synced_folder "./", "/var/www/", type: "nfs"

  config.ssh.forward_agent = true

  config.vm.provider :virtualbox do |vb|
  
  	#fix for https://github.com/chef/bento/issues/688
  	vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
  	
    vb.customize ["modifyvm", :id, "--memory", "2048"]
    vb.customize ["modifyvm", :id, "--cpus", "1"]
    vb.name = "smreka"
    vb.gui = true

  end

end
