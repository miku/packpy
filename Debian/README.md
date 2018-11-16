dh-virtualenv
-------------

* Homepage: https://github.com/spotify/dh-virtualenv

Skip boilerplate with cookiecutter.

```
$ pip install cookiecutter
$ cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
```

If you are on OS X, you might want to use Vagrant to boot up a Linux box
to test debian packaging of Python packages via dh-virtualenv.

```
$ vagrant init ubuntu/trusty64
$ vagrant ssh
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install debhelper
$ sudo apt-get install devscripts
$ sudo apt-get install python-virtualenv git equivs

At the time of writing, the latest version was maintained by the author, here:

* https://launchpad.net/~spotify-jyrki/+archive/ubuntu/dh-virtualenv

```
$ sudo add-apt-repository ppa:spotify-jyrki/dh-virtualenv
$ sudo apt-get update
````

Otherwise just:

```
$ sudo apt-get install dh-virtualenv
```

Change into the mounted directory and buid package:

```
$ cd /vagrant/zing
$ dpkg-buildpackage -us -uc
```

You should see a new package in the parent directory:

```
$ dpkg -c ../zing_0.1-1_amd64.deb
```
