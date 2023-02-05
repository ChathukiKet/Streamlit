import current_short_id

def increment_short_id(current_id, max_id): 
    if current_id == max_id:
        short_id = 0
    else:
        short_id = current_id + 1

    return short_id


def main():
    current_id = current_short_id.current_short_id
    short_id = increment_short_id(current_id, 9)
    return short_id
    

if __name__ == '__main__':
    main()



