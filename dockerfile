from jupyter/base-notebook:notebook-6.4.8
USER root
RUN pip3 uninstall jupyterlab -y
RUN python3 -m pip install -U pip wheel setuptools

COPY magic_package /home/jovyan/magic_package
RUN pip3 install -e  /home/jovyan/magic_package 

USER jovyan
RUN mkdir /home/jovyan/workspace
RUN chown jovyan:users /home/jovyan/workspace


COPY jupyter_notebook_config.py /home/jovyan/.jupyter/jupyter_notebook_config.py