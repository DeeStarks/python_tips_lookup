from celery.decorators import task
from celery.schedules import crontab
from .models import PythonTip
import pandas as pd
import os

@task
def fetch_data():
    data_folder = os.listdir("data_files/")
    for file in data_folder:
        tips = pd.read_csv(f"data_files/{file}")
        tips.columns = [col.replace(' ', '_').replace(':', '').lower() for col in tips.columns]
        for i, tip in tips.iterrows():
            if tip.python_tip not in [tip.tip for tip in PythonTip.objects.all()]:
                PythonTip.objects.create(
                    tip=tip.python_tip,
                    poster=tip.your_name_or_twitter_id,
                    poster_email=tip.your_email,
                    timestamp=tip.timestamp
                )
    print("Data Fetched!")