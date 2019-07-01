from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create("127.0.0.1 ", 4711)
# This sets the x,y and z location to set blocks.
x, y, z = mc.player.getPos()

# Clear with ait (air = 0)
air = 0
mc.setBlocks(x-100,y, z-100, x+100, y+100, z+100,air)
mc.setBlocks(x-100,y-1,z-100, x+100, y-1, z+100,2)
#leg left
mc.setBlocks(x-5,y,z,x-7,y,z,35,12)
mc.setBlocks(x-4,y,z-1,x-8,y,z-1,35,12)
mc.setBlocks(x-4,y,z-2,x-8,y,z-2,35,12)
mc.setBlocks(x-3,y,z-3,x-7,y,z-3,35,12)
mc.setBlocks(x-3,y,z-4,x-6,y,z-4,35,12)
mc.setBlocks(x-2,y,z-5,x-5,y,z-5,35,12)
mc.setBlocks(x-2,y,z-6,x-5,y,z-8,35,12)
mc.setBlocks(x-2,y,z-9,x-4,y,z-9,35,12)
mc.setBlocks(x+1,y,z-10,x-4,y,z-10,35,12)


#leg right
mc.setBlocks(x+5,y,z,x+9,y,z-3,35,12)
mc.setBlocks(x+4,y,z-4,x+8,y,z-5,35,12)
mc.setBlocks(x+3,y,z-6,x+7,y,z-7,35,12)
mc.setBlocks(x+3,y,z-8,x+8,y,z-9,35,12)
mc.setBlocks(x+2,y,z-10,x+9,y,z-10,35,12)

#body
mc.setBlocks(x-4,y,z-11,x+10,y,z-11,35,12)
mc.setBlocks(x-3,y,z-12,x+10,y,z-12,35,12)
mc.setBlocks(x-2,y,z-13,x+10,y,z-13,35,12)
mc.setBlocks(x,y,z-11,x,y,z-12,35,4)
mc.setBlocks(x-1,y,z-14,x+10,y,z-14,35,12)
mc.setBlocks(x-1,y,z-15,x+9,y,z-16,35,12)
mc.setBlocks(x-1,y,z-17,x+8,y,z-17,35,12)
mc.setBlocks(x-1,y,z-18,x+7,y,z-18,35,12)
mc.setBlocks(x+4,y,z-14,x+4,y,z-15,35,4)
mc.setBlocks(x+5,y,z-15,x+5,y,z-16,35,4)
mc.setBlocks(x,y,z-19,x+8,y,z-22,35,12)
mc.setBlocks(x+2,y,z-19,x+2,y,z-20,35,4)
mc.setBlocks(x+7,y,z-21,x+7,y,z-22,35,4)
mc.setBlocks(x+1,y,z-23,x+9,y,z-25,35,12)
mc.setBlocks(x,y,z-26,x+12,y,z-26,35,12)
mc.setBlocks(x-2,y,z-27,x+13,y,z-27,35,12)
mc.setBlocks(x-4,y,z-28,x+14,y,z-28,35,12)
mc.setBlocks(x-5,y,z-29,x+15,y,z-29,35,12)
mc.setBlocks(x-6,y,z-30,x+16,y,z-30,35,12)
mc.setBlocks(x+4,y,z-24,x+4,y,z-26,35,4)



#left arm
mc.setBlocks(x-8,y,z-31,x-3,y,z-31,35,12)
mc.setBlocks(x-9,y,z-32,x-4,y,z-32,35,12)
mc.setBlocks(x-10,y,z-33,x-5,y,z-33,35,12)
mc.setBlocks(x-9,y,z-34,x-6,y,z-34,35,12)
mc.setBlocks(x-8,y,z-35,x-7,y,z-35,35,12)
mc.setBlocks(x-10,y,z-34,x-15,y,z-39,35,5)
mc.setBlocks(x-9,y,z-35,x-14,y,z-39,35,5)
mc.setBlocks(x-11,y,z-34,x-15,y,z-34,35,5)
mc.setBlocks(x-7,y,z-34,x-2,y,z-39,35,5)
mc.setBlocks(x-9,y,z-32,x-15,y,z-27,35,5)


#right arm
mc.setBlocks(x+13,y,z-31,x+17,y,z-31,35,12)
mc.setBlocks(x+14,y,z-32,x+18,y,z-32,35,12)
mc.setBlocks(x+15,y,z-33,x+17,y,z-33,35,12)
mc.setBlocks(x+16,y,z-34,x+16,y,z-34,35,12)
mc.setBlocks(x+15,y,z-34,x+12,y,z-39,35,5)
mc.setBlocks(x+17,y,z-33,x+22,y,z-39,35,5)
mc.setBlocks(x+17,y,z-31,x+22,y,z-26,35,5)










#head
mc.setBlocks(x,y,z-31,x+10,y,z-32,35,12)
mc.setBlocks(x+1,y,z-33,x+11,y,z-42,35,12)
mc.setBlocks(x+4,y,z-35,x+7,y,z-35,35,14)
mc.setBlock(x+3,y,z-35,35,15)
mc.setBlock(x+8,y,z-35,35,15)
mc.setBlocks(x+4,y,z-34,x+7,y,z-34,35,15)
mc.setBlocks(x+4,y,z-39,x+4,y,z-40,35,15)
mc.setBlocks(x+8,y,z-39,x+8,y,z-40,35,15)
mc.setBlocks(x+5,y,z-43,x+7,y,z-50,35,12)
mc.setBlocks(x+8,y,z-48,x+10,y,z-50,35,12)
mc.setBlocks(x+4,y,z-48,x+2,y,z-50,35,12)



#WOOL:
#0: White
#1: Orange
#2: Magenta
#3: Light Blue
#4: Yellow
#5: Lime
#6: Pink
#7: Grey
#8: Light grey
#9: Cyan
#10: Purple
#11: Blue
#12: Brown
#13: Green
#14: Red
#15:Black
