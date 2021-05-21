Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.hostname = "jenkins.local" # TODO not working
  config.vm.network "private_network", ip: "192.168.50.4", hostname: true
  config.vm.network "forwarded_port", guest: 8080, host: 8080 # Jenkins port
  config.vm.network "forwarded_port", guest: 8081, host: 8081 # Java webapp port
  config.vm.provision "shell" do |shell|
    shell.path = "jenkins.sh"
  end
end
