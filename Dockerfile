FROM inemo/isanlp_base
ENV MODEL_NAME ru_core_news_lg

RUN apt update
RUN apt install libffi-dev

RUN pyenv install 3.7.2
RUN pyenv global 3.7.2

COPY requirements.txt .
RUN pip install -U pip \
    && pip install grpcio git+https://github.com/IINemo/isanlp.git \
    && pip install -r requirements.txt

RUN python -m spacy download $MODEL_NAME

COPY pipeline_object.py .
CMD [ "python", "/start.py", "-m", "pipeline_object", "-a", "create_pipeline", "--no_multiprocessing", "True"]