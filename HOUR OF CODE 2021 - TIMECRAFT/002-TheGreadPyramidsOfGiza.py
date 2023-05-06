# The Great Pyramids of Giza 

# 提示
# 協助建築師完成三角形建築，打造經得起時間考驗的設計。
# 思考如何 建造一座金字塔。還需要增加 2 層：底部 3 個方塊，上方 1 個方塊。
# 編碼打造解決方案，使用 agent.give() 為你的 Agent 提供一堆 SANDSTONE，使用 agent.move() 來移動 Agent 的位置，然後使用 agent.place() 將方塊放置在 3 層金字塔結構上。

# agent.give() 函數採用了三組參數。
# 物品 (字串)：你要給 Agent 的物品。
# 數量 (整數)：Agent 將收到多少物品。
# 欄位 (整數)：Agent 接收物品的庫存欄位。

# agent.move() 函數採用了一個參數：方向。
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

# agent.turn() 函數採用了一組參數：turn_direction。
# 有效的方向為：
# 向左 (left)
# 向右 (right)

# 要求：
# 指導建築師如何使用 SANDSTONE 建造 2 層的金字塔

# 比較簡單的做法
# 在這裡編寫程式碼

agent.give("SANDSTONE", 64, 1)
agent.move("forward")
agent.place("back", 1)
agent.move("forward")
agent.place("back", 1)
agent.move("forward")
agent.place("back", 1)
agent.move("up")

agent.turn("left")
agent.turn("left")

agent.move("forward")
agent.place("forward", 1)



# 比較進階的做法
agent.give("SANDSTONE", 64, 1) # 給 Agent 64個沙岩放在物品欄1
