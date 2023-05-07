# 登月任務
# 將 Agent 傳送到太空小艇以交付計算結果。
# 你無法計算 Agent 完成任務所需移動的空間。
# 請思考必要的移動，並運用數學家的計算結果來確認 Agent 必須移動多少步。
# 使用 agent.move() 讓 Agent 抵達登月小艇並停靠。

# agent.move() 函數採用了一個參數：方向。
# 有效的方向為：
# 前進 (forward)
# 退後 (back)
# 向左 (left)
# 向上 (up)
# 向下 (down)

#agent.turn() 函數採用了一組參數：turn_direction。
#有效的方向為：
#向左 (left)
#向右 (right)

# 使用迴圈的作法
for i in range(25):
    agent.move("forward")
agent.turn("right")

for i in range(17):
    agent.move("forward")
agent.turn("right")

for i in range(3):
    agent.move("down")

# 如果不使用迴圈程式碼會變得很冗長
# 所以在這題開始會建議大家學會 for 迴圈
# 透過 for 迴圈可以讓程式碼更簡潔
# 並且更容易的執行重複的動作
# 如果不使用迴圈的作法就會像下面這樣
agent.move("forward")
agent.move("forward")
agent.move("forward")
# ... 重複 25 次

agent.turn("right") # 右轉

agent.move("forward")
agent.move("forward")
agent.move("forward")
# ... 重複 17 次

agent.turn("right") # 右轉

agent.move("down")
agent.move("down")
agent.move("down")