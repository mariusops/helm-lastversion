# https://github.com/dvershinin/lastversion
import lastversion

keycloak_url = 'https://github.com/codecentric/helm-charts/tree/master/charts/keycloak'
nfs_url = 'https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner/blob/master/charts/nfs-subdir-external' \
      '-provisioner '
grafana_url = 'https://github.com/grafana/helm-charts/tree/main/charts/grafana'
jenkins_url = 'https://github.com/bitnami/charts/blob/master/bitnami/jenkins'
kibana_url = 'https://github.com/bitnami/charts/tree/master/bitnami/kibana'


# Checking last version of repo
def get_last_version(url):
    print(lastversion.latest(url))


# Checks if there's a newer version than the one you passed as version
def has_update(name, version, url):
    latest_version = lastversion.has_update(repo=url, current_version=version)
    if latest_version:
        print("Newer {} helm version is available: {} (Current version {})".format(name, str(latest_version), version))
    else:
        print('No update is available')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    has_update('keycloak', '10.2.0', keycloak_url)
