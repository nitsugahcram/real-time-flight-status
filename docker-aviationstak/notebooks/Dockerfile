ARG BASE_CONTAINER=python:3.8-slim-buster

# docker pull ubuntu:bionic
FROM $BASE_CONTAINER
## Base on https://github.com/jupyter/docker-stacks/blob/master/base-notebook/Dockerfile
LABEL maintainer="Nitsuga Chram <agustin.march@gmail.com>"
ARG NB_USER=analytics
ARG NB_UID=1000
ARG NB_GID=100
# default password for user
ARG PW=docker

USER root

ENV DEBIAN_FRONTEND noninteractive

# Option1: Using unencrypted password/ specifying password
RUN groupadd -g ${NB_GID} -o ${NB_GROUP:-${NB_USER}}
RUN useradd -m ${NB_USER} --uid=${NB_UID} -g ${NB_GID}  && echo "${NB_USER}:${PW}" | chpasswd
# Configure environment
ENV SHELL=/bin/bash \
    USER=$NB_USER \
    UID=$NB_UID \
    GID=$NB_GID

ENV HOME=/home/${NB_USER} \
    PATH=/home/${NB_USER}/.local/bin:${PATH}

##SUDO USERS
RUN apt-get update && apt-get install --no-install-recommends -y sudo && \
    echo "$NB_USER ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/notebook

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential inkscape \
    pandoc texlive-xetex texlive-fonts-recommended jq \
    curl git zip unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ## Install AWS CLI 2
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
#     unzip awscliv2.zip && \
#     ./aws/install 

# Copy a script that we will use to correct permissions after running certain commands
COPY fix-permissions /usr/local/bin/fix-permissions
RUN chmod a+rx /usr/local/bin/fix-permissions

# RUN fix-permissions ${HOME}
# Enable prompt color in the skeleton .bashrc before creating the default NB_USER
RUN sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' /etc/skel/.bashrc
USER $NB_UID
WORKDIR $HOME
# Setup work directory for backward-compatibility
RUN fix-permissions /home/${USER}
RUN pip3 install -U jupyter-book yapf \
    isort autopep8 RISE ipywidgets \
    boto3 iplantuml ruamel-yaml pandas matplotlib seaborn pandoc \
    numpy pyarrow \
    scipy statsmodels \
    psutil nbresuse \
    psycopg2-binary \
    jupyter_contrib_nbextensions jupyterthemes && \
    jupyter contrib nbextension install --user


RUN jupyter nbextension enable codefolding/main && \
    jupyter nbextension enable spellchecker/main && \
    jupyter nbextension enable collapsible_headings/main && \
    jupyter nbextension enable snippets_menu/main && \
    jupyter nbextension enable code_prettify/code_prettify && \
    jupyter nbextension enable code_prettify/isort && \
    jupyter nbextension enable execute_time/ExecuteTime && \
    jupyter nbextension enable zenmode/main && \
    jupyter nbextension enable toc2/main && \
    jupyter nbextension enable toggle_all_line_numbers/main && \
    jupyter nbextension enable splitcell/splitcell && \
    jupyter nbextension enable freeze/main && \
    jupyter nbextension enable scratchpad/main && \
    jupyter nbextension enable rise/main && \
    jupyter nbextension enable highlighter/highlighter && \
    jupyter nbextension enable hide_input/main && \
    jupyter nbextension enable move_selected_cells/main && \
    jupyter nbextension enable hide_input_all/main

#
# Copy local files as late as possible to avoid cache busting
COPY start.sh start-notebook.sh start-singleuser.sh /usr/local/bin/

USER root
RUN jupyter serverextension enable --py nbresuse --sys-prefix && \
    jupyter nbextension install --py nbresuse --sys-prefix && \
    jupyter nbextension enable --py nbresuse --sys-prefix && \
    jupyter nbextension enable nbresuse --py --sys-prefix

# Spark dependencies
# ENV APACHE_SPARK_VERSION=3.0.1 \
#     HADOOP_VERSION=3.2
## V2.4.6-2.7 3A9F401EDA9B5749CDAFD246B1D14219229C26387017791C345A23A65782FB8B25A302BF4AC1ED7C16A1FE83108E94E55DAD9639A51C751D81C8C0534A4A9641
## V3.0.0-3.2 BFE45406C67CC4AE00411AD18CC438F51E7D4B6F14EB61E7BF6B5450897C2E8D3AB020152657C0239F253735C263512FFABF538AC5B9FFFA38B8295736A9C387
## V3.0.1-3.2 E8B47C5B658E0FBC1E57EEA06262649D8418AE2B2765E44DA53AAF50094877D17297CC5F0B9B35DF2CEEF830F19AA31D7E56EAD950BBE7F8830D6874F88CFC3C
## Install Java RE 11 for compatibility with SPARK 3.0
# RUN mkdir --parent /usr/share/man/man1

# RUN mkdir --parent /usr/share/man/man1 && \
#     apt-get -y update && \
#     apt-get install --no-install-recommends -y openjdk-11-jre-headless ca-certificates-java wget gnupg && \
#     apt-get clean && rm -rf /var/lib/apt/lists/* && \
#     java -version

# Using the preferred mirror to download the file
# RUN cd /tmp && \
#     wget -q $(wget -qO- https://www.apache.org/dyn/closer.lua/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz\?as_json | \
#     python -c "import sys, json; content=json.load(sys.stdin); print(content['preferred']+content['path_info'])") && \
#     echo "E8B47C5B658E0FBC1E57EEA06262649D8418AE2B2765E44DA53AAF50094877D17297CC5F0B9B35DF2CEEF830F19AA31D7E56EAD950BBE7F8830D6874F88CFC3C *spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha512sum -c - && \
#     tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /usr/local --owner root --group root --no-same-owner && \
#     rm spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
# RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark

# ENV SPARK_HOME=/usr/local/spark
# ENV PATH=$PATH:${SPARK_HOME}/bin
# Spark and Mesos config
# ENV SPARK_HOME=/usr/local/spark
# ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9-src.zip:${HOME}/workspaces/ \
#     # MESOS_NATIVE_LIBRARY=/usr/local/lib/libmesos.so \
#     SPARK_OPTS="--driver-java-options=-Xms4096M --driver-java-options=-Xmx8192M --driver-java-options=-Dlog4j.logLevel=info" \
#     PATH=$PATH:$SPARK_HOME/bin

USER $NB_UID
# RUN jt -r
# EXPOSE 9001
# EXPOSE 4040
EXPOSE 8000