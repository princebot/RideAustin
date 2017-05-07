import pandas as pd

ra=pd.read_csv('RideAustin_Weather.csv', parse_dates=['completed_on','started_on','Date']) 

#go through the ra DF, use dt.weekday to determine what weekday that entry falls over

Mondays=ra.loc[(ra['started_on'].dt.weekday==0),:]
Tuesdays=ra.loc[(ra['started_on'].dt.weekday==1),:]
Wednesdays=ra.loc[(ra['started_on'].dt.weekday==2),:]
Thursdays=ra.loc[(ra['started_on'].dt.weekday==3),:]
Fridays=ra.loc[(ra['started_on'].dt.weekday==4),:]
Saturdays=ra.loc[(ra['started_on'].dt.weekday==5),:]
Sundays=ra.loc[(ra['started_on'].dt.weekday==6),:]

#strike the date from each: this assigns all to the same date
Mondays['started_on']=Mondays['started_on'].dt.strftime('2017-05-01 %H:%M:%S')
Mondays['completed_on']=Mondays['completed_on'].dt.strftime('2017-05-01 %H:%M:%S')
Tuesdays['started_on']=Tuesdays['started_on'].dt.strftime('2017-05-02 %H:%M:%S')
Tuesdays['completed_on']=Tuesdays['completed_on'].dt.strftime('2017-05-02 %H:%M:%S')
Wednesdays['started_on']=Wednesdays['started_on'].dt.strftime('2017-05-03 %H:%M:%S')
Wednesdays['completed_on']=Wednesdays['completed_on'].dt.strftime('2017-05-03 %H:%M:%S')
Thursdays['started_on']=Thursdays['started_on'].dt.strftime('2017-05-04 %H:%M:%S')
Thursdays['completed_on']=Thursdays['completed_on'].dt.strftime('2017-05-04 %H:%M:%S')
Fridays['started_on']=Fridays['started_on'].dt.strftime('2017-05-05 %H:%M:%S')
Fridays['completed_on']=Fridays['completed_on'].dt.strftime('2017-05-05 %H:%M:%S')
Saturdays['started_on']=Saturdays['started_on'].dt.strftime('2017-05-06 %H:%M:%S')
Saturdays['completed_on']=Saturdays['completed_on'].dt.strftime('2017-05-06 %H:%M:%S')
Sundays['started_on']=Sundays['started_on'].dt.strftime('2017-05-07 %H:%M:%S')
Sundays['completed_on']=Sundays['completed_on'].dt.strftime('2017-07-05 %H:%M:%S')

#save each object as a separate csv
Mondays.to_csv('Mondays.csv')
Tuesdays.to_csv('Tuesdays.csv')
Wednesdays.to_csv('Wednesdays.csv')
Thursdays.to_csv('Thursdays.csv')
Fridays.to_csv('Fridays.csv')
Saturdays.to_csv('Saturdays.csv')
Sundays.to_csv('Sundays.csv')




#Notes: 
#for i
#dates = pd.to_datetime(pd.Series(['20010101', '20010331']), format = '%Y%m%d')
#dates.apply(lambda x: x.strftime('%Y-%m-%d'))

#ra.loc[:,'started_on']=ra['started_on'].apply(lambda x: ra.loc['started_on'].strftime('2017-05-05 %H:%M:%S'))
#Mondays.loc[:,'started_on']=Mondays.loc[:,'started_on'].apply(lambda x: ra.loc['started_on'].strftime('2017-05-05 %H:%M:%S'))


#for i in Mondays.iterrows():
#	Mondays.loc[i, 'started_on'] = Mondays.loc[i, 'started_on'].strftime('2017-05-05 %H:%M:%S')
#TypeError: 'Series' objects are mutable, thus they cannot be hashed

#for i, trial in dfTrials.iterrows():
#dfTrials.loc[i, "response"] = "answer {}".format(trial["no"])


