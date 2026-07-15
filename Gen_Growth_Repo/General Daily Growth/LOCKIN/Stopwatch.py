import time
def stop_watch():
    start_time = time.time()
    try:
        while True:
            current_time = time.time()
            seconds = int((current_time-start_time)%60)
            minutes = (int((current_time-start_time)/60))%60
            hours = (int((current_time-start_time)/3600))%60
            print(f'{hours:02}:{minutes:02}:{seconds:02}')
            time.sleep(1)
    except KeyboardInterrupt:
        end_time = time.time()
        final_time = int(end_time - start_time)
        return final_time
overtime = stop_watch()
print(overtime)
    