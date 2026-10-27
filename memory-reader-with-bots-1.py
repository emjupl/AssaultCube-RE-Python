import pymem
import time

pm = pymem.Pymem("ac_client.exe")

module = pymem.process.module_from_name(
    pm.process_handle, "ac_client.exe"
)
base = module.lpBaseOfDll

def isOnGround(address):
    addressValue = pm.read_int(address)
    if addressValue != 0:
        return True
    else:
        return False

def main():
    if (module):
        ObjectList = base + 0x0018AC04
        ObjectListStart = pm.read_uint(ObjectList)

        ammoAddress = base + 0x00183828

        ammoAddress = pm.read_uint(ammoAddress) + 0x8
        ammoAddress = pm.read_uint(ammoAddress) + 0x98
        ammoAddress = pm.read_uint(ammoAddress) + 0x30
        ammoAddress = pm.read_uint(ammoAddress) + 0x2F0

        while True:
            playerCount = base + 0x0005C434
            playerCount = pm.read_uint(playerCount)
            playerCount = pm.read_uint(playerCount)

            xcoordAddress = base + 0x0017E0A8

            xcoordAddress = pm.read_uint(xcoordAddress) + 0x28
            ycoordAddress = xcoordAddress + 4
            zcoordAddress = xcoordAddress + 8
            yawAddress = xcoordAddress + 12
            pitchAddress = xcoordAddress + 16

            isOnGroundAddress = base + 0x00183828
            isOnGroundAddress = pm.read_uint(isOnGroundAddress) + 0x8
            isOnGroundAddress = pm.read_uint(isOnGroundAddress) + 0xDA8
            isOnGroundAddress = pm.read_uint(isOnGroundAddress) + 0x108

            oNickname = 0x0205
            oHealth = 0x00EC
            oXcoord = 0x004
            oYcoord = 0x008
            oZcoord = 0x00C

            print('------------------------------ Local Player values ------------------------------')
            ammoValue = pm.read_int(ammoAddress)
            xcoordValue = pm.read_float(xcoordAddress)
            ycoordValue = pm.read_float(ycoordAddress)
            zcoordValue = pm.read_float(zcoordAddress) + 4.5
            yawValue = pm.read_float(yawAddress)
            pitchValue = pm.read_float(pitchAddress)
            isOnGroundBool = isOnGround(isOnGroundAddress)

            print('Ammo Value: ', ammoValue)
            print('X: ', xcoordValue)
            print('y: ', ycoordValue)
            print('z: ', zcoordValue)
            print('Yaw:', yawValue)
            print('Pitch:', pitchValue)

            print('Is On Ground?:', isOnGroundBool)

            for i in range(1, playerCount):
                print('---------------------------------------',i, '---------------------------------------')
                entityAddress = ObjectListStart + 4*i
                entityNickname= pm.read_uint(entityAddress) + oNickname
                entityNickname = pm.read_string(entityNickname)
                entityXcoord = pm.read_uint(entityAddress) + oXcoord
                entityXcoord = pm.read_float(entityXcoord)
                print('X:', entityXcoord)

                entityYcoord = pm.read_uint(entityAddress) + oYcoord
                entityYcoord = pm.read_float(entityYcoord)
                print('Y: ', entityYcoord)

                entityZcoord = pm.read_uint(entityAddress) + oZcoord
                entityZcoord = pm.read_float(entityZcoord)
                print('Z: ', entityZcoord)

                entityHealth = pm.read_uint(entityAddress) + oHealth
                entityHealth = pm.read_int(entityHealth)

                if(entityHealth > 0):
                    print('HP: ', entityHealth)
                else:
                    print('HP: ', red, 'DEAD', reset)

                print('Nickname: ',entityNickname)

            time.sleep(0.2)
            os.system('cls')

main()






