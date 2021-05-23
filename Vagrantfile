IMAGE_NAME = "hashicorp/bionic64"

Vagrant.configure("2") do |config|

  config.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 2
  end

  config.vm.define "jenkins" do |master|
    master.vm.box = IMAGE_NAME
    master.vm.network "private_network", ip: "192.168.50.4"
    master.vm.hostname = "jenkins"
    master.vm.network "forwarded_port", guest: 8080, host: 8080, auto_correct: true # Jenkins port
    master.vm.network "forwarded_port", guest: 8081, host: 8081, auto_correct: true # Java webapp port
    master.vm.provision "shell" do |shell|
      shell.path = "jenkins.sh"
    end
    master.vm.provision "ansible" do |ansible|
      ansible.playbook = "jenkins/docker-playbook.yml"
    end
  end
end
