import psutil
import time
import logging
from datetime import datetime

# Configuration
process_name = "analytic_server.exe"
log_file = "process_metrics_log.txt"
interval = 60  # Interval in seconds
memory_usage_threshold_percent = 95  # Threshold to kill the process (in percentage of total memory)

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
                metrics_reports.append((log_entry, memory_usage_percent, pid, proc))
            except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                logging.error(f"Error accessing metrics for PID {pid}: {e}")
    
    return metrics_reports

# Create or clear the log file
open(log_file, 'w').close()

# Monitor the process in an infinite loop
while True:
    metrics_reports = get_process_metrics(process_name)

    for metrics, memory_usage_percent, pid, proc in metrics_reports:
        logging.info(metrics)

        if memory_usage_percent > memory_usage_threshold_percent:
            logging.critical(f"High memory usage detected for PID {pid}: {memory_usage_percent:.2f}%. Terminating process.")
            proc.terminate()  # Terminate the process
            logging.info(f"Process with PID {pid} has been terminated due to high memory usage.")

    # Wait before the next iteration
    time.sleep(interval)
