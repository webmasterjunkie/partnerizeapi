import argparse
import sys


class PartnerizeApi:
    def __init__(self):
        self.main()

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--application_key', default=None, help='Application API Key')
        parser.add_argument('-p', '--user_key', default=None, help='User API Key')
        parser.add_argument('-s', '--subdomain', default='api', help='The Partnerize API domain to use')
        parser.add_argument('-c', '--campaign_id', default=None, help='The Partnerize campaign to use')
        parser.add_argument('-m', '--method', default=None, help='The endpoint to call on Partnerize')
        a = parser.parse_args()

        if a.application_key is None:
            print(
                '\033[91mYou must provide a Partnerize application_api_key using the -u or --application_key '
                'flag.\033[91m')
            sys.exit()
        if a.user_key is None:
            print('\033[91mYou must provide a Partnerize user_api using the -p or --user_key flag.\033[91m')
            sys.exit()

        return a

    def main(self):
        min_python = (3, 6)
        if sys.version_info < min_python:
            sys.exit('Python %s.%s or later is required.\n' % min_python)

        a = self.get_args()
        if a.subdomain == 'api':
            url = 'https://api.partnerize.com/'
        else:
            url = 'https://' + a.subdomain + '-api.partnerize.com'

        if a.method == 'publishers':
            from lib.campaign import publishers
            publishers(a, url)


if __name__ == '__main__':
    PartnerizeApi()
