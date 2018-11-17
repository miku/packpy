Grocker
=======

```shell
$ pip install grocker
...
```

Basic usage:

```
$ grocker build ipython==7.1.1 --entrypoint ipython
```

Then run:

```shell
$ docker run --rm -ti ipython:5.0.0-5.4
...
```

Default config:

```shell
# .grocker.yml (defaults)
runtime: python3.4
pip_constraint: # optional
volumes: []
ports: []
repositories: {}
dependencies: []
docker_image_prefix: # optional
image_base_name: # optional
entrypoint_name: grocker-runner
```

Image is about 250M. Relatively small Python project:

```shell
$ loc .
--------------------------------------------------------------------------------
 Language             Files        Lines        Blank      Comment         Code
--------------------------------------------------------------------------------
 Python                  20         1708          320           50         1338
 reStructuredText         9          674          195            0          479
 CSS                      1          532           70           11          451
 Bourne Shell             2           93           17            5           71
 YAML                     2           60            7            9           44
 Plain Text               2           45            7            0           38
 Makefile                 1           21            5            0           16
 INI                      1           20            4            0           16
 Autoconf                 1            6            0            0            6
 ASP.NET                  2            2            0            0            2
--------------------------------------------------------------------------------
 Total                   41         3161          625           75         2461
--------------------------------------------------------------------------------
```

----------------

Just logs:

```
grocker: Compiling dependencies...
grocker.builders.op: Pulling image grocker-python3.4-root:5.4-17283be0deaeda63...
 ---> 40aa6d4339d4
Step 2/7 : LABEL grocker.runtime python3.4
 ---> Running in 1e5b0083c2a4
 ---> 29bfd19f70f9
Removing intermediate container 1e5b0083c2a4
Step 3/7 : ENV LANG C.UTF-8 GROCKER_VERSION 5.4 GROCKER_RUNTIME python3.4
 ---> Running in d40b97b7545d
 ---> 61ac34572352
Removing intermediate container d40b97b7545d
Step 4/7 : COPY . /tmp/grocker/
 ---> b7cb2e6e4d64
Step 5/7 : ARG SYSTEM_DEPENDENCIES
 ---> Running in 3bfef77d908e
 ---> d9d25da633aa
Removing intermediate container 3bfef77d908e
Step 6/7 : RUN /bin/sh /tmp/grocker/provision.sh
 ---> Running in 8fcfaa30c729
...
Removing intermediate container 8fcfaa30c729
Step 7/7 : LABEL grocker.image.role 'root' grocker.version '5.4'
 ---> Running in 8bce6794e44a
 ---> 5d118b844265
Removing intermediate container 8bce6794e44a
{u'aux': {u'ID': u'sha256:5d118b84426566099c02c0edf801f9d5ccd45d5fb69ddeaa0739708f1fa51099'}}
Successfully built 5d118b844265
Successfully tagged grocker-python3.4-root:5.4-17283be0deaeda63ad6fc29636a5f310bf93fdc471e5b991af253accfed702d2

grocker.builders.op: Pulling image grocker-python3.4-compiler:5.4-17283be0deaeda63ad6fc29636a5f310bf93fdc471e5b991af253accfed702d2...
Step 1/9 : FROM grocker-python3.4-root:5.4-17283be0deaeda63ad6fc29636a5f310bf93fdc471e5b991af253accfed702d2
 ---> 5d118b844265
Step 2/9 : COPY . /tmp/grocker
 ---> 679d9df082ca
Step 3/9 : ARG SYSTEM_DEPENDENCIES
 ---> Running in c1807eff79e7
 ---> 874409bfb411
Removing intermediate container c1807eff79e7
Step 4/9 : RUN /tmp/grocker/provision.sh
 ---> Running in 1b258734f5f6
+ which apt
+ apt install -qy less netcat-traditional vim python3 libpython3.4 python3-venv build-essential gettext nodejs-legacy python3-dev libpython3.4 python3-venv
....
0 upgraded, 118 newly installed, 0 to remove and 0 not upgraded.
Need to get 114 MB of archives.
After this operation, 287 MB of additional disk space will be used.
....
+ install -m 0555 -o grocker /tmp/grocker/compile.py /home/grocker/compile.py
+ install -m 0777 -o grocker -d /home/grocker/packages
+ dirname /tmp/grocker/provision.sh
+ rm -r /tmp/grocker
 ---> 7ce2043d4741
Removing intermediate container 1b258734f5f6
...
Step 5/9 : USER grocker
 ---> Running in 2dd33d9b0443
 ---> b897c1fa03ea
Removing intermediate container 2dd33d9b0443
Step 6/9 : WORKDIR /home/grocker
 ---> e752cd8785f6
Removing intermediate container 50cc5d1a603d
Step 7/9 : VOLUME /home/grocker/packages
 ---> Running in 02b569f2cc42
 ---> 8fd28788ecf1
Removing intermediate container 02b569f2cc42
Step 8/9 : ENTRYPOINT python3.4 /home/grocker/compile.py
 ---> Running in 3c82fcd71a67
 ---> 3c85c3dbc697
Removing intermediate container 3c82fcd71a67
Step 9/9 : LABEL grocker.image.role 'compiler' grocker.version '5.4'
 ---> Running in 951d685ca7cd
 ---> e2f5d56103f4
Removing intermediate container 951d685ca7cd
{u'aux': {u'ID': u'sha256:e2f5d56103f4960ee5ddf61d62073ab848c2d366cfe2414108e5d84c28756094'}}
Successfully built e2f5d56103f4
Successfully tagged grocker-python3.4-compiler:5.4-17283be0deaeda63ad6fc29636a5f310bf93fdc471e5b991af253accfed702d2
...
grocker.builders.op: Creating volume grocker-wheel-cache-5.4-python3.4-17283be0deaeda63ad6fc29636a5f310bf93fdc471e5b991af253accfed702d2...
grocker.builders.wheels: -> Pip use configuration from /Users/tir/.cache/tmpH1cYtg.
grocker.builders.op: Running [u'--python', 'python3.4', u'ipython==5.0.0'] on image grocker-python3.4-compiler:5.4-17283be0deaeda63ad6fc29636a5f310bf93fdc471e5b991af253accfed702d2 (volumes:{u'grocker-wheel-cache-5.4-python3.4-17283be0deaeda63ad6fc29636a5f310bf93fdc471e5b991af253accfed702d2': {u'bind': u'/home/grocker/packages', u'mode': u'rw'}}, environment:{})
Setup venv using python3.4...
...
Downloading/unpacking wheel
Installing collected packages: pip, setuptools, wheel
  Found existing installation: pip 1.5.6
    Uninstalling pip:
      Successfully uninstalled pip
  Found existing installation: setuptools 5.5.1
    Uninstalling setuptools:
      Successfully uninstalled setuptools
Successfully installed pip setuptools wheel
Cleaning up...
Setup pip...
Building wheels for ipython==5.0.0...
Collecting ipython==5.0.0
  Downloading ipython-5.0.0-py2.py3-none-any.whl (743kB)
  Saved ./packages/ipython-5.0.0-py2.py3-none-any.whl
Collecting traitlets>=4.2 (from ipython==5.0.0)
...
grocker: Building image...
grocker.builders.op: Pulling image grocker-wheel-server:5.4...
Step 1/3 : FROM nginx:alpine
...
Step 2/3 : COPY nginx.conf /etc/nginx/nginx.conf
 ---> ee3322d6900e
Step 3/3 : LABEL grocker.image.role 'wheel-server' grocker.version '5.4'
 ---> Running in ed94c0db2624
 ---> 1a816af0dc2e
Removing intermediate container ed94c0db2624
{u'aux': {u'ID': u'sha256:1a816af0dc2eed035180056c27aafe5d0f8e87e2c666691438f9311d93742e6d'}}
Successfully built 1a816af0dc2e
Successfully tagged grocker-wheel-server:5.4
...
grocker.builders.build: Starting http server in container: ec9e248b063321f902292262c5f9ef069f016809cc6b01cab8fee3b0019f4a90
Step 1/10 : FROM grocker-python3.4-root:5.4-17283be0deaeda63ad6fc29636a5f310bf93fdc471e5b991af253accfed702d2
 ---> 5d118b844265
Step 2/10 : LABEL grocker.app.name ipython grocker.app.extras  grocker.app.version 5.0.0
 ---> Running in 269dfca8ae85
 ---> 764ec7b2e6fc
Removing intermediate container 269dfca8ae85
Step 3/10 : ENV GROCKER_APP ipython GROCKER_APP_EXTRAS  GROCKER_APP_VERSION 5.0.0 PATH /home/grocker/app.venv/bin/:${PATH}
 ---> Running in 648188e1d86c
 ---> d52f8cf09504
Removing intermediate container 648188e1d86c
Step 4/10 : ARG GROCKER_WHEEL_SERVER_IP
 ---> Running in 2a832b1eb044
 ---> a85e79550c7f
Removing intermediate container 2a832b1eb044
Step 5/10 : COPY . /tmp/grocker
 ---> 1e67015d288f
...
Step 6/10 : RUN /bin/sh /tmp/grocker/provision.sh
 ---> Running in 8943834ea9a6
+ GROCKER_USER=grocker
+ dirname /tmp/grocker/provision.sh
+ WORKING_DIR=/tmp/grocker
+ only_run_as_root system_provision
+ local script_or_function
+ script_or_function=system_provision
+ whoami
+ [ root = root ]
+ system_provision
+ which apt
/usr/bin/apt
+ debian_up
+ apt update
...
Removing intermediate container 06d40a13ad80
{u'aux': {u'ID': u'sha256:52f704f2cbe7a750ef713af68d3cea4e06964aa9248f8e7f7e5d9dea017e6636'}}
Successfully built 52f704f2cbe7
Successfully tagged ipython:5.0.0-5.4
...
grocker: Not pushing any image since the registry is unclear in ipython:5.0.0-5.4
```
