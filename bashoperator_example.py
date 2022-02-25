# Import the BashOperator
from airflow.operators.bash_operator import BashOperator

# Define the BashOperator 
cleanup = BashOperator(
    task_id="cleanup_task",
    # Define the bash_command
    bash_command="cleanup.sh",
    # Add the task to the dag
    dag=analytics_dag
)

# Define a second operator to run the `consolidate_data.sh` script
consolidate = BashOperator(
    task_id='consolidate_task',
    bash_command="consolidate_data.sh",
    dag=analytics_dag)

# Define a final operator to execute the `push_data.sh` script
push_data = BashOperator(
    task_id="pushdata_task",
    bash_command="push_data.sh",
    dag=analytics_dag)

# Airflow Tasks Dependencies example
# Define a new pull_sales task
pull_sales = BashOperator(
    task_id='pullsales_task',
    bash_command="wget https://salestracking/latestinfo?json",
    dag=analytics_dag
)

# Set pull_sales to run prior to cleanup
pull_sales >> cleanup

# Configure consolidate to run after cleanup
cleanup >> consolidate

# Set push_data to run last
consolidate >> push_data