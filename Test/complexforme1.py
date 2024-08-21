import psutil
import time
import logging
import matplotlib.pyplot as plt
from collections import deque

# Configuration
process_name = "analytic_server.exe"
log_file = "process_metrics_log.txt"
interval = 60  # Interval in seconds
handle_threshold = 1000  # Example threshold for handles
thread_threshold = 50    # Example threshold for threads
memory_leak_threshold_mb = 500  # Example threshold for memory leak detection (in MB)
history_length = 100  # Number of data points to keep for graphs

# Set up logging
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize data storage for graphs
cpu_usage_history = deque(maxlen=history_length)
memory_usage_history = deque(maxlen=history_length)
handle_count_history = deque(maxlen=history_length)
thread_count_history = deque(maxlen=history_length)

def get_process_metrics(process_name):
    """Get detailed metrics of the specified process."""
    for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_info', 'num_handles', 'num_threads']):
        if proc.info['name'] == process_name:
            cpu_usage = proc.info['cpu_percent']
            memory_usage_mb = proc.info['memory_info'].rss / (1024 * 1024)  # Convert bytes to MB
            handle_count = proc.info['num_handles']
            thread_count = proc.info['num_threads']

            # Detect anomalies
            anomaly_report = ""
            if handle_count > handle_threshold:
                anomaly_report += f"High handle count detected: {handle_count} handles (threshold: {handle_threshold}). "
            if thread_count > thread_threshold:
                anomaly_report += f"High thread count detected: {thread_count} threads (threshold: {thread_threshold}). "
            
            # Detect memory leaks
            memory_leak_detected = False
            if memory_usage_mb > memory_leak_threshold_mb:
                memory_leak_detected = True
                anomaly_report += f"Potential memory leak detected: {memory_usage_mb:.2f} MB (threshold: {memory_leak_threshold_mb} MB). "

            # Store metrics for graphing
            cpu_usage_history.append(cpu_usage)
            memory_usage_history.append(memory_usage_mb)
            handle_count_history.append(handle_count)
            thread_count_history.append(thread_count)

            # Log metrics
            log_entry = (f"{process_name}: CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage_mb:.2f} MB, "
                         f"Handle Count: {handle_count}, Thread Count: {thread_count}. {anomaly_report}")
            return log_entry, memory_leak_detected

    return f"{process_name} not found", False

def detect_memory_leak(last_memory_usage_mb, current_memory_usage_mb):
    """Detect if memory usage has significantly increased."""
    if current_memory_usage_mb > last_memory_usage_mb * 1.1:  # 10% increase as a simple heuristic
        return True
    return False

def plot_graphs():
    """Generate and save graphs for the monitored metrics."""
    plt.figure(figsize=(10, 8))

    # Plot CPU usage
    plt.subplot(2, 2, 1)
    plt.plot(cpu_usage_history)
    plt.title('CPU Usage (%)')
    plt.xlabel('Time (intervals)')
    plt.ylabel('CPU Usage (%)')

    # Plot Memory usage
    plt.subplot(2, 2, 2)
    plt.plot(memory_usage_history)
    plt.title('Memory Usage (MB)')
    plt.xlabel('Time (intervals)')
    plt.ylabel('Memory Usage (MB)')

    # Plot Handle count
    plt.subplot(2, 2, 3)
    plt.plot(handle_count_history)
    plt.title('Handle Count')
    plt.xlabel('Time (intervals)')
    plt.ylabel('Handle Count')

    # Plot Thread count
    plt.subplot(2, 2, 4)
    plt.plot(thread_count_history)
    plt.title('Thread Count')
    plt.xlabel('Time (intervals)')
    plt.ylabel('Thread Count')

    plt.tight_layout()
    plt.savefig('process_metrics_graphs.png')
    plt.close()

# Create or clear the log file
open(log_file, 'w').close()

last_memory_usage_mb = 0

# Monitor the process in an infinite loop
while True:
    metrics, memory_leak_detected = get_process_metrics(process_name)

    if memory_leak_detected:
        logging.warning(metrics)
    else:
        logging.info(metrics)

    # Monitor memory leak over time
    if last_memory_usage_mb > 0:
        memory_leak_detected = detect_memory_leak(last_memory_usage_mb, memory_usage_history[-1])
        if memory_leak_detected:
            logging.warning(f"Memory leak detected: Memory usage increased from {last_memory_usage_mb:.2f} MB to {memory_usage_history[-1]:.2f} MB")

    last_memory_usage_mb = memory_usage_history[-1] if memory_usage_history else 0

    # Update real-time monitoring in console
    print(metrics)

    # Plot and save graphs every interval
    if len(cpu_usage_history) == history_length:
        plot_graphs()

    # Wait before the next iteration
    time.sleep(interval)
