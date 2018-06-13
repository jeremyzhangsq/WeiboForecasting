import pandas as pd
import random
path = "weibo_train_data.txt"

def df_gen(path):
    with open(path, 'rb') as f:
        content = f.read()

    content = content.decode('utf-8')
    lines = content.split('\n')
    info = {"uid":[],"mid":[],"time":[],"forward_count":[],"comment_count":[],"like_count":[],"content":[],}
    cnt = 0
    for index, line in enumerate(lines):
        try:
            uid, mid, time, forward_count, comment_count, like_count, content = line.split('\t')
        except:
            print('skiped {}'.format(index))
            cnt+=1
            continue

        info["uid"].append(uid)
        info["mid"].append(mid)
        info['time'].append(time)
        info['forward_count'].append(forward_count)
        info['comment_count'].append(comment_count)
        info['like_count'].append(like_count)
        info['content'].append(content)


    df = pd.DataFrame(info)
    print('skipped count: {}'.format(cnt))
    return df

if __name__ == "__main__":
    df = df_gen(path)
    print(df.head())