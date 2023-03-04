import tkinter as tk
import tkinter.ttk as ttk
from threading import Thread
import pygame
import os
from sys import platform
import json
from time import sleep
import random
data = {}

if platform == 'win32':
    datajson = '\\data.json'
else:
    datajson = '/data.json'        

with open(f"{os.getcwd()}{datajson}") as file:
    data = json.load(file)

class UiApp:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=512, padx=5, pady=5, width=720)
        toplevel1.geometry("640x480")
        toplevel1.maxsize(768, 576)
        toplevel1.minsize(768, 576)
        self.top_frame = ttk.Frame(toplevel1)
        self.top_frame.configure(height=200)
        self.coalLabel = ttk.Label(self.top_frame)
        self.coalLabel.configure(relief="flat", state="normal", text='Coal: ')
        self.coalLabel.grid(column=0, row=0, sticky="w")
        self.coalNum = ttk.Label(self.top_frame)
        self.coal = tk.IntVar()
        self.coalNum.configure(textvariable=self.coal)
        self.coalNum.grid(column=1, row=0)
        self.tinLabel = ttk.Label(self.top_frame)
        self.tinLabel.configure(text='Tin:')
        self.tinLabel.grid(column=0, ipadx=5, row=1, sticky="w")
        self.tinNum = ttk.Label(self.top_frame)
        self.tin = tk.IntVar(value=0)
        self.tinNum.configure(text='0', textvariable=self.tin)
        self.tinNum.grid(column=1, row=1)
        self.ironLabel = ttk.Label(self.top_frame)
        self.ironLabel.configure(text='Iron: ')
        self.ironLabel.grid(column=0, row=2, sticky="w")
        self.ironNum = ttk.Label(self.top_frame)
        self.iron = tk.IntVar(value=0)
        self.ironNum.configure(text='0', textvariable=self.iron)
        self.ironNum.grid(column=1, row=2)
        self.tungstenLabel = ttk.Label(self.top_frame)
        self.tungstenLabel.configure(text='Tungsten: ')
        self.tungstenLabel.grid(column=0, row=3, sticky="w")
        self.tungstenNum = ttk.Label(self.top_frame)
        self.tungsten = tk.IntVar(value=0)
        self.tungstenNum.configure(text='0', textvariable=self.tungsten)
        self.tungstenNum.grid(column=1, row=3)
        self.goldLabel = ttk.Label(self.top_frame)
        self.goldLabel.configure(text='Gold: ')
        self.goldLabel.grid(column=0, row=4, sticky="w")
        self.goldNum = ttk.Label(self.top_frame)
        self.gold = tk.IntVar(value=0)
        self.goldNum.configure(text='0', textvariable=self.gold)
        self.goldNum.grid(column=1, row=4)
        self.platinumLabel = ttk.Label(self.top_frame)
        self.platinumLabel.configure(text='Platinum: ')
        self.platinumLabel.grid(column=0, row=5, sticky="w")
        self.platinumNum = ttk.Label(self.top_frame)
        self.platinum = tk.IntVar(value=0)
        self.platinumNum.configure(text='0', textvariable=self.platinum)
        self.platinumNum.grid(column=1, row=5)
        self.diamondLabel = ttk.Label(self.top_frame)
        self.diamondLabel.configure(text='Diamond: ')
        self.diamondLabel.grid(column=0, row=6, sticky="w")
        self.diamondNum = ttk.Label(self.top_frame)
        self.diamond = tk.IntVar(value=0)
        self.diamondNum.configure(text='0', textvariable=self.diamond)
        self.diamondNum.grid(column=1, row=6)
        self.emeraldLabel = ttk.Label(self.top_frame)
        self.emeraldLabel.configure(text='Emerald: ')
        self.emeraldLabel.grid(column=0, row=7, sticky="w")
        self.emeraldNum = ttk.Label(self.top_frame)
        self.emerald = tk.IntVar(value=0)
        self.emeraldNum.configure(text='0', textvariable=self.emerald)
        self.emeraldNum.grid(column=1, row=7)
        self.rubyLabel = ttk.Label(self.top_frame)
        self.rubyLabel.configure(text='Ruby: ')
        self.rubyLabel.grid(column=0, row=8, sticky="w")
        self.rubyNum = ttk.Label(self.top_frame)
        self.ruby = tk.IntVar(value=0)
        self.rubyNum.configure(text='0', textvariable=self.ruby)
        self.rubyNum.grid(column=1, row=8)
        self.mythrilLabel = ttk.Label(self.top_frame)
        self.mythrilLabel.configure(text='Mythril: ')
        self.mythrilLabel.grid(column=0, row=9, sticky="w")
        self.mythrilNum = ttk.Label(self.top_frame)
        self.mythril = tk.IntVar(value=0)
        self.mythrilNum.configure(text='0', textvariable=self.mythril)
        self.mythrilNum.grid(column=1, row=9)
        self.adamantiteLabel = ttk.Label(self.top_frame)
        self.adamantiteLabel.configure(text='Adamantite: ')
        self.adamantiteLabel.grid(column=0, row=10, sticky="w")
        self.adamantiteNum = ttk.Label(self.top_frame)
        self.adamantite = tk.IntVar(value=0)
        self.adamantiteNum.configure(text='0', textvariable=self.adamantite)
        self.adamantiteNum.grid(column=1, row=10)
        self.orichalcumLabel = ttk.Label(self.top_frame)
        self.orichalcumLabel.configure(text='Orichalcum: ')
        self.orichalcumLabel.grid(column=0, row=11, sticky="w")
        self.orichalcumNum = ttk.Label(self.top_frame)
        self.orichalcum = tk.IntVar(value=0)
        self.orichalcumNum.configure(text='0', textvariable=self.orichalcum)
        self.orichalcumNum.grid(column=1, row=11)
        self.lanthanumLabel = ttk.Label(self.top_frame)
        self.lanthanumLabel.configure(text='Lanthanum: ')
        self.lanthanumLabel.grid(column=0, row=12, sticky="w")
        self.lanthanumNum = ttk.Label(self.top_frame)
        self.lanthanum = tk.IntVar(value=0)
        self.lanthanumNum.configure(text='0', textvariable=self.lanthanum)
        self.lanthanumNum.grid(column=1, row=12)
        self.ceriumLabel = ttk.Label(self.top_frame)
        self.ceriumLabel.configure(text='Cerium: ')
        self.ceriumLabel.grid(column=0, row=13, sticky="w")
        self.ceriumNum = ttk.Label(self.top_frame)
        self.cerium = tk.IntVar(value=0)
        self.ceriumNum.configure(text='0', textvariable=self.cerium)
        self.ceriumNum.grid(column=1, row=13)
        self.praseodymiumLabel = ttk.Label(self.top_frame)
        self.praseodymiumLabel.configure(text='Praseodymium:')
        self.praseodymiumLabel.grid(column=0, row=14, sticky="w")
        self.praseodymiumNum = ttk.Label(self.top_frame)
        self.praseodymium = tk.IntVar(value=0)
        self.praseodymiumNum.configure(
            text='0', textvariable=self.praseodymium)
        self.praseodymiumNum.grid(column=1, row=14)
        self.promethiumLabel = ttk.Label(self.top_frame)
        self.promethiumLabel.configure(text='Promethium: ')
        self.promethiumLabel.grid(column=0, row=15, sticky="w")
        self.promethiumNum = ttk.Label(self.top_frame)
        self.promethium = tk.IntVar(value=0)
        self.promethiumNum.configure(text='0', textvariable=self.promethium)
        self.promethiumNum.grid(column=1, row=15)
        self.europiumLabel = ttk.Label(self.top_frame)
        self.europiumLabel.configure(text='Europium: ')
        self.europiumLabel.grid(column=0, row=16, sticky="w")
        self.europiumNum = ttk.Label(self.top_frame)
        self.europium = tk.IntVar(value=0)
        self.europiumNum.configure(text='0', textvariable=self.europium)
        self.europiumNum.grid(column=1, row=16)
        self.hafniumLabel = ttk.Label(self.top_frame)
        self.hafniumLabel.configure(text='Hafnium: ')
        self.hafniumLabel.grid(column=0, row=17, sticky="w")
        self.hafniumNum = ttk.Label(self.top_frame)
        self.hafnium = tk.IntVar(value=0)
        self.hafniumNum.configure(text='0', textvariable=self.hafnium)
        self.hafniumNum.grid(column=1, row=17)
        self.osmiumLabel = ttk.Label(self.top_frame)
        self.osmiumLabel.configure(text='Osmium: ')
        self.osmiumLabel.grid(column=0, row=18, sticky="w")
        self.osmiumNum = ttk.Label(self.top_frame)
        self.osmium = tk.IntVar(value=0)
        self.osmiumNum.configure(text='0', textvariable=self.osmium)
        self.osmiumNum.grid(column=1, row=18)
        self.bismuthLabel = ttk.Label(self.top_frame)
        self.bismuthLabel.configure(text='Bismuth: ')
        self.bismuthLabel.grid(column=0, row=19, sticky="w")
        self.bismuthNum = ttk.Label(self.top_frame)
        self.bismuth = tk.IntVar(value=0)
        self.bismuthNum.configure(text='0', textvariable=self.bismuth)
        self.bismuthNum.grid(column=1, row=19)
        self.franciumLabel = ttk.Label(self.top_frame)
        self.franciumLabel.configure(text='Francium: ')
        self.franciumLabel.grid(column=0, row=20, sticky="w")
        self.franciumNum = ttk.Label(self.top_frame)
        self.francium = tk.IntVar(value=0)
        self.franciumNum.configure(text='0', textvariable=self.francium)
        self.franciumNum.grid(column=1, row=20)
        self.neptuniumLabel = ttk.Label(self.top_frame)
        self.neptuniumLabel.configure(text='Neptunium: ')
        self.neptuniumLabel.grid(column=0, row=21, sticky="w")
        self.neptuniumNum = ttk.Label(self.top_frame)
        self.neptunium = tk.IntVar(value=0)
        self.neptuniumNum.configure(text='0', textvariable=self.neptunium)
        self.neptuniumNum.grid(column=1, row=21)
        self.californiumLabel = ttk.Label(self.top_frame)
        self.californiumLabel.configure(text='Californium: ')
        self.californiumLabel.grid(column=0, row=22, sticky="w")
        self.californiumNum = ttk.Label(self.top_frame)
        self.californium = tk.IntVar(value=0)
        self.californiumNum.configure(text='0', textvariable=self.californium)
        self.californiumNum.grid(column=1, row=22)
        self.einsteiniumLabel = ttk.Label(self.top_frame)
        self.einsteiniumLabel.configure(text='Einsteinium: ')
        self.einsteiniumLabel.grid(column=0, row=23, sticky="w")
        self.einsteiniumNum = ttk.Label(self.top_frame)
        self.einsteinium = tk.IntVar(value=0)
        self.einsteiniumNum.configure(text='0', textvariable=self.einsteinium)
        self.einsteiniumNum.grid(column=1, row=23)
        self.astatineLabel = ttk.Label(self.top_frame)
        self.astatineLabel.configure(text='Astatine: ')
        self.astatineLabel.grid(column=0, row=24, sticky="w")
        self.astatineNum = ttk.Label(self.top_frame)
        self.astatine = tk.IntVar(value=0)
        self.astatineNum.configure(text='0', textvariable=self.astatine)
        self.astatineNum.grid(column=1, row=24)
        self.tennessineLabel = ttk.Label(self.top_frame)
        self.tennessineLabel.configure(text='Tennessine: ')
        self.tennessineLabel.grid(column=0, row=25, sticky="w")
        self.tennessineNum = ttk.Label(self.top_frame)
        self.tennessine = tk.IntVar(value=0)
        self.tennessineNum.configure(text='0', textvariable=self.tennessine)
        self.tennessineNum.grid(column=1, row=25)
        self.soakiteLabel = ttk.Label(self.top_frame)
        self.soakiteLabel.configure(text='Soakite: ')
        self.soakiteLabel.grid(column=0, row=26, sticky="w")
        self.soakiteNum = ttk.Label(self.top_frame)
        self.soakite = tk.IntVar(value=0)
        self.soakiteNum.configure(text='0', textvariable=self.soakite)
        self.soakiteNum.grid(column=1, row=26)
        self.invisLabelR = ttk.Label(self.top_frame)
        self.invisLabelR.grid(column=0, row=27)
        self.dabloonsLabel = ttk.Label(self.top_frame)
        self.dabloonsLabel.configure(text='Dabloons: ')
        self.dabloonsLabel.grid(column=0, row=28, sticky="w")
        self.dabloonsNum = ttk.Label(self.top_frame)
        self.dabloons = tk.IntVar(value=0)
        self.dabloonsNum.configure(text='0', textvariable=self.dabloons)
        self.dabloonsNum.grid(column=1, row=28)
        self.top_frame.grid(column=0, row=0)
        separator2 = ttk.Separator(toplevel1)
        separator2.configure(orient="vertical")
        separator2.grid(column=1, padx=10, row=0, sticky="ns")
        frame2 = ttk.Frame(toplevel1)
        frame2.configure(height=460, width=90)
        self.sellButton = ttk.Button(frame2)
        self.sellButton.configure(text='SELL ALL')
        self.sellButton.grid(column=0, row=0)
        self.sellButton.configure(command=self.sell)
        self.invisLabel = ttk.Label(frame2)
        self.invisLabel.configure(relief="flat")
        self.invisLabel.grid(column=0, pady=190, row=1)
        self.oreFoundLabel = ttk.Label(frame2)
        self.oreFound = tk.StringVar(value='Coal Found!')
        self.oreFoundLabel.configure(
            text='Coal Found!',
            textvariable=self.oreFound)
        self.oreFoundLabel.grid(column=0, row=3)
        separator4 = ttk.Separator(frame2)
        separator4.configure(orient="horizontal")
        separator4.grid(column=0, row=2, sticky="ew")
        separator5 = ttk.Separator(frame2)
        separator5.configure(orient="horizontal")
        separator5.grid(column=0, row=4, sticky="ew")
        frame2.grid(column=2, row=0)
        frame2.grid_propagate(0)
        separator6 = ttk.Separator(toplevel1)
        separator6.configure(orient="vertical")
        separator6.grid(column=3, padx=10, row=0, sticky="ns")
        frame4 = ttk.Frame(toplevel1)
        frame4.configure(height=460, width=250)
        self.musicOnButton = ttk.Radiobutton(frame4)
        self.musicOn = tk.StringVar(value='1')
        self.musicOnButton.configure(
            text='Music On', value=1, variable=self.musicOn)
        self.musicOnButton.grid(column=0, row=0, sticky="w")
        self.musicOnButton.configure(command=self.musicVolume)
        self.musicOffButton = ttk.Radiobutton(frame4)
        self.musicOffButton.configure(
            text='Music Off', value=0, variable=self.musicOn)
        self.musicOffButton.grid(column=0, row=1, sticky="w")
        self.musicOffButton.configure(command=self.musicVolume)
        self.invisLabel2 = ttk.Label(frame4)
        self.invisLabel2.grid(column=0, pady=170, row=2)
        self.pickaxeUpgradeButton = ttk.Button(frame4)
        self.pickaxeUpgradeButton.configure(text='Upgrade Pickaxe Level')
        self.pickaxeUpgradeButton.grid(column=0, row=3)
        self.pickaxeUpgradeButton.configure(command=self.upgradePickaxeLevel)
        self.pickaxeSpeedButton = ttk.Button(frame4)
        self.pickaxeSpeedButton.configure(text='Upgrade Pickaxe Speed')
        self.pickaxeSpeedButton.grid(column=0, row=4)
        self.pickaxeSpeedButton.configure(command=self.upgradePickaxeSpeed)
        self.costLabel1 = ttk.Label(frame4)
        self.costLabel1.configure(text='Cost:')
        self.costLabel1.grid(column=1, row=3)
        self.costNum1 = ttk.Label(frame4)
        self.upgradeCost = tk.IntVar(value=0)
        self.costNum1.configure(text='0 ', textvariable=self.upgradeCost)
        self.costNum1.grid(column=2, row=3)
        self.costLabel2 = ttk.Label(frame4)
        self.costLabel2.configure(state="normal", text='Cost: ')
        self.costLabel2.grid(column=1, row=4)
        self.costNum2 = ttk.Label(frame4)
        self.speedCost = tk.IntVar(value=0)
        self.costNum2.configure(text='0', textvariable=self.speedCost)
        self.costNum2.grid(column=2, row=4)
        self.fovSlider = ttk.LabeledScale(frame4, from_=12, to=4435)
        self.fovSlider.grid(column=0, pady=160, row=2)
        self.fovLabel = ttk.Label(frame4)
        self.fovLabel.configure(font="{MV Boli} 20 {}", text='FOV')
        self.fovLabel.grid(column=1, row=2)
        frame4.grid(column=4, row=0)
        frame4.grid_propagate(0)
        separator3 = ttk.Separator(toplevel1)
        separator3.configure(orient="vertical")
        separator3.grid(column=5, padx=15, row=0, sticky="ns")
        label12 = ttk.Label(toplevel1)
        label12.configure(font="{Comic Sans MS} 20 {}", text='IDLEMINER')
        label12.grid(column=6, row=0, sticky="n")
        self.invisLabel4 = ttk.Label(toplevel1)
        self.invisLabel4.configure(font="{Corbel} 8 {}", text='V1.1!')
        self.invisLabel4.grid(column=6, row=0)
      
        self.coal.set(data['coal'])
        self.tin.set(data['tin'])
        self.iron.set(data['iron'])
        self.tungsten.set(data['tungsten'])
        self.gold.set(data['gold'])
        self.platinum.set(data['platinum'])
        self.diamond.set(data['diamond'])
        self.emerald.set(data['emerald'])
        self.ruby.set(data['ruby'])
        self.mythril.set(data['mythril'])
        self.adamantite.set(data['adamantite'])
        self.orichalcum.set(data['orichalcum'])
        self.lanthanum.set(data['lanthanum'])
        self.cerium.set(data['cerium'])
        self.praseodymium.set(data['praseodymium'])
        self.promethium.set(data['promethium'])
        self.europium.set(data['europium'])
        self.hafnium.set(data['hafnium'])
        self.osmium.set(data['osmium'])
        self.bismuth.set(data['bismuth'])
        self.francium.set(data['francium'])
        self.neptunium.set(data['neptunium'])
        self.californium.set(data['californium'])
        self.einsteinium.set(data['einsteinium'])
        self.astatine.set(data['astatine'])
        self.tennessine.set(data['tennessine'])
        self.soakite.set(data['soakite'])
        self.dabloons.set(data['dabloons'])
        
        self.upgradeCost.set(data['pickaxeLevelCost'])
        self.speedCost.set(data['pickaxeSpeedCost'])
        
        self.musicOn.set(0)

        # Main widget
        self.mainwindow = toplevel1
        
        toplevel1.title("IDLEMINER   V1.1")


    def run(self):
        
        Thread(target=self.logic).start()
        
        self.mainwindow.mainloop()


    def sell(self):
        
        data['dabloons'] += (data['coal'] * 1)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['tin'] * 2)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['iron'] * 3)
        self.dabloons.set(data['dabloons'])
        
        data['dabloons'] += (data['tungsten'] * 7)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['gold'] * 10)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['platinum'] * 15)
        self.dabloons.set(data['dabloons'])
        
        data['dabloons'] += (data['diamond'] * 35)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['emerald'] * 40)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['ruby'] * 50)
        self.dabloons.set(data['dabloons'])
        
        data['dabloons'] += (data['mythril'] * 110)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['adamantite'] * 125)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['orichalcum'] * 140)
        self.dabloons.set(data['dabloons'])
        
        data['dabloons'] += (data['lanthanum'] * 300)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['cerium'] * 360)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['praseodymium'] * 450)
        self.dabloons.set(data['dabloons'])
        
        data['dabloons'] += (data['promethium'] * 1000)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['europium'] * 1500)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['hafnium'] * 2250)
        self.dabloons.set(data['dabloons'])
        
        data['dabloons'] += (data['osmium'] * 6000)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['bismuth'] * 7000)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['francium'] * 9000)
        self.dabloons.set(data['dabloons'])
        
        data['dabloons'] += (data['neptunium'] * 25000)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['californium'] * 40000)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['einsteinium'] * 60000)
        self.dabloons.set(data['dabloons'])
        
        data['dabloons'] += (data['astatine'] * 200000)
        self.dabloons.set(data['dabloons'])
        data['dabloons'] += (data['tennessine'] * 500000)
        self.dabloons.set(data['dabloons'])
        
        
        data['coal'] = 0
        data['tin'] = 0
        data['iron'] = 0
        data['tungsten'] = 0
        data['gold'] = 0
        data['platinum'] = 0
        data['diamond'] = 0
        data['emerald'] = 0
        data['ruby'] = 0
        data['mythril'] = 0
        data['adamantite'] = 0
        data['orichalcum'] = 0
        data['lanthanum'] = 0
        data['cerium'] = 0
        data['praseodymium'] = 0
        data['promethium'] = 0
        data['europium'] = 0
        data['hafnium'] = 0
        data['osmium'] = 0
        data['bismuth'] = 0
        data['francium'] = 0
        data['neptunium'] = 0
        data['californium'] = 0
        data['einsteinium'] = 0
        data['astatine'] = 0
        data['tennessine'] = 0
        
        self.coal.set(data['coal'])
        self.tin.set(data['tin'])
        self.iron.set(data['iron'])
        self.tungsten.set(data['tungsten'])
        self.gold.set(data['gold'])
        self.platinum.set(data['platinum'])
        self.diamond.set(data['diamond'])
        self.emerald.set(data['emerald'])
        self.ruby.set(data['ruby'])
        self.mythril.set(data['mythril'])
        self.adamantite.set(data['adamantite'])
        self.orichalcum.set(data['orichalcum'])
        self.lanthanum.set(data['lanthanum'])
        self.cerium.set(data['cerium'])
        self.praseodymium.set(data['praseodymium'])
        self.promethium.set(data['promethium'])
        self.europium.set(data['europium'])
        self.hafnium.set(data['hafnium'])
        self.osmium.set(data['osmium'])
        self.bismuth.set(data['bismuth'])
        self.francium.set(data['francium'])
        self.neptunium.set(data['neptunium'])
        self.californium.set(data['californium'])
        self.einsteinium.set(data['einsteinium'])
        self.astatine.set(data['astatine'])
        self.tennessine.set(data['tennessine'])
        
        with open(f"{os.getcwd()}{datajson}", "w") as file:
            json.dump(data, file, indent=4) 


    def musicVolume(self):
        
        isPlaying = False
        
        if isPlaying == False:
            
            filename = f"{os.getcwd()}\\Ophanim.mp3"
            
            pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 2**12) 
            channel1 = pygame.mixer.Channel(0)
            
            sound = pygame.mixer.Sound(filename)
            channel1.play(sound, loops = -1)
            
            isPlaying = True
        
        channel1.set_volume(int(self.musicOn.get()) / 2)
          
            
    def logic(self):
        
        while True:
        
            match data['pickaxeSpeed']:
                
                case 0:
                    sleep(3)
                case 1:
                    sleep(2.66)
                case 2:
                    sleep(2.33)
                case 3:
                    sleep(2)
                case 4:
                    sleep(1.66)
                case 5:
                    sleep(1.33)
                case 6:
                    sleep(1)
                case 7:
                    sleep(0.66)
                case 8:
                    sleep(0.33)
            
            
            num = random.randint(1, 1000000)
            
            match data['pickaxeLevel']:
                
                case 0:
                    
                    match num:
                        case num if num <= 400000:
                            data['coal'] += 1
                            self.coal.set(data['coal'])
                            self.oreFound.set("Coal Found!")
                        case num if num > 400000 and num <= 750000:
                            data['tin'] += 1
                            self.tin.set(data['tin'])
                            self.oreFound.set("Tin Found!")
                        case num if num > 750000 and num <= 1000000:
                            data['iron'] += 1
                            self.iron.set(data['iron'])
                            self.oreFound.set("Iron Found!")
                
                case 1:
                    
                    match num:
                        case num if num <= 100000:
                            data['coal'] += 1
                            self.coal.set(data['coal'])
                            self.oreFound.set("Coal Found!")
                        case num if num > 100000 and num <= 250000:
                            data['tin'] += 1
                            self.tin.set(data['tin'])
                            self.oreFound.set("Tin Found!")
                        case num if num > 250000 and num <= 550000:
                            data['iron'] += 1
                            self.iron.set(data['iron'])
                            self.oreFound.set("Iron Found!")
                        case num if num > 550000 and num <= 750000:
                            data['tungsten'] += 1
                            self.tungsten.set(data['tungsten'])
                            self.oreFound.set("Tungsten\n Found!")
                        case num if num > 750000 and num <= 900000:
                            data['gold'] += 1
                            self.gold.set(data['gold'])
                            self.oreFound.set("Gold Found!")
                        case num if num > 900000 and num <= 1000000:
                            data['platinum'] += 1
                            self.platinum.set(data['platinum'])
                            self.oreFound.set("Platinum\n Found!")
                
                case 2:
                    
                    match num:
                        case num if num <= 50000:
                            data['coal'] += 1
                            self.coal.set(data['coal'])
                            self.oreFound.set("Coal Found!")
                        case num if num > 50000 and num <= 100000:
                            data['tin'] += 1
                            self.tin.set(data['tin'])
                            self.oreFound.set("Tin Found!")
                        case num if num > 100000 and num <= 150000:
                            data['iron'] += 1
                            self.iron.set(data['iron'])
                            self.oreFound.set("Iron Found!")
                        case num if num > 150000 and num <= 300000:
                            data['tungsten'] += 1
                            self.tungsten.set(data['tungsten'])
                            self.oreFound.set("Tungsten\n Found!")
                        case num if num > 300000 and num <= 500000:
                            data['gold'] += 1
                            self.gold.set(data['gold'])
                            self.oreFound.set("Gold Found!")
                        case num if num > 500000 and num <= 700000:
                            data['platinum'] += 1
                            self.platinum.set(data['platinum'])
                            self.oreFound.set("Platinum\n Found!")
                        case num if num > 700000 and num <= 800000:
                            data['diamond'] += 1
                            self.diamond.set(data['diamond'])
                            self.oreFound.set("Diamond\n Found!")
                        case num if num > 800000 and num <= 900000:
                            data['emerald'] += 1
                            self.emerald.set(data['emerald'])
                            self.oreFound.set("Emerald\n Found!")
                        case num if num > 900000 and num <= 1000000:
                            data['ruby'] += 1
                            self.ruby.set(data['ruby'])
                            self.oreFound.set("Ruby Found!")
                            
                case 3:
                    
                    match num:
                        case num if num <= 50000:
                            data['coal'] += 1
                            self.coal.set(data['coal'])
                            self.oreFound.set("Coal Found!")
                        case num if num > 50000 and num <= 100000:
                            data['tin'] += 1
                            self.tin.set(data['tin'])
                            self.oreFound.set("Tin Found!")
                        case num if num > 100000 and num <= 150000:
                            data['iron'] += 1
                            self.iron.set(data['iron'])
                            self.oreFound.set("Iron Found!")
                        case num if num > 150000 and num <= 200000:
                            data['tungsten'] += 1
                            self.tungsten.set(data['tungsten'])
                            self.oreFound.set("Tungsten\n Found!")
                        case num if num > 200000 and num <= 275000:
                            data['gold'] += 1
                            self.gold.set(data['gold'])
                            self.oreFound.set("Gold Found!")
                        case num if num > 275000 and num <= 475000:
                            data['platinum'] += 1
                            self.platinum.set(data['platinum'])
                            self.oreFound.set("Platinum\n Found!")
                        case num if num > 475000 and num <= 600000:
                            data['diamond'] += 1
                            self.diamond.set(data['diamond'])
                            self.oreFound.set("Diamond\n Found!")
                        case num if num > 600000 and num <= 725000:
                            data['emerald'] += 1
                            self.emerald.set(data['emerald'])
                            self.oreFound.set("Emerald\n Found!")
                        case num if num > 725000 and num <= 850000:
                            data['ruby'] += 1
                            self.ruby.set(data['ruby'])
                            self.oreFound.set("Ruby Found!")
                        case num if num > 850000 and num <= 900000:
                            data['mythril'] += 1
                            self.mythril.set(data['mythril'])
                            self.oreFound.set("Mythril\n Found!")
                        case num if num > 900000 and num <= 950000:
                            data['adamantite'] += 1
                            self.adamantite.set(data['adamantite'])
                            self.oreFound.set("Adamantite\n Found!")
                        case num if num > 950000 and num <= 1000000:
                            data['orichalcum'] += 1
                            self.orichalcum.set(data['orichalcum'])
                            self.oreFound.set("Orichalcum\n Found!")
                            
                case 4:
                    
                    match num:
                        case num if num <= 33000:
                            data['coal'] += 1
                            self.coal.set(data['coal'])
                            self.oreFound.set("Coal Found!")
                        case num if num > 33000 and num <= 66000:
                            data['tin'] += 1
                            self.tin.set(data['tin'])
                            self.oreFound.set("Tin Found!")
                        case num if num > 66000 and num <= 100000:
                            data['iron'] += 1
                            self.iron.set(data['iron'])
                            self.oreFound.set("Iron Found!")
                        case num if num > 150000 and num <= 200000:
                            data['tungsten'] += 1
                            self.tungsten.set(data['tungsten'])
                            self.oreFound.set("Tungsten\n Found!")
                        case num if num > 200000 and num <= 250000:
                            data['gold'] += 1
                            self.gold.set(data['gold'])
                            self.oreFound.set("Gold Found!")
                        case num if num > 250000 and num <= 300000:
                            data['platinum'] += 1
                            self.platinum.set(data['platinum'])
                            self.oreFound.set("Platinum\n Found!")
                        case num if num > 300000 and num <= 375000:
                            data['diamond'] += 1
                            self.diamond.set(data['diamond'])
                            self.oreFound.set("Diamond\n Found!")
                        case num if num > 375000 and num <= 450000:
                            data['emerald'] += 1
                            self.emerald.set(data['emerald'])
                            self.oreFound.set("Emerald\n Found!")
                        case num if num > 450000 and num <= 525000:
                            data['ruby'] += 1
                            self.ruby.set(data['ruby'])
                            self.oreFound.set("Ruby Found!")
                        case num if num > 525000 and num <= 650000:
                            data['mythril'] += 1
                            self.mythril.set(data['mythril'])
                            self.oreFound.set("Mythril\n Found!")
                        case num if num > 650000 and num <= 750000:
                            data['adamantite'] += 1
                            self.adamantite.set(data['adamantite'])
                            self.oreFound.set("Adamantite\n Found!")
                        case num if num > 750000 and num <= 850000:
                            data['orichalcum'] += 1
                            self.orichalcum.set(data['orichalcum'])
                            self.oreFound.set("Orichalcum\n Found!")
                        case num if num > 850000 and num <= 900000:
                            data['lanthanum'] += 1
                            self.lanthanum.set(data['lanthanum'])
                            self.oreFound.set("Lanthanum\n Found!")
                        case num if num > 900000 and num <= 950000:
                            data['cerium'] += 1
                            self.cerium.set(data['cerium'])
                            self.oreFound.set("Cerium Found!")
                        case num if num > 950000 and num <= 1000000:
                            data['praseodymium'] += 1
                            self.praseodymium.set(data['praseodymium'])
                            self.oreFound.set("Praseodymium\n Found!")
                            
                case 5:
                    
                    match num:
                        case num if num <= 33000:
                            data['coal'] += 1
                            self.coal.set(data['coal'])
                            self.oreFound.set("Coal Found!")
                        case num if num > 33000 and num <= 66000:
                            data['tin'] += 1
                            self.tin.set(data['tin'])
                            self.oreFound.set("Tin Found!")
                        case num if num > 66000 and num <= 100000:
                            data['iron'] += 1
                            self.iron.set(data['iron'])
                            self.oreFound.set("Iron Found!")
                        case num if num > 100000 and num <= 150000:
                            data['tungsten'] += 1
                            self.tungsten.set(data['tungsten'])
                            self.oreFound.set("Tungsten\n Found!")
                        case num if num > 150000 and num <= 200000:
                            data['gold'] += 1
                            self.gold.set(data['gold'])
                            self.oreFound.set("Gold Found!")
                        case num if num > 200000 and num <= 250000:
                            data['platinum'] += 1
                            self.platinum.set(data['platinum'])
                            self.oreFound.set("Platinum\n Found!")
                        case num if num > 250000 and num <= 300000:
                            data['diamond'] += 1
                            self.diamond.set(data['diamond'])
                            self.oreFound.set("Diamond\n Found!")
                        case num if num > 300000 and num <= 350000:
                            data['emerald'] += 1
                            self.emerald.set(data['emerald'])
                            self.oreFound.set("Emerald\n Found!")
                        case num if num > 350000 and num <= 400000:
                            data['ruby'] += 1
                            self.ruby.set(data['ruby'])
                            self.oreFound.set("Ruby Found!")
                        case num if num > 400000 and num <= 500000:
                            data['mythril'] += 1
                            self.mythril.set(data['mythril'])
                            self.oreFound.set("Mythril\n Found!")
                        case num if num > 500000 and num <= 600000:
                            data['adamantite'] += 1
                            self.adamantite.set(data['adamantite'])
                            self.oreFound.set("Adamantite\n Found!")
                        case num if num > 600000 and num <= 700000:
                            data['orichalcum'] += 1
                            self.orichalcum.set(data['orichalcum'])
                            self.oreFound.set("Orichalcum\n Found!")
                        case num if num > 700000 and num <= 800000:
                            data['lanthanum'] += 1
                            self.lanthanum.set(data['lanthanum'])
                            self.oreFound.set("Lanthanum\n Found!")
                        case num if num > 800000 and num <= 850000:
                            data['cerium'] += 1
                            self.cerium.set(data['cerium'])
                            self.oreFound.set("Cerium Found!")
                        case num if num > 850000 and num <= 900000:
                            data['praseodymium'] += 1
                            self.praseodymium.set(data['praseodymium'])
                            self.oreFound.set("Praseodymium\n Found!")
                        case num if num > 900000 and num <= 933000:
                            data['promethium'] += 1
                            self.promethium.set(data['promethium'])
                            self.oreFound.set("Promethium\n Found!")
                        case num if num > 933000 and num <= 966000:
                            data['europium'] += 1
                            self.europium.set(data['europium'])
                            self.oreFound.set("Europium\n Found!")
                        case num if num > 966000 and num <= 1000000:
                            data['hafnium'] += 1
                            self.hafnium.set(data['hafnium'])
                            self.oreFound.set("Hafnium Found!")
                            
                case 6:
                    
                    match num:
                        case num if num <= 25000:
                            data['coal'] += 1
                            self.coal.set(data['coal'])
                            self.oreFound.set("Coal Found!")
                        case num if num > 25000 and num <= 50000:
                            data['tin'] += 1
                            self.tin.set(data['tin'])
                            self.oreFound.set("Tin Found!")
                        case num if num > 50000 and num <= 75000:
                            data['iron'] += 1
                            self.iron.set(data['iron'])
                            self.oreFound.set("Iron Found!")
                        case num if num > 75000 and num <= 100000:
                            data['tungsten'] += 1
                            self.tungsten.set(data['tungsten'])
                            self.oreFound.set("Tungsten\n Found!")
                        case num if num > 100000 and num <= 150000:
                            data['gold'] += 1
                            self.gold.set(data['gold'])
                            self.oreFound.set("Gold Found!")
                        case num if num > 150000 and num <= 200000:
                            data['platinum'] += 1
                            self.platinum.set(data['platinum'])
                            self.oreFound.set("Platinum\n Found!")
                        case num if num > 200000 and num <= 250000:
                            data['diamond'] += 1
                            self.diamond.set(data['diamond'])
                            self.oreFound.set("Diamond\n Found!")
                        case num if num > 250000 and num <= 300000:
                            data['emerald'] += 1
                            self.emerald.set(data['emerald'])
                            self.oreFound.set("Emerald\n Found!")
                        case num if num > 300000 and num <= 350000:
                            data['ruby'] += 1
                            self.ruby.set(data['ruby'])
                            self.oreFound.set("Ruby Found!")
                        case num if num > 350000 and num <= 425000:
                            data['mythril'] += 1
                            self.mythril.set(data['mythril'])
                            self.oreFound.set("Mythril\n Found!")
                        case num if num > 425000 and num <= 500000:
                            data['adamantite'] += 1
                            self.adamantite.set(data['adamantite'])
                            self.oreFound.set("Adamantite\n Found!")
                        case num if num > 500000 and num <= 575000:
                            data['orichalcum'] += 1
                            self.orichalcum.set(data['orichalcum'])
                            self.oreFound.set("Orichalcum\n Found!")
                        case num if num > 575000 and num <= 650000:
                            data['lanthanum'] += 1
                            self.lanthanum.set(data['lanthanum'])
                            self.oreFound.set("Lanthanum\n Found!")
                        case num if num > 650000 and num <= 700000:
                            data['cerium'] += 1
                            self.cerium.set(data['cerium'])
                            self.oreFound.set("Cerium Found!")
                        case num if num > 700000 and num <= 750000:
                            data['praseodymium'] += 1
                            self.praseodymium.set(data['praseodymium'])
                            self.oreFound.set("Praseodymium\n Found!")
                        case num if num > 750000 and num <= 800000:
                            data['promethium'] += 1
                            self.promethium.set(data['promethium'])
                            self.oreFound.set("Promethium\n Found!")
                        case num if num > 800000 and num <= 850000:
                            data['europium'] += 1
                            self.europium.set(data['europium'])
                            self.oreFound.set("Europium\n Found!")
                        case num if num > 850000 and num <= 900000:
                            data['hafnium'] += 1
                            self.hafnium.set(data['hafnium'])
                            self.oreFound.set("Hafnium\n Found!")
                        case num if num > 900000 and num <= 933000:
                            data['osmium'] += 1
                            self.osmium.set(data['osmium'])
                            self.oreFound.set("Osmium Found!")
                        case num if num > 933000 and num <= 966000:
                            data['bismuth'] += 1
                            self.bismuth.set(data['bismuth'])
                            self.oreFound.set("Bismuth\n Found!")
                        case num if num > 966000 and num <= 1000000:
                            data['francium'] += 1
                            self.francium.set(data['francium'])
                            self.oreFound.set("Francium\n Found!")
                            
                case 7:
                    
                    match num:
                        case num if num <= 25000:
                            data['coal'] += 1
                            self.coal.set(data['coal'])
                            self.oreFound.set("Coal Found!")
                        case num if num > 25000 and num <= 50000:
                            data['tin'] += 1
                            self.tin.set(data['tin'])
                            self.oreFound.set("Tin Found!")
                        case num if num > 50000 and num <= 75000:
                            data['iron'] += 1
                            self.iron.set(data['iron'])
                            self.oreFound.set("Iron Found!")
                        case num if num > 75000 and num <= 100000:
                            data['tungsten'] += 1
                            self.tungsten.set(data['tungsten'])
                            self.oreFound.set("Tungsten\n Found!")
                        case num if num > 100000 and num <= 125000:
                            data['gold'] += 1
                            self.gold.set(data['gold'])
                            self.oreFound.set("Gold Found!")
                        case num if num > 125000 and num <= 150000:
                            data['platinum'] += 1
                            self.platinum.set(data['platinum'])
                            self.oreFound.set("Platinum\n Found!")
                        case num if num > 150000 and num <= 200000:
                            data['diamond'] += 1
                            self.diamond.set(data['diamond'])
                            self.oreFound.set("Diamond\n Found!")
                        case num if num > 200000 and num <= 250000:
                            data['emerald'] += 1
                            self.emerald.set(data['emerald'])
                            self.oreFound.set("Emerald\n Found!")
                        case num if num > 250000 and num <= 300000:
                            data['ruby'] += 1
                            self.ruby.set(data['ruby'])
                            self.oreFound.set("Ruby Found!")
                        case num if num > 300000 and num <= 350000:
                            data['mythril'] += 1
                            self.mythril.set(data['mythril'])
                            self.oreFound.set("Mythril\n Found!")
                        case num if num > 350000 and num <= 400000:
                            data['adamantite'] += 1
                            self.adamantite.set(data['adamantite'])
                            self.oreFound.set("Adamantite\n Found!")
                        case num if num > 400000 and num <= 450000:
                            data['orichalcum'] += 1
                            self.orichalcum.set(data['orichalcum'])
                            self.oreFound.set("Orichalcum\n Found!")
                        case num if num > 450000 and num <= 500000:
                            data['lanthanum'] += 1
                            self.lanthanum.set(data['lanthanum'])
                            self.oreFound.set("Lanthanum\n Found!")
                        case num if num > 500000 and num <= 550000:
                            data['cerium'] += 1
                            self.cerium.set(data['cerium'])
                            self.oreFound.set("Cerium Found!")
                        case num if num > 550000 and num <= 600000:
                            data['praseodymium'] += 1
                            self.praseodymium.set(data['praseodymium'])
                            self.oreFound.set("Praseodymium\n Found!")
                        case num if num > 600000 and num <= 650000:
                            data['promethium'] += 1
                            self.promethium.set(data['promethium'])
                            self.oreFound.set("Promethium\n Found!")
                        case num if num > 650000 and num <= 700000:
                            data['europium'] += 1
                            self.europium.set(data['europium'])
                            self.oreFound.set("Europium\n Found!")
                        case num if num > 700000 and num <= 750000:
                            data['hafnium'] += 1
                            self.hafnium.set(data['hafnium'])
                            self.oreFound.set("Hafnium\n Found!")
                        case num if num > 750000 and num <= 800000:
                            data['osmium'] += 1
                            self.osmium.set(data['osmium'])
                            self.oreFound.set("Osmium Found!")
                        case num if num > 800000 and num <= 850000:
                            data['bismuth'] += 1
                            self.bismuth.set(data['bismuth'])
                            self.oreFound.set("Bismuth\n Found!")
                        case num if num > 850000 and num <= 900000:
                            data['francium'] += 1
                            self.francium.set(data['francium'])
                            self.oreFound.set("Francium\n Found!")
                        case num if num > 900000 and num <= 933000:
                            data['neptunium'] += 1
                            self.neptunium.set(data['neptunium'])
                            self.oreFound.set("Neptunium\n Found!")
                        case num if num > 933000 and num <= 966000:
                            data['californium'] += 1
                            self.californium.set(data['californium'])
                            self.oreFound.set("Californium\n Found!")
                        case num if num > 966000 and num <= 1000000:
                            data['einsteinium'] += 1
                            self.einsteinium.set(data['einsteinium'])
                            self.oreFound.set("Einsteinium\n Found!")
                            
                case 8:
                    
                    match num:
                        case num if num <= 10000:
                            data['coal'] += 1
                            self.coal.set(data['coal'])
                            self.oreFound.set("Coal Found!")
                        case num if num > 10000 and num <= 20000:
                            data['tin'] += 1
                            self.tin.set(data['tin'])
                            self.oreFound.set("Tin Found!")
                        case num if num > 20000 and num <= 30000:
                            data['iron'] += 1
                            self.iron.set(data['iron'])
                            self.oreFound.set("Iron Found!")
                        case num if num > 30000 and num <= 40000:
                            data['tungsten'] += 1
                            self.tungsten.set(data['tungsten'])
                            self.oreFound.set("Tungsten\n Found!")
                        case num if num > 40000 and num <= 50000:
                            data['gold'] += 1
                            self.gold.set(data['gold'])
                            self.oreFound.set("Gold Found!")
                        case num if num > 50000 and num <= 60000:
                            data['platinum'] += 1
                            self.platinum.set(data['platinum'])
                            self.oreFound.set("Platinum\n Found!")
                        case num if num > 60000 and num <= 70000:
                            data['diamond'] += 1
                            self.diamond.set(data['diamond'])
                            self.oreFound.set("Diamond\n Found!")
                        case num if num > 70000 and num <= 80000:
                            data['emerald'] += 1
                            self.emerald.set(data['emerald'])
                            self.oreFound.set("Emerald\n Found!")
                        case num if num > 80000 and num <= 90000:
                            data['ruby'] += 1
                            self.ruby.set(data['ruby'])
                            self.oreFound.set("Ruby Found!")
                        case num if num > 90000 and num <= 100000:
                            data['mythril'] += 1
                            self.mythril.set(data['mythril'])
                            self.oreFound.set("Mythril\n Found!")
                        case num if num > 100000 and num <= 125000:
                            data['adamantite'] += 1
                            self.adamantite.set(data['adamantite'])
                            self.oreFound.set("Adamantite\n Found!")
                        case num if num > 125000 and num <= 150000:
                            data['orichalcum'] += 1
                            self.orichalcum.set(data['orichalcum'])
                            self.oreFound.set("Orichalcum\n Found!")
                        case num if num > 150000 and num <= 175000:
                            data['lanthanum'] += 1
                            self.lanthanum.set(data['lanthanum'])
                            self.oreFound.set("Lanthanum\n Found!")
                        case num if num > 175000 and num <= 200000:
                            data['cerium'] += 1
                            self.cerium.set(data['cerium'])
                            self.oreFound.set("Cerium Found!")
                        case num if num > 200000 and num <= 275000:
                            data['praseodymium'] += 1
                            self.praseodymium.set(data['praseodymium'])
                            self.oreFound.set("Praseodymium\n Found!")
                        case num if num > 275000 and num <= 325000:
                            data['promethium'] += 1
                            self.promethium.set(data['promethium'])
                            self.oreFound.set("Promethium\n Found!")
                        case num if num > 325000 and num <= 375000:
                            data['europium'] += 1
                            self.europium.set(data['europium'])
                            self.oreFound.set("Europium\n Found!")
                        case num if num > 375000 and num <= 425000:
                            data['hafnium'] += 1
                            self.hafnium.set(data['hafnium'])
                            self.oreFound.set("Hafnium\n Found!")
                        case num if num > 425000 and num <= 500000:
                            data['osmium'] += 1
                            self.osmium.set(data['osmium'])
                            self.oreFound.set("Osmium Found!")
                        case num if num > 500000 and num <= 575000:
                            data['bismuth'] += 1
                            self.bismuth.set(data['bismuth'])
                            self.oreFound.set("Bismuth\n Found!")
                        case num if num > 575000 and num <= 650000:
                            data['francium'] += 1
                            self.francium.set(data['francium'])
                            self.oreFound.set("Francium\n Found!")
                        case num if num > 650000 and num <= 750000:
                            data['neptunium'] += 1
                            self.neptunium.set(data['neptunium'])
                            self.oreFound.set("Neptunium\n Found!")
                        case num if num > 750000 and num <= 850000:
                            data['californium'] += 1
                            self.californium.set(data['californium'])
                            self.oreFound.set("Californium\n Found!")
                        case num if num > 850000 and num <= 950000:
                            data['einsteinium'] += 1
                            self.einsteinium.set(data['einsteinium'])
                            self.oreFound.set("Einsteinium\n Found!")
                        case num if num > 950000 and num <= 975000:
                            data['astatine'] += 1
                            self.astatine.set(data['astatine'])
                            self.oreFound.set("Astatine\n Found!")
                        case num if num > 975000 and num <= 999999:
                            data['tennessine'] += 1
                            self.tennessine.set(data['tennessine'])
                            self.oreFound.set("Tennessine\n Found!")
                        case num if num == 1000000:
                            data['soakite'] += 1
                            self.soakite.set(data['soakite'])
                            self.oreFound.set("SOAKITE\n FOUND!!!")
                            
            with open(f"{os.getcwd()}{datajson}", "w") as file:
                json.dump(data, file, indent=4)
             

    def upgradePickaxeLevel(self):
        
        if data['pickaxeLevel'] >= 0 and data['pickaxeLevel'] < 8:
            
            match data['pickaxeLevel']:
                
                case 0:
                    data['pickaxeLevelCost'] = 500
                    self.upgradeCost.set(data['pickaxeLevelCost'])
                    
                    if data['dabloons'] >= data['pickaxeLevelCost']:
                        data['dabloons'] -= data['pickaxeLevelCost']
                        data['pickaxeLevel'] += 1
                        data['pickaxeLevelCost'] = 5000
                        self.upgradeCost.set(data['pickaxeLevelCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 1:
                    data['pickaxeLevelCost'] = 5000
                    self.upgradeCost.set(data['pickaxeLevelCost'])
                    
                    if data['dabloons'] >= data['pickaxeLevelCost']:
                        data['dabloons'] -= data['pickaxeLevelCost']
                        data['pickaxeLevel'] += 1
                        data['pickaxeLevelCost'] = 50000
                        self.upgradeCost.set(data['pickaxeLevelCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 2:
                    data['pickaxeLevelCost'] = 50000
                    self.upgradeCost.set(data['pickaxeLevelCost'])
                    
                    if data['dabloons'] >= data['pickaxeLevelCost']:
                        data['dabloons'] -= data['pickaxeLevelCost']
                        data['pickaxeLevel'] += 1
                        data['pickaxeLevelCost'] = 500000
                        self.upgradeCost.set(data['pickaxeLevelCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 3:
                    data['pickaxeLevelCost'] = 500000
                    self.upgradeCost.set(data['pickaxeLevelCost'])
                    
                    if data['dabloons'] >= data['pickaxeLevelCost']:
                        data['dabloons'] -= data['pickaxeLevelCost']
                        data['pickaxeLevel'] += 1
                        data['pickaxeLevelCost'] = 5000000
                        self.upgradeCost.set(data['pickaxeLevelCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 4:
                    data['pickaxeLevelCost'] = 5000000
                    self.upgradeCost.set(data['pickaxeLevelCost'])
                    
                    if data['dabloons'] >= data['pickaxeLevelCost']:
                        data['dabloons'] -= data['pickaxeLevelCost']
                        data['pickaxeLevel'] += 1
                        data['pickaxeLevelCost'] = 10000000
                        self.upgradeCost.set(data['pickaxeLevelCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 5:
                    data['pickaxeLevelCost'] = 10000000
                    self.upgradeCost.set(data['pickaxeLevelCost'])
                    
                    if data['dabloons'] >= data['pickaxeLevelCost']:
                        data['dabloons'] -= data['pickaxeLevelCost']
                        data['pickaxeLevel'] += 1
                        data['pickaxeLevelCost'] = 100000000
                        self.upgradeCost.set(data['pickaxeLevelCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 6:
                    data['pickaxeLevelCost'] = 100000000
                    self.upgradeCost.set(data['pickaxeLevelCost'])
                    
                    if data['dabloons'] >= data['pickaxeLevelCost']:
                        data['dabloons'] -= data['pickaxeLevelCost']
                        data['pickaxeLevel'] += 1
                        data['pickaxeLevelCost'] = 1000000000
                        self.upgradeCost.set(data['pickaxeLevelCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 7:
                    data['pickaxeLevelCost'] = 1000000000
                    self.upgradeCost.set(data['pickaxeLevelCost'])
                    
                    if data['dabloons'] >= data['pickaxeLevelCost']:
                        data['dabloons'] -= data['pickaxeLevelCost']
                        data['pickaxeLevel'] += 1
                        data['pickaxeLevelCost'] = 5000000000
                        self.upgradeCost.set(data['pickaxeLevelCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
        else:
            data['pickaxeLevelCost'] = 0
            self.upgradeCost.set(data['pickaxeLevelCost'])
            
            with open(f"{os.getcwd()}{datajson}", "w") as file:
                json.dump(data, file, indent=4) 


    def upgradePickaxeSpeed(self):
        
        if data['pickaxeSpeed'] >= 0 and data['pickaxeSpeed'] < 8:
            
            match data['pickaxeSpeed']:
                
                case 0:
                    data['pickaxeSpeedCost'] = 500
                    self.speedCost.set(data['pickaxeSpeedCost'])
                    
                    if data['dabloons'] >= data['pickaxeSpeedCost']:
                        data['dabloons'] -= data['pickaxeSpeedCost']
                        data['pickaxeSpeed'] += 1
                        data['pickaxeSpeedCost'] = 5000
                        self.speedCost.set(data['pickaxeSpeedCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 1:
                    data['pickaxeSpeedCost'] = 5000
                    self.speedCost.set(data['pickaxeSpeedCost'])
                    
                    if data['dabloons'] >= data['pickaxeSpeedCost']:
                        data['dabloons'] -= data['pickaxeSpeedCost']
                        data['pickaxeSpeed'] += 1
                        data['pickaxeSpeedCost'] = 50000
                        self.speedCost.set(data['pickaxeSpeedCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 2:
                    data['pickaxeSpeedCost'] = 50000
                    self.speedCost.set(data['pickaxeSpeedCost'])
                    
                    if data['dabloons'] >= data['pickaxeSpeedCost']:
                        data['dabloons'] -= data['pickaxeSpeedCost']
                        data['pickaxeSpeed'] += 1
                        data['pickaxeSpeedCost'] = 500000
                        self.speedCost.set(data['pickaxeSpeedCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 3:
                    data['pickaxeSpeedCost'] = 500000
                    self.speedCost.set(data['pickaxeSpeedCost'])
                    
                    if data['dabloons'] >= data['pickaxeSpeedCost']:
                        data['dabloons'] -= data['pickaxeSpeedCost']
                        data['pickaxeSpeed'] += 1
                        data['pickaxeSpeedCost'] = 5000000
                        self.speedCost.set(data['pickaxeSpeedCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 4:
                    data['pickaxeSpeedCost'] = 5000000
                    self.speedCost.set(data['pickaxeSpeedCost'])
                    
                    if data['dabloons'] >= data['pickaxeSpeedCost']:
                        data['dabloons'] -= data['pickaxeSpeedCost']
                        data['pickaxeSpeed'] += 1
                        data['pickaxeSpeedCost'] = 10000000
                        self.speedCost.set(data['pickaxeSpeedCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 5:
                    data['pickaxeSpeedCost'] = 10000000
                    self.speedCost.set(data['pickaxeSpeedCost'])
                    
                    if data['dabloons'] >= data['pickaxeSpeedCost']:
                        data['dabloons'] -= data['pickaxeSpeedCost']
                        data['pickaxeSpeed'] += 1
                        data['pickaxeSpeedCost'] = 100000000
                        self.speedCost.set(data['pickaxeSpeedCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 6:
                    data['pickaxeSpeedCost'] = 100000000
                    self.speedCost.set(data['pickaxeSpeedCost'])
                    
                    if data['dabloons'] >= data['pickaxeSpeedCost']:
                        data['dabloons'] -= data['pickaxeSpeedCost']
                        data['pickaxeSpeed'] += 1
                        data['pickaxeSpeedCost'] = 1000000000
                        self.speedCost.set(data['pickaxeSpeedCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
                case 7:
                    data['pickaxeSpeedCost'] = 1000000000
                    self.speedCost.set(data['pickaxeSpeedCost'])
                    
                    if data['dabloons'] >= data['pickaxeSpeedCost']:
                        data['dabloons'] -= data['pickaxeSpeedCost']
                        data['pickaxeSpeed'] += 1
                        data['pickaxeSpeedCost'] = 5000000000
                        self.speedCost.set(data['pickaxeSpeedCost'])
                        self.dabloons.set(data['dabloons'])
                        
                        with open(f"{os.getcwd()}{datajson}", "w") as file:
                            json.dump(data, file, indent=4)
        else:
            data['pickaxeSpeedCost'] = 0
            self.speedCost.set(data['pickaxeSpeedCost'])
            
            with open(f"{os.getcwd()}{datajson}", "w") as file:
                json.dump(data, file, indent=4)
            


if __name__ == "__main__":
    app = UiApp()
    app.run()
