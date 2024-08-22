import psutil
import time
import logging
import matplotlib.pyplot as plt
from collections import deque
from datetime import datetime, timedelta
from tkinter import Tk, Label, Button

# Configuration
process_name = "analytic_server.exe"
log_file = "process_metrics_log.txt"
interval = 60  # Interval in seconds
handle_threshold = 2000  # Adjusted threshold for handles
thread_threshold = 1000  # Adjusted threshold for threads
memory_leak_threshold_mb = 6000  # Adjusted threshold for memory leak detection (in MB)
history_length = 100  # Number of data points to keep for graphs

# Set up logging
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize data storage for graphs
cpu_usage_histories = {}
memory_usage_histories = {}
handle_count_histories = {}
thread_count_histories = {}

# Initialize timing for hourly graph generation
last_graph_time = datetime.now()
hourly_interval = timedelta(hours=1)

# Tkinter Popup Window
def show_popup(message):
    """Display a popup with a message."""
    root = Tk()
    root.title("Process Monitoring Alert")
    
    label = Label(root, text=message, padx=20, pady=20)
    label.pack()
    
    button = Button(root, text="OK", command=root.destroy, padx=10, pady=5)
    button.pack(pady=10)
    
    root.mainloop()

def get_process_metrics(process_name):
    """Get detailed metrics of each instance of the specified process."""
    metrics_reports = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'num_handles', 'num_threads']):
        if proc.info['name'] == process_name:
            pid = proc.info['pid']

            # Initialize history for each process if not already done
            if pid not in cpu_usage_histories:
                cpu_usage_histories[pid] = deque(maxlen=history_length)
                memory_usage_histories[pid] = deque(maxlen=history_length)
                handle_count_histories[pid] = deque(maxlen=history_length)
                thread_count_histories[pid] = deque(maxlen=history_length)

            try:
                cpu_usage = proc.info['cpu_percent']
                # Ensure CPU usage is within 0-100%
                cpu_usage = min(cpu_usage, 100.0)
                
                memory_usage_mb = proc.info['memory_info'].rss / (1024 * 1024)  # Convert bytes to MB
                handle_count = proc.info['num_handles']
                thread_count = proc.info['num_threads']

                # Store metrics for each process
                cpu_usage_histories[pid].append(cpu_usage)
                memory_usage_histories[pid].append(memory_usage_mb)
                handle_count_histories[pid].append(handle_count)
                thread_count_histories[pid].append(thread_count)

                # Detect anomalies for each process
                anomaly_report = ""
                if handle_count > handle_threshold:
                    anomaly_report += f"High handle count detected for PID {pid}: {handle_count} handles (threshold: {handle_threshold}). "
                if thread_count > thread_threshold:
                    anomaly_report += f"High thread count detected for PID {pid}: {thread_count} threads (threshold: {thread_threshold}). "
                if memory_usage_mb > memory_leak_threshold_mb:
                    anomaly_report += f"Potential memory leak detected for PID {pid}: {memory_usage_mb:.2f} MB (threshold: {memory_leak_threshold_mb} MB). "

                # Log metrics
                log_entry = (f"PID {pid} ({process_name}): CPU Usage: {cpu_usage:.2f}%, Memory Usage: {memory_usage_mb:.2f} MB, "
                             f"Handle Count: {handle_count}, Thread Count: {thread_count}. {anomaly_report}")
                metrics_reports.append((log_entry, anomaly_report, pid))
            except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                logging.error(f"Error accessing metrics for PID {pid}: {e}")
    
    return metrics_reports

def detect_memory_leak(last_memory_usage_mb, current_memory_usage_mb):
    """Detect if memory usage has significantly increased."""
    return current_memory_usage_mb > last_memory_usage_mb * 1.1  # 10% increase as a simple heuristic

def plot_graphs():
    """Generate and save graphs for each process being monitored."""
    plt.figure(figsize=(10, 8))

    for pid in cpu_usage_histories:
        plt.clf()  # Clear the figure to plot individual graphs

        # Plot CPU usage
        plt.subplot(2, 2, 1)
        plt.plot(cpu_usage_histories[pid])
        plt.title(f'CPU Usage (%) for PID {pid}')
        plt.xlabel('Time (intervals)')
        plt.ylabel('CPU Usage (%)')

        # Plot Memory usage
        plt.subplot(2, 2, 2)
        plt.plot(memory_usage_histories[pid])
        plt.title(f'Memory Usage (MB) for PID {pid}')
        plt.xlabel('Time (intervals)')
        plt.ylabel('Memory Usage (MB)')

        # Plot Handle count
        plt.subplot(2, 2, 3)
        plt.plot(handle_count_histories[pid])
        plt.title(f'Handle Count for PID {pid}')
        plt.xlabel('Time (intervals)')
        plt.ylabel('Handle Count')

        # Plot Thread count
        plt.subplot(2, 2, 4)
        plt.plot(thread_count_histories[pid])
        plt.title(f'Thread Count for PID {pid}')
        plt.xlabel('Time (intervals)')
        plt.ylabel('Thread Count')

        plt.tight_layout()
        plt.savefig(f'process_metrics_graphs_pid_{pid}.png')

    plt.close()

# Create or clear the log file
open(log_file, 'w').close()

last_memory_usage_mb = {}

# Show a popup at the start to indicate that monitoring has begun
show_popup("Process monitoring has started. The script will run in the background and alert if anomalies are detected.")

# Monitor the process in an infinite loop
while True:
    metrics_reports = get_process_metrics(process_name)

    for metrics, anomaly_report, pid in metrics_reports:
        if anomaly_report:
            logging.warning(f"Anomaly detected for PID {pid}: {anomaly_report}")
            show_popup(f"Anomaly detected for PID {pid}! Check the logs for details.")
            plot_graphs()  # Optionally generate graph for anomalies

        if pid in last_memory_usage_mb and detect_memory_leak(last_memory_usage_mb[pid], memory_usage_histories[pid][-1]):
            logging.warning(f"Memory leak detected for PID {pid}: Memory usage increased from {last_memory_usage_mb[pid]:.2f} MB to {memory_usage_histories[pid][-1]:.2f} MB")
            show_popup(f"Memory leak detected for PID {pid}! Check the logs for details.")
            plot_graphs()  # Generate graph for detected memory leak

        last_memory_usage_mb[pid] = memory_usage_histories[pid][-1]

        # Update real-time monitoring in console
        print(metrics)

    # Plot and save graphs every hour
    current_time = datetime.now()
    if current_time - last_graph_time >= hourly_interval:
        plot_graphs()
        last_graph_time = current_time

    # Wait before the next iteration
    time.sleep(interval)
