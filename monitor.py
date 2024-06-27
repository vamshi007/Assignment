import psutil
import time


def check_memory_usage():
    while True:
        memory_info = psutil.virtual_memory()
        memory_utilization = memory_info.percent
        if memory_utilization >= 80:
            print("Warning: You are using 80% of memory of the system")
        print(f"Memory Utilization: {memory_utilization}%")
        time.sleep(60)


if __name__ == "__main__":
    check_memory_usage()
