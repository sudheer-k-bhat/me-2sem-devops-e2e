Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.network "forwarded_port", guest: 8080, host: 8080 # Jenkins port
  config.vm.network "forwarded_port", guest: 8081, host: 8081 # Java webapp port
  config.vm.provision "shell" do |shell|
    shell.path = "jenkins.sh"
  end
end
