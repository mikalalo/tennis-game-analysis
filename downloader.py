import requests
from analyzer import process_data
from timeit import default_timer as timer

def download():
    print("RUNNING 'tennis-competitive-scoring")

    url_list = [
        'https://raw.githubusercontent.com/JeffSackmann/tennis_MatchChartingProject/master/charting-w-points-2010s.csv',
        'https://raw.githubusercontent.com/JeffSackmann/tennis_MatchChartingProject/master/charting-w-points-2020s.csv',
    ]

    aggregated_data = []
    for url in url_list:
        start_time = timer()   
        req = requests.get(url)
        data = req.text.split('\n')
        data.pop(0)
        data.pop()
        end_time = timer()   
        print(f'  - DOWNLOADED ../{url.split('/')[-1]} in {(end_time - start_time):.2} seconds\n')
        aggregated_data.extend(data)

    return process_data(aggregated_data)


