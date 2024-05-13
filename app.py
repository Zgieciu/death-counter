import curses

def save_deaths(deaths):
    with open("deaths.txt", "w") as file:
        file.write(str(deaths))

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
                tmp_deaths -= 1
                save_deaths(deaths)
        elif key == ord('c'):
            tmp_deaths = 0
            checkpoint = not checkpoint
        elif key == ord('q'):
            break

        stdscr.clear()
        stdscr.addstr(f"Aktualna liczba śmierci: {deaths}\n")
        if checkpoint:
            stdscr.addstr(f"Liczba śmierci od ostatniego checkpointu: {tmp_deaths}\n")
        stdscr.refresh()

curses.wrapper(main)