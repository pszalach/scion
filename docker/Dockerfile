FROM scion_base:latest

# Now copy over the current branch
COPY . $BASE/
RUN sudo chown -R scion: $BASE

# Restore the go dependency cache from scion_base
RUN tar xf ~/go_vendor.tar.gz -C go/vendor/

# Make sure dependencies haven't been changed since scion_base was rebuilt
RUN docker/deps_check

# Syncing should be a no-op, just need installation to run
RUN make -C go deps

# Setup scion-web
RUN cp sub/web/web_scion/settings/private.dist.py sub/web/web_scion/settings/private.py
RUN sub/web/manage.py makemigrations

# Build topology files
RUN ./scion.sh topology
