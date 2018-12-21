FROM python:3.7.1-stretch

# Install Postgres
RUN sudo apt-get update && \
    sudo apt-get install postgresql postgresql-contrib

# Create Database
RUN sudo service postgresql start && \
    sudo -u postgres psql -c 'createdb budgetapp'

# Install application requirements
RUN pip install -r requirements.txt
