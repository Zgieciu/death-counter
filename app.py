import curses

def save_deaths(deaths):
    with open("deaths.txt", "w") as file:
        file.write(str(deaths))

def save_boss(deaths, boss_name):
    with open("bosses.txt", "a") as file:
        file.write(boss_name + ": " + str(deaths) + "\n")

def load_deaths():
    try:
        with open("deaths.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def main(stdscr):
    deaths = load_deaths()
    tmp_deaths = 0
    checkpoint = False

    curses.curs_set(0) 
    stdscr.clear()
    stdscr.addstr(f"Aktualna liczba śmierci: {deaths}\n")
    stdscr.refresh()

    while True:
        key = stdscr.getch() 
        if key == ord('a'):
            deaths += 1
            tmp_deaths += 1
            save_deaths(deaths)
        elif key == ord('r'): 
            if deaths > 0:
                deaths -= 1
                save_deaths(deaths)
            if tmp_deaths > 0:
                tmp_deaths -= 1
        elif key == ord('c'):
            tmp_deaths = 0
            checkpoint = not checkpoint
        elif key == ord('s'):
            curses.echo()
            stdscr.addstr("Podaj nazwę bossa: ")
            boss_name_bytes = stdscr.getstr()
            boss_name = boss_name_bytes.decode('utf-8')
            curses.noecho()
            save_boss(tmp_deaths, boss_name)
        elif key == ord('q'): 
            break

        stdscr.clear()
        stdscr.addstr(f"Aktualna liczba śmierci: {deaths}\n")
        if checkpoint:
            stdscr.addstr(f"Liczba śmierci od ostatniego checkpointu: {tmp_deaths}\n")
        stdscr.refresh()

curses.wrapper(main)