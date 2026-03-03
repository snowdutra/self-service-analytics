FROM postgres:15

ENV POSTGRES_DB=imobiliaria
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin123

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432