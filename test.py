def late(x):
    late=x[0]
    next_num=x[0] + 1 
    waiting=x[0]
    done = False
    while done == False:
        for events in x:
            if events == "take":
                late += 1
                waiting += 1 
                next_num += 1 
                if next_num > 999:
                    next_num = 1 
            elif events == "serve":
                waiting -= 1 
            elif events == "close":
                print(late, waiting,next_num)
                late = 0
            elif events == "EOF":
                done = True
        
x = [23, 'take', 'take', 'serve', 'take', 'serve', 'serve', 'close', 'take', 'take', 'take', 'serve', 'close', 'take', 'serve', 'take', 'serve', 'take', 'take', 'take', 'take', 'take', 'take', 'serve', 'close', 'EOF']
late(x)