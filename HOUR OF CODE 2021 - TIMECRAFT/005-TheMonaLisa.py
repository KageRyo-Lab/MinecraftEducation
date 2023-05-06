

# 在這裡編寫程式碼

agent.give("WHITE GLAZED TERRACOTTA", 64, 1)

for i in range(5):
    agent.move("forward")
    agent.place("down", 1)

agent.turn("right")

for i in range(5):
    agent.move("forward")
    agent.place("down", 1)
