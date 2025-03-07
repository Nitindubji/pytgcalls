ARG python_version="3.6"
ARG dname="amd64"
ARG pname="manylinux2014_x86_64"
FROM ${dname}/python:${python_version}-buster
RUN \
  echo "deb https://deb.nodesource.com/node_16.x buster main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
  wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  apt-get update && \
  apt-get install -yqq nodejs yarn && \
  pip install -U pip && pip install pipenv && \
  npm i -g npm@^7 && \
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python && ln -s /root/.poetry/bin/poetry /usr/local/bin && \
  rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/pytgcalls
WORKDIR pytgcalls/
COPY pytgcalls/ .
WORKDIR ../src/
COPY src/* .
WORKDIR ..
COPY .npmignore .
COPY package.json .
COPY tsconfig.json .
COPY setup.py .
COPY LICENSE .
COPY README.md .
COPY requirements.txt .
ARG pname
ARG python_version
RUN python${python_version} setup.py sdist bdist_wheel --plat-name ${pname}
WORKDIR /usr/src/installer
COPY platforms/linux/linux_mount.sh /usr/src/installer
RUN chmod +x /usr/src/installer/linux_mount.sh
VOLUME ['/usr/src/installer', '/usr/src/pytgcalls']
