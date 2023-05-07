# 官方給予的程式碼有誤
# 修改前
# agent.drop(1, 1) 
# 修改後
# agent.drop("BEETROOT", 1) 
agent.give("BEETROOT", 64, 1)
for i in range(6):
    agent.drop("BEETROOT", 1) 
    agent.move("forward")
    agent.move("forward")
    agent.move("forward")
    agent.move("forward")
