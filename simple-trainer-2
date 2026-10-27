import time
import pymem
import os

try:
    pm = pymem.Pymem('ac_client.exe')
    module = pymem.process.module_from_name(
        pm.process_handle, "ac_client.exe"
    )

    base = module.lpBaseOfDll
    print('Connected with ac_client.exe.')

except Exception:
    print('Can\'t connect with ac_client.exe.')

class localPlayer:
    def __init__(self, address):
        self.playerAddress = address

    @property
    def health(self):
        oHealth = 0x04
        return pm.read_uint(self.playerAddress + oHealth)

    @health.setter
    def health(self, value):
        oHealth = 0x04
        pm.write_uint(self.playerAddress + oHealth, value)

    @property
    def kevlar(self):
        oKevlar = 0x08
        return pm.read_uint(self.playerAddress + oKevlar)

    @kevlar.setter
    def kevlar(self, value):
        oKevlar = 0x08
        pm.write_uint(self.playerAddress + oKevlar, value)

    @property
    def grenades(self):
        oGrenades = 0x5c
        return pm.read_uint(self.playerAddress + oGrenades)

    @grenades.setter
    def grenades(self, value):
        oGrenades = 0x5c
        pm.write_uint(self.playerAddress + oGrenades, value)

    @property
    def rifleAmmo(self):
        oRifleAmmo = 0x58
        return pm.read_uint(self.playerAddress + oRifleAmmo)

    @rifleAmmo.setter
    def rifleAmmo(self, value):
        oRifleAmmo = 0x58
        pm.write_uint(self.playerAddress + oRifleAmmo, value)

    @property
    def pistolAmmo(self):
        oPistolAmmo = 0x44
        return pm.read_uint(self.playerAddress + oPistolAmmo)

    @pistolAmmo.setter
    def pistolAmmo(self, value):
        oPistolAmmo = 0x44
        pm.write_uint(self.playerAddress + oPistolAmmo, value)

    @property
    def nickname(self):
        oNickname = 0x11D
        return pm.read_string(self.playerAddress + oNickname)

    @nickname.setter
    def nickname(self, value):
        oNickname = 0x11D
        pm.write_string(self.playerAddress + oNickname, value)

def main():
    playerAddress = pm.read_uint(base + 0x0017E0A8) + 0xE8
    player = localPlayer(playerAddress)
    while True:
        os.system('cls')
        player.health = 1337
        player.kevlar = 999
        player.grenades = 999
        player.rifleAmmo = 999
        player.pistolAmmo = 999

        print('Welcome,', player.nickname)
        print()
        print('Health: ', player.health)
        print('Kevlar: ', player.kevlar)
        print('Grenades: ', player.grenades)
        print('Rifle Ammo: ', player.rifleAmmo)
        print('Pistol ammo: ', player.pistolAmmo)
        time.sleep(0.5)
if __name__ == '__main__':
    main()



