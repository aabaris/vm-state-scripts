#!/bin/sh
#

podman run -it \
	-v $WDIR/vm-state-scripts/bin:/root/bin:Z \
	-v $WDIR/venv:/root/osp-client:Z \
	-v $WDIR/auth:/root/.config/openstack/:Z \
	-v $WDIR/vm-state-scripts/dot.bashrc:/root/.bashrc:Z \
	python bash
