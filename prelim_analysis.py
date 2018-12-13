# Jake Son
# Child Mind Institute

import numpy as np
import pandas as pd

def create_brt(trial1_file, trial2_file):

    df = pd.read_csv(trial1_file)

    results = {'participant': [], 'trial': [], 'hand': [], 'n_correct': [], 'n_incorrect': [],
               'avg_correct_time': [], 'avg_incorrect_time': []}

    for part in df.participant_id.unique():

        sub = df[df.participant_id == part]

        for hand in ['Left', 'Right']:

            values = dict(sub[sub.condition == hand]['correct_button'].value_counts())

            num_c = values[1]
            num_i = values[0]

            results['participant'].append(part[-3:])
            results['trial'].append('1')
            results['hand'].append(hand)
            results['n_correct'].append(num_c)
            results['n_incorrect'].append(num_i)

            sub_hand = sub[sub.condition == hand]

            avg_c_time = np.average(sub_hand[sub_hand.correct_button == 1].response_time.tolist())
            avg_i_time = np.average(sub_hand[sub_hand.correct_button == 0].response_time.tolist())

            results['avg_correct_time'].append(avg_c_time)
            results['avg_incorrect_time'].append(avg_i_time)

    df = pd.read_csv(trial2_file)

    for part in df.participant_id.unique():

        sub = df[df.participant_id == part]

        for hand in ['Left', 'Right']:

            values = dict(sub[df.condition == hand]['correct_button'].value_counts())

            num_c = values[1]
            num_i = values[0]

            results['participant'].append(part[-3:])
            results['trial'].append('2')
            results['hand'].append(hand)
            results['n_correct'].append(num_c)
            results['n_incorrect'].append(num_i)

            sub_hand = sub[sub.condition == hand]

            avg_c_time = np.average(sub_hand[sub_hand.correct_button == 1].response_time.tolist())
            avg_i_time = np.average(sub_hand[sub_hand.correct_button == 0].response_time.tolist())

            results['avg_correct_time'].append(avg_c_time)
            results['avg_incorrect_time'].append(avg_i_time)

    out_df = pd.DataFrame.from_dict(results)

    return out_df

trial1_brt_file = './ACE/ACE_EXPORT_BRT_BK.csv'
trial2_brt_file = './ACE/ACE_EXPORT_BRT_BS.csv'

df = create_brt(trial1_brt_file, trial2_brt_file)

for part in df.participant.unique():

    for hand in ['Left', 'Right']:

        try:

            sub = df[(df.participant == part) & (df.hand == hand)]

            d_correct = int(sub[sub.trial == '2'].n_correct) - int(sub[sub.trial == '1'].n_correct)
            d_incorrect = int(sub[sub.trial == '2'].n_incorrect) - int(sub[sub.trial == '1'].n_incorrect)

            d_time_correct = float(sub[sub.trial == '2'].avg_correct_time) - float(sub[sub.trial == '1'].avg_correct_time)

            print(part, hand, d_correct, d_time_correct)

        except:

            continue