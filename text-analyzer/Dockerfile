FROM smizy/scikit-learn

# Set the WORKDIR to be the folder
COPY . /app
# Expose port 5000
EXPOSE 5000
ENV PORT 5000
WORKDIR /app

# RUN pip install -r requirements.txt

RUN apk add libgomp

# RUN python -m pip install --no-build-isolation --user numpy scipy matplotlib ipython jupyter pandas sympy nose flask gunicorn

RUN python -m pip install --no-build-isolation numpy scipy matplotlib ipython jupyter pandas sympy nose flask gunicorn
# RUN pip3 install scikit-learn==0.19.1
# RUN pip3 install --no-build-isolation scikit-learn==0.19.1
RUN pip3 install scikit-learn flask gunicorn

# CMD python main.py
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 60 main:app
