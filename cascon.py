from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
def cascon(): 
    cloud_config= {'secure_connect_bundle': 'secure-connect-project.zip'}
    auth_provider = PlainTextAuthProvider('CBvzwoixPdIabZkbdmMsQqlA', '4fTMt_aArg182tdtubzzlI7xKIzTXN6Dxj,7C35ZySUxJwqEfl9fqrkw6LKFXAuxtTa3ZA_3lCg1bahq8mp6z2iwuiko-PHGbawOgbm.jX+urcAMHDm42n0rZ4k4CDR4')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect('iot')
    print("Connection successfull")
    return session
cascon()

