import webbrowser


print('''

░██████╗██╗░░██╗██╗██╗░░░██╗░█████╗░██╗░░░██╗        ░░███╗░░░░░░█████╗░░░███╗░░
██╔════╝██║░░██║██║██║░░░██║██╔══██╗╚██╗░██╔╝        ░████║░░░░░██╔══██╗░████║░░
╚█████╗░███████║██║╚██╗░██╔╝███████║░╚████╔╝░        ██╔██║░░░░░██║░░██║██╔██║░░
░╚═══██╗██╔══██║██║░╚████╔╝░██╔══██║░░╚██╔╝░░        ╚═╝██║░░░░░██║░░██║╚═╝██║░░
██████╔╝██║░░██║██║░░╚██╔╝░░██║░░██║░░░██║░░░        ███████╗██╗╚█████╔╝███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░        ╚══════╝╚═╝░╚════╝░╚══════╝

░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝ 
███████╗███╗░░██╗░██████╗░██╗███╗░░██╗███████╗
██╔════╝████╗░██║██╔════╝░██║████╗░██║██╔════╝
█████╗░░██╔██╗██║██║░░██╗░██║██╔██╗██║█████╗░░
██╔══╝░░██║╚████║██║░░╚██╗██║██║╚████║██╔══╝░░
███████╗██║░╚███║╚██████╔╝██║██║░╚███║███████╗
╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝░░╚══╝╚══════╝
''')


while True:
    browser = input("Serch Browser or Type URL: ")
    webbrowser.open(browser)