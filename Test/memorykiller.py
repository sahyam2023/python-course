import psutil
import time
import logging
from datetime import datetime, timedelta

# Configuration
process_name = "analytic_server.exe"
log_file = "process_metrics_log.txt"
interval = 60  # Interval in seconds
memory_usage_threshold_percent = 95  # Threshold in percentage of total memory
memory_usage_threshold_mb = 60000  # Absolute memory usage threshold in MB (60 GB)
sleep_after_kill = timedelta(hours=3)  # Sleep duration after killing the process
last_kill_time = None  # Tracks the last kill time

# Set up logging
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def get_process_metrics(process_name):
    """Get detailed metrics of each instance of the specified process."""
    metrics_reports = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'memory_percent']):
        if proc.info['name'] == process_name:
            pid = proc.info['pid']

            try:
                cpu_usage = proc.info['cpu_percent']
                if cpu_usage > 100:
                    cpu_usage = 100  # Cap CPU usage to 100%

                memory_usage_mb = proc.info['memory_info'].rss / (1024 * 1024)  # Convert bytes to MB
                memory_usage_percent = proc.memory_percent()  # Memory usage as a percentage of total memory

                # Log metrics
                log_entry = (f"PID {pid} ({process_name}): CPU Usage: {cpu_usage:.2f}%, "
                             f"Memory Usage: {memory_usage_mb:.2f} MB ({memory_usage_percent:.2f}%)")
                metrics_reports.append((log_entry, memory_usage_percent, memory_usage_mb, pid, proc))
            except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                logging.error(f"Error accessing metrics for PID {pid}: {e}")
    
    return metrics_reports

# Create or clear the log file
open(log_file, 'w').close()

# Monitor the process in an infinite loop
while True:
    current_time = datetime.now()

    if last_kill_time is None or (current_time - last_kill_time) > sleep_after_kill:
        metrics_reports = get_process_metrics(process_name)

        for metrics, memory_usage_percent, memory_usage_mb, pid, proc in metrics_reports:
            logging.info(metrics)

            if memory_usage_percent > memory_usage_threshold_percent or memory_usage_mb > memory_usage_threshold_mb:
                logging.critical(f"High memory usage detected for PID {pid}: {memory_usage_percent:.2f}% "
                                 f"({memory_usage_mb:.2f} MB). Terminating process.")
                proc.terminate()  # Terminate the process
                logging.info(f"Process with PID {pid} has been terminated due to high memory usage.")
                last_kill_time = current_time  # Update the last kill time
                break  # Break to sleep after terminating the process

    else:
        logging.info(f"Skipping monitoring as the process was terminated within the last {sleep_after_kill}. Next check at {last_kill_time + sleep_after_kill}")

    # Wait before the next iteration
    time.sleep(interval)
