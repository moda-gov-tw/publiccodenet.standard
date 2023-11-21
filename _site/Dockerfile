# OS: Ubuntu 22.04

FROM ubuntu:22.04

WORKDIR /var/www/html

ENV TZ="Asia/Taipei"

ENV GIT_COMPLETION_URL="https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash"

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y software-properties-common ca-certificates lsb-release apt-transport-https \
    && apt-get install -y zip unzip curl vim wget cron

RUN add-apt-repository ppa:ondrej/php \
    && apt-get update

RUN apt-get install -y apache2 apache2-utils

RUN apt-get install -y git curl autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm6 libgdbm-dev libdb-dev

RUN curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
RUN echo 'eval "$(rbenv init -)"' >> ~/.bashrc

RUN ~/.rbenv/bin/rbenv init -
RUN ~/.rbenv/bin/rbenv install 3.1.3
RUN ~/.rbenv/bin/rbenv global 3.1.3

RUN ~/.rbenv/shims/gem install bundler jekyll

# 中文語系顯示
RUN apt-get install -y locales language-pack-zh-hans
RUN locale-gen zh_TW.UTF-8

RUN apt-get -y autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN a2enmod rewrite && a2enmod proxy && a2enmod proxy_http

# 中文語系顯示
RUN echo "export LANG=zh_TW.UTF-8" >> /root/.bashrc
RUN echo "export LC_ALL=zh_TW.UTF-8" >> /root/.bashrc
RUN echo 'PS1="\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\u@\h:\W\$ "' >> /root/.bashrc

CMD ["apache2ctl", "-D", "FOREGROUND"]
EXPOSE 80

