def late(x):
    late=x[0]
    next_num=0
    waiting=0
    done = False
    while done == False:
        for events in x:
            if events == "take":
                late += 1
                waiting = late
            elif events == "serve":
                waiting -= 1
            elif events == "close":
                next_num = late + 1
                if next_num == 1000:
                    next_num = 1
                print(late,waiting,next_num)
                late = waiting
            elif events == "EOF":
                done = True
        
x = [23, 'take', 'take', 'serve', 'take', 'serve', 'serve', 'close', 'take', 'take', 'take', 'serve', 'close', 'take', 'serve', 'take', 'serve', 'take', 'take', 'take', 'take', 'take', 'take', 'serve', 'close', 'EOF']
late(x)