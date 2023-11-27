def add(stops, idx, string):
    if 0 <= idx < len(stops):
        return stops[:idx] + string + stops[idx:]
    return stops

def remove(stops, start, end):
    if 0 <= start <= end < len(stops):
        return stops[:start] + stops[end + 1:]
    return stops

def switch(stops, old_string, new_string):
    if old_string in stops:
        return stops.replace(old_string, new_string)
    return stops

def main():
    stops = input()
    input_line = input().split(':')
    while input_line[0] != 'Travel':
        command = input_line[0]
        if command == 'Add Stop':
            idx, string = int(input_line[1]), input_line[2]
            stops = add(stops, idx, string)
        elif command == 'Remove Stop':
            start, end = int(input_line[1]), int(input_line[2])
            stops = remove(stops, start, end)
        elif command == 'Switch':
            old_string, new_string = input_line[1], input_line[2]
            stops = switch(stops, old_string, new_string)
        print(stops)
        input_line = input().split(':')

    print(f"Ready for world tour! Planned stops: {stops}")

if __name__ == '__main__':
    main()
