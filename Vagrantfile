Vagrant.configure('2') do |config|
  config.vm.box     = 'Flagrant'
  config.vm.box_url = 'ubuntu/trusty64'
  config.vm.synced_folder './app','/home/vagrant/app', create:true
  config.vm.network :private_network, ip: '192.168.42.42'
  config.vm.provision :shell, :path => 'setup.sh'
end
