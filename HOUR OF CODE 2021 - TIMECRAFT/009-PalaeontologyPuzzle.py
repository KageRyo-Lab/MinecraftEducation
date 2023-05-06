#官方給予的程式碼有誤
#修改前
#agent.give("BONEBLOCK", 64, 1)
#修改後
#agent.give("BONE BLOCK", 64, 1)

agent.give("BONE BLOCK", 64, 1)

for i in range(4):
    agent.move("forward")
    agent.move("forward")
    agent.destroy("down")
    agent.place("down", 1)
