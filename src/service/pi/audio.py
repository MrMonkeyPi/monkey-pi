# aplay -Dhw:1,0 /usr/share/sounds/alsa/Rear_Center.wav
# set volume
# alsamixer

import time
import os
import subprocess
import threading

is_in_pi = os.environ.get('IN_PI') is not None


def find_rsc_file(name, rscDirs):
    for dir in rscDirs:
        if not os.path.exists(dir):
            continue
        for path, sub_dirs, files in os.walk(dir):
            for file_name in files:
                if file_name.startswith(name+'.'):
                    return os.path.join(path, file_name)
    return None


def has_cn(words):
    for ch in words:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def sing_off_work(file_path):
    for _ in range(5):
        os.system('aplay ' + file_path)
        time.sleep(2)


def call_espeak(words):
    cmds = ['espeak', '"'+words+'"', '-p 65']

    if has_cn(words):
        cmds.append('-v zh -s 180')
    else:
        cmds.append('-s 160')

    cmds.append('--stdout | aplay')
    os.system(' '.join(cmds))


def sing(name, rscDirs):
    file_path = find_rsc_file(name, rscDirs)
    if file_path is None:
        return

    print(file_path)

    # spefial logic for sing off work
    if name == 'OffWork':
        threading.Thread(target=sing_off_work, args=[file_path]).start()
    else:
        subprocess.Popen(['aplay', file_path])


def say(words):
    threading.Thread(target=call_espeak, args=[words]).start()
    # cmds = ['espeak', words, '-p 65']

    # if has_cn(words):
    #     cmds.append('-v')
    #     cmds.append('zh')
    #     cmds.append('-s 180')
    # else:
    #     cmds.append(' -s 160 ')

    # cmds.append(' --stdout | aplay')
    # # if is_in_pi:
    # #     cmds.append(' --stdout | aplay')

    # # print(words)
    # subprocess.Popen(cmds)
