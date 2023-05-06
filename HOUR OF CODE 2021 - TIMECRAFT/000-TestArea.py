# 測試區

# 提示：
# 歡迎來到第一個編碼任務。讓我們測試一下 Time Agent，看看 Time Agent 是否會依照你的程式碼行動。
# 使用 agent.move() 將 Agent 向前移動 3 個方塊。
# 按下「執行」以執行程式碼。
# agent.move() 函數採用了一組參數：direction。
# 有效的方向為：
# 前進 (forward)
# 退後 (back)
# 向左 (left)
# 向右 (right)
# 向上 (up)
# 向下 (down)

# 要求：
# 移動 Agent 向前 3 個方塊就定位。

# 比較簡單的做法
# 直接移動三次
agent.move("forward")
agent.move("forward")
agent.move("forward")

# 比較進階的做法
# 使用 for 迴圈設定範圍為3次 (0~2)
# 在 for 迴圈當中執行 "前進"
for i in range(3):
	agent.move("forward")