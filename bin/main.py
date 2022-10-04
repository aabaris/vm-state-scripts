#!/usr/bin/env python

import yaml

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystone_client
from keystoneclient.v3 import services as services
from novaclient import client

def mk_auth(cred_name):
    with open('/root/.config/openstack/clouds.yaml') as f:
        os_cloud = yaml.load(
            f,Loader=yaml.FullLoader
        )['clouds'][cred_name]['auth']
        ac_id = os_cloud['application_credential_id']
        ac_secret = os_cloud['application_credential_secret']
        auth_url = os_cloud['auth_url']

    auth = v3.ApplicationCredential(
        auth_url=auth_url,
        application_credential_id=ac_id,
        application_credential_secret=ac_secret,
    )
    return(auth)

def main():
    ks_auth = mk_auth("nerc")
    ks_session = session.Session(ks_auth)
    ks_client = keystone_client.Client(session=ks_session)
    nova_client = client.Client(version=2,session=ks_session)
    projects = ks_client.projects.list()
    print(nova_client.servers.list(search_opts={'all_tenants':1}))
    return 0

if __name__ == "__main__":
    main()

