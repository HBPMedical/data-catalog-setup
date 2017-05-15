FROM hbpmip/alembic:0.9.1-0

MAINTAINER mirco.nasuti@chuv.ch

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

########################################################################################################################
# Copy project files
########################################################################################################################

COPY alembic.ini.tmpl /alembic.ini.tmpl
COPY data_catalog_schema.py /data_catalog_schema.py
COPY db_migrations/ /db_migrations/


########################################################################################################################
# Setup entrypoint and cmd
########################################################################################################################

WORKDIR /
ENTRYPOINT ["dockerize", "-template", "/alembic.ini.tmpl:/alembic.ini", "alembic"]
CMD ["help"]

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="hbpmip/data-catalog-setup" \
      org.label-schema.description="Data catalog database setup" \
      org.label-schema.url="https://github.com/LREN-CHUV/data-catalog-setup" \
      org.label-schema.vcs-type="git" \
      org.label-schema.vcs-url="https://github.com/LREN-CHUV/data-catalog-setup" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.version="$VERSION" \
      org.label-schema.vendor="LREN CHUV" \
      org.label-schema.license="Apache2.0" \
      org.label-schema.docker.dockerfile="Dockerfile" \
      org.label-schema.schema-version="1.0"
