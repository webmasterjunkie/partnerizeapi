import csv
import json
import requests
import sys
from src.lib.udf import progress_bar

PARTICIPATION_HEADERS = [
    'publisher_id',
    'account_name',
    'reporting_identifier',
    'camref',
    'vertical_name',
    'promotional_method_name',
    'operating_country',
    'contact_locale',
    'company_name',
    'created',
    'network_status',
    'campaign_status',
    'campaign_approved',
    'contact_email',
    'phone',
    'signup_ip',
]


def save_publishers(campaign, publishers):
    with open('out/' + campaign + '_publishers.out', 'a', newline='') as file:
        campaign_csv = csv.writer(file, delimiter=',')
        for i in publishers:
            row = []
            for h in PARTICIPATION_HEADERS:
                row.append(i["publisher"][h])
            campaign_csv.writerow(row)


def publishers(a, url):
    if a.campaign_id is None:
        print('\033[91mYou must provide a Partnerize campaign_id using the -c or --campaign_id flag.\033[91m')
        sys.exit()

    api_url = '/campaign/' + a.campaign_id + '/publisher.json'

    with open('out/' + a.campaign_id + '_publishers.out', 'w', newline='') as file:
        campaign_csv = csv.writer(file, delimiter=',')
        campaign_csv.writerow(PARTICIPATION_HEADERS)

    i = 0
    while api_url is not None:
        r = requests.get(url + api_url, auth=(a.application_key, a.user_key))
        partnerize = json.loads(r.text)
        save_publishers(a.campaign_id, partnerize["publishers"])
        api_url = partnerize["hypermedia"]["pagination"]["next_page"]

        i = i + 1
        progress_bar(i, partnerize["hypermedia"]["pagination"]["total_page_count"], prefix='Progress:',
                     suffix='Complete', length=50)
