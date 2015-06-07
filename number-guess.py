import random




class guess():

    def __init__(self):
        global end_range, initial_number, guessed
        end_range = 5000
        initial_number = int(end_range/2)
        self.banners()
        self.initiate()

    def initiate(self):
        print "initial number : %d, endrange : %d" % (initial_number, end_range)
        number = initial_number
        guessed = False
        while not guessed:
            resp = self.ask(number)
            if resp == 's':
                number = int(round(number / 2))
            elif resp == 'b':
                number = int(round(number*2))
            elif resp == 'c':
                print("[+] Correct number : %d" % number)
                guessed = True
                break

    def ask(self, number):
        print("[%s]" % number)
        print("[s]maller, [b]igger, [c]orrect!")
        

        while True:
            resp = raw_input("[~]:> ")
            if resp.lower() == 's' or resp.lower() == 'b' or resp.lower() == 'c':
                return resp
            elif resp.lower() == 'e' or resp.lower() == 'q':
                exit()
            else:
                print("Invalid input")

    def banners(self):
        print("[+] Think of a number in your mind")
        print("[+] Number range = 1~5000")
        raw_input("[+] Press enter when ready...")

if __name__ == '__main__':
    app = guess()