# linux docker image
FROM ubuntu:latest

# commands to for installation
RUN apt-get update && \
    apt-get install -y git sudo fortune-mod cowsay && \
    apt-get clean


#cloning the repository
RUN git clone https://github.com/nyrahul/wisecow.git /opt/wisecow

# changeing the directory
WORKDIR /opt/wisecow

#exposing to the ports
EXPOSE 4499

# command to run the application
CMD ["./wisecow.sh"]
