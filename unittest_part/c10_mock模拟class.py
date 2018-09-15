from unittest import mock


class CloudClient(object):
    def connect(self):
        pass

    def disconnect(self):
        pass

    def upload(self):
        pass

    def download(self):
        pass


tmock = mock.Mock(CloudClient)
print(dir(tmock))

tmock.connect.return_value = 200
print(tmock.connect())
