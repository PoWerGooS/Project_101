import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BEqP1vH92lzMa3FcJ5_uvyrLzCQG0q7WpykVbWH0SydamBNwCqET5KKSW3nl0gywkaAuShhiRHsyweKycJWjZr0qTQrtAGuM-9W38-nTjdI4OMiYXMboJ4VDd0cFizWo-rBKGJ0IWf3z'
    transferData = TransferData(access_token)

    file_from = 'text.txt'
    file_to = '/text_dropbox/text.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
main()