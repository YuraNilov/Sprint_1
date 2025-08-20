time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

for time_value in time_string.split(','):
    hours = minutes = seconds = 0
    
    for component in time_value.strip().split():
        if 'h' in component:
            hours = int(component.replace('h', ''))
        elif 'm' in component:
            minutes = int(component.replace('m', ''))
        elif 's' in component:
            seconds = int(component.replace('s', ''))
    
    total_minutes += hours * 60 + minutes + seconds // 60

print(f"Общее количество минут: {total_minutes}")