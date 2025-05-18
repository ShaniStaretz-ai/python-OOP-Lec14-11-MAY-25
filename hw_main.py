from timer import Timer

if __name__ == '__main__':
    t1 = Timer("shani's timer", 60)
    t1.pause = False
    del t1.pause
    t2 = Timer("shani's timer2", 60)
    timers_list: list[Timer] = [t1, t2]
    print(timers_list)

    t = Timer("Workout", 0.1)
    t_clone = eval(repr(t))
    t.run()
    print("time passed:",t.time_passed())
    print("Same name:", t.name == t_clone.name)
    print("Same duration:", t.duration == t_clone.duration)
