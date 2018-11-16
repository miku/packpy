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
$ vagrant init debain/stretch64
$ vagrant ssh
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install debhelper devscripts python-virtualenv git equivs
$ sudo apt-get install dh-virtualenv

Change into the mounted directory and buid package:

```
$ cd /vagrant/zing
$ dpkg-buildpackage -us -uc
```

You should see a new package in the parent directory:

```
$ dpkg -c ../zing_0.1-1_amd64.deb
```

To install the package:

```
$ sudo dpkg -i ../zing_0.1-1_amd64.deb
```
