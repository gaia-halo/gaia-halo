[![Build Status](http://img.shields.io/travis/TokTok/py-toxcore-c.svg)](https://travis-ci.org/TokTok/py-toxcore-c)
[![Coverage Status](https://coveralls.io/repos/github/TokTok/py-toxcore-c/badge.svg?branch=master)](https://coveralls.io/github/TokTok/py-toxcore-c?branch=master)

# PyTox

Python binding for [Project Tox](https://github.com/TokTok/c-toxcore).

# Docker

```
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```

PyTox provides a Pythonic binding, i.e Object-oriented instead of C style, raise
exception instead of returning error code. A simple example is as follows:

```
mkdir /data
```

```
cd /data
```

```
apt-get update 
```

```
apt-get install git
```

```
git clone https://github.com/gaia-halo/py_tox.git
```

```
cd py_tox
```

```
docker build -t pytox .
```

```
docker run --name -it -v /data:/data pytox /bin/bash
```

```
docker exec -it pytox /bin/bash
```

# in docker

```
apt-get update -y
```

```
apt-get install vim
```

```
vim /etc/ld.so.conf
```

```
include /etc/ld.so.conf.d/*.conf
/usr/local/lib
```

```
ldconfig
```

```
git clone https://github.com/gaia-halo/py_tox.git
```

```
cd py_tox
```

```
python examples/echo.py
```

```
docker exec -it # /bin/bash
```
