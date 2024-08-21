import psutil
import time
import logging
from ctypes import windll, wintypes

# Configuration
process_name = "analytic_server.exe"
log_file = "process_metrics_log.txt"
memory_threshold = 0.95  # 95% of total physical memory
duration = 180  # Duration to monitor in seconds
pause_after_action = 10800  # 3 hours in seconds

# Set up logging
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def get_processes_by_name(name):
    """Get a list of processes with the given name."""
    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        if proc.info['name'] == name:
            process_list.append(proc)
    return process_list

def terminate_process(proc):
    """Terminate the given process."""
    try:
        proc.terminate()
        proc.wait(timeout=5)
        logging.info(f"Process {proc.pid} terminated successfully.")
    except psutil.TimeoutExpired:
        proc.kill()
        logging.info(f"Process {proc.pid} killed after termination timeout.")
    except psutil.NoSuchProcess:
        logging.warning(f"Process {proc.pid} no longer exists.")
    except psutil.AccessDenied:
        logging.error(f"Access denied when trying to terminate process {proc.pid}.")

def monitor_processes():
    """Monitor and manage processes based on memory usage."""
    high_memory_flag = False

    while True:
        if high_memory_flag:
            logging.info("Pausing monitoring for 3 hours after taking action.")
            time.sleep(pause_after_action)
            high_memory_flag = False
            logging.info("Resuming monitoring...")

        processes = get_processes_by_name(process_name)

        if processes:
            for proc in processes:
                try:
                    memory_usage = proc.memory_info().rss / windll.kernel32.GetPhysicallyInstalledSystemMemory(0)
                    
                    if memory_usage >= memory_threshold:
                        if not high_memory_flag:
                            logging.warning(f"High memory usage detected for PID {proc.pid}: {memory_usage*100:.2f}%")
                            high_memory_flag = True

                        time.sleep(duration)

                        processes = get_processes_by_name(process_name)
                        for proc in processes:
                            memory_usage = proc.memory_info().rss / windll.kernel32.GetPhysicallyInstalledSystemMemory(0)
                            if memory_usage >= memory_threshold:
                                logging.warning(f"Memory usage still high after {duration} seconds for PID {proc.pid}. Terminating process...")
                                terminate_process(proc)

                                while not get_processes_by_name(process_name):
                                    time.sleep(1)

                                logging.info(f"Process {process_name} started again with PID {proc.pid}.")
                            else:
                                logging.info(f"Memory usage normalized for PID {proc.pid}. No action taken.")
                                high_memory_flag = False

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    logging.warning(f"Error accessing process {proc.pid}.")
        else:
            logging.info(f"Process {process_name} not found.")

        time.sleep(60)

if __name__ == "__main__":
    monitor_processes()
