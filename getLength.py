import subprocess, os
from datetime import timedelta

total_sec = 0
overall_total = 0
video_ext = ('mkv','mp4', 'm4a', 'm4v', 'f4v', 'f4a', 
            'm4b', 'm4r', 'f4b', 'mov','avi', 'wmv')
files_list = []
parent = os.path.abspath('.')

def get_length(filename):
    result = subprocess.run(["./ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True)
    try:
        result = float(result.stdout)
        global total_sec,overall_total
        total_sec = total_sec + result
        overall_total = overall_total + result
        return '{}\t{}'.format(str(timedelta(seconds=result))[:-7],filename)
    except:
        return '{}\t{}'.format('NaN',filename)
old_pwd = ''    
for pwd, dirs , files in os.walk(os.path.abspath('.')):
    for f in files:
        if f.endswith(video_ext):
            old_pwd = pwd
            print(get_length(os.path.join(parent,pwd,f)))
    if old_pwd == pwd:
        print('Total Duration: ' + str(timedelta(seconds=total_sec))[:-7],end='\n\n')
        total_sec = 0
               

print('\nOverall Total Duration: ' + str(timedelta(seconds=overall_total))[:-7],end='\n')