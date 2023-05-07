# 古生物學謎題
# 有人從恐龍骨架上取下了骨頭，並且用橙色方塊代替。
# 編寫程式碼，讓 Agent 破壞全部 4 個橙色方塊，並放置 BONEBLOCK。
# 使用 agent.give() 函數給 Agent 一堆 BONEBLOCK，然後使用 agent.move() 移動 Agent 至橙色方塊上方，然後使用 agent.destroy() 打破橙色方塊並使用 agent.place() 將其替換成 BONEBLOCK。

# agent.give() 函數採用了三組參數。
# 物品 (字串)：你要給 Agent 的物品。
# 數量 (整數)：Agent 將收到多少物品。
# 欄位 (整數)：Agent 接收物品的庫存欄位。

# agent.move() 函數採用了一組參數：direction。
# 有效的方向為：
# 前進 (forward)
# 退後 (back)
# 向左 (left)
# 向右 (right)
# 向上 (up)
# 向下 (down)

# agent.destroy() 函數採用了一組參數：direction。
# 有效的方向為：
# 前進 (forward)
# 退後 (back)
# 向左 (left)
# 向右 (right)
# 向上 (up)
# 向下 (down)

# agent.place() 函數採用了兩組參數。
# 欄位編號 (整數)：Agent 應使用哪一個庫存欄位。
# 方向 (字串)：你希望 Agent 放置物品的方向。
# 有效的方向為：
# 前進 (forward)
# 退後 (back)
# 向左 (left)
# 向右 (right)
# 向上 (up)
# 向下 (down)

# 使用 for 迴圈的程式碼
agent.give("BONE BLOCK", 64, 1)
for i in range(4):
    agent.move("forward")
    agent.move("forward")
    agent.destroy("down")
    agent.place("down", 1)

# 如果不使用 for 迴圈的程式碼
agent.give("BONE BLOCK", 64, 1)
agent.move("forward")
agent.move("forward")
agent.destroy("down")
agent.place("down", 1)
agent.move("forward")
agent.move("forward")
agent.destroy("down")
agent.place("down", 1)
agent.move("forward")
agent.move("forward")
agent.destroy("down")
agent.place("down", 1)
agent.move("forward")
agent.move("forward")
agent.destroy("down")
agent.place("down", 1)
# 如果不使用迴圈程式碼會變得很冗長
# 透過 for 迴圈可以讓程式碼更簡潔
# 並且更容易的執行重複的動作
# 如果不使用迴圈的作法就會像上面這樣

# 官方給予的程式碼有誤
# 修改前
agent.give("BONEBLOCK", 64, 1)
# 修改後
agent.give("BONE BLOCK", 64, 1)