from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'PY',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 24),  # Start on a Thursday
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'weekly_push_to_github',
    default_args=default_args,
    description='Run script weekly and push to GitHub',
    schedule='0 0 * * 4',  # Every Thursday at midnight',
    catchup=False
)

run_python_script = BashOperator(
    task_id='run_team_script',
    bash_command='echo "Running script" && /opt/anaconda3/bin/python3 /Users/papayaw/projects/premtracker/PremTracker.py',
    dag=dag
)

