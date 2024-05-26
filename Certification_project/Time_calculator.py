def add_time(start, duration,day_of_week=None):
    days_of_week_index={"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
    days_of_week_array=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    #duration hours and minutes
    duration_tuple=duration.partition(":")
    duration_hours=int(duration_tuple[0])
    duration_mins=int(duration_tuple[2])
    #start_time hours and minutes
    start_time=start.partition(":")
    start_minutes_tuple=start_time[2].partition(" ")
    start_hours=int(start_time[0])
    start_mins=int(start_minutes_tuple[0])
    am_or_pm=start_minutes_tuple[2]
    am_or_pm_flip={"AM":"PM","PM":"AM"}
    
    amount_of_days=int(duration_hours/24)
    
    end_minutes=duration_mins+start_mins
    if end_minutes>=60:
        start_hours+=1
        end_minutes=end_minutes%60
    am_and_pm_flips=int((start_hours+duration_hours)/12)
    end_hours=(duration_hours+start_hours)%12
    
    end_minutes=end_minutes if end_minutes>9 else "0" + str(end_minutes)
    end_hours=end_hours=12 if end_hours==0 else end_hours
    
    if am_or_pm=="PM" and start_hours+(duration_hours%12)>=12:
        amount_of_days+=1
    
    am_or_pm=am_or_pm_flip[am_or_pm] if am_and_pm_flips%2==1 else am_or_pm
    
    returnTime=str(end_hours)+":"+str(end_minutes)+" "+am_or_pm
    if day_of_week:
        day_of_week=day_of_week.lower()
        index=int(days_of_week_index[day_of_week]+amount_of_days)%7
        new_day=days_of_week_array[index]
        returnTime+=", "+new_day
    if amount_of_days==1:
        return returnTime+" "+"(next day)"
    elif amount_of_days>1:
        return returnTime+" ("+str(amount_of_days)+" days later)"

    return returnTime
